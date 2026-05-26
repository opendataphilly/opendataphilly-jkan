#!/usr/bin/env python3
"""
normalize_tags.py - Apply tag normalization to all dataset files.

Reads scripts/tag_normalization.yml for the raw->canonical mapping,
then rewrites the tags: block in every _datasets/*.md file.

Usage:
    python scripts/normalize_tags.py --dry-run   # Preview normalization changes
    python scripts/normalize_tags.py             # Apply normalization
"""

import re
import sys
import argparse
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent
NORM_MAP_FILE = Path(__file__).parent / "tag_normalization.yml"
DATASETS_DIR = REPO_ROOT / "_datasets"


def load_normalization_map():
    with open(NORM_MAP_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["mappings"]


def extract_tags(content):
    """
    Extract raw tags from YAML front matter.
    Returns (tags_list, match_object, style) or ([], None, None) if no tags found.

    Handles three styles:
      block:     tags:\n  - foo\n  - bar
      inline:    tags: [foo, bar]
      same_line: tags: foo, bar
    """
    # Block style: tags:\n  - tag (may span multiple lines)
    block = re.search(r'^(tags:\s*\n)((?:[ \t]*-[ \t]+[^\n]+\n)*)', content, re.MULTILINE)
    if block:
        items_text = block.group(2)
        tags = re.findall(r'^[ \t]*-[ \t]+(.+?)[ \t]*$', items_text, re.MULTILINE)
        if tags:
            return tags, block, 'block'

    # Inline style: tags: [foo, bar]
    inline = re.search(r'^tags:\s*\[([^\]]*)\]', content, re.MULTILINE)
    if inline:
        raw = inline.group(1)
        tags = [t.strip().strip("\"'") for t in raw.split(',') if t.strip()]
        if tags:
            return tags, inline, 'inline'

    # Same-line comma style: tags: foo, bar
    same_line = re.search(r'^tags:\s+([^\[\{][^\n]*)$', content, re.MULTILINE)
    if same_line:
        raw = same_line.group(1)
        tags = [t.strip() for t in raw.split(',') if t.strip()]
        if tags:
            return tags, same_line, 'same_line'

    return [], None, None


def normalize_tags(raw_tags, norm_map):
    """Map each raw tag to its canonical label and deduplicate."""
    seen = set()
    result = []
    for raw in raw_tags:
        canonical = norm_map.get(raw, raw)
        if canonical not in seen:
            result.append(canonical)
            seen.add(canonical)
    return sorted(result)


def _yaml_safe(value):
    """Quote values that YAML would otherwise parse as non-strings (numbers,
    booleans, null) so dataset tags always round-trip as strings — Jekyll's
    slugify filter crashes on Integer (e.g., a bare `- 311`)."""
    if re.fullmatch(r"-?\d+(\.\d+)?", value) or value.lower() in (
        "null", "true", "false", "yes", "no", "on", "off", "~", ""
    ):
        return f'"{value}"'
    return value


def build_block(tags):
    """Build YAML block-style tags section."""
    if not tags:
        return "tags:\n"
    return "tags:\n" + "".join(f"  - {_yaml_safe(tag)}\n" for tag in tags)


def process_file(filepath, norm_map, dry_run=False):
    """
    Process one dataset file.
    Returns (changed: bool, old_tags: list, new_tags: list).
    """
    content = filepath.read_text(encoding="utf-8")
    raw_tags, match, style = extract_tags(content)

    if not raw_tags:
        return False, [], []

    normalized = normalize_tags(raw_tags, norm_map)

    if raw_tags == normalized and style == 'block':
        return False, raw_tags, normalized

    if not dry_run:
        if style == 'block':
            # Replace header + items together (group 0 = full match)
            new_content = content[:match.start()] + build_block(normalized) + content[match.end():]
        else:
            # Replace the whole match (inline / same-line → block style)
            new_content = content[:match.start()] + build_block(normalized) + content[match.end():]

        filepath.write_text(new_content, encoding="utf-8")

    return True, raw_tags, normalized


def main():
    parser = argparse.ArgumentParser(description="Normalize tags in all _datasets/*.md files.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing any files")
    args = parser.parse_args()

    norm_map = load_normalization_map()
    dataset_files = sorted(DATASETS_DIR.glob("*.md"))

    changed = 0
    unchanged = 0
    errors = []

    for filepath in dataset_files:
        try:
            was_changed, old_tags, new_tags = process_file(filepath, norm_map, args.dry_run)
            if was_changed:
                changed += 1
                if args.dry_run:
                    print(f"\n{filepath.name}:")
                    print(f"  Before: {old_tags}")
                    print(f"  After:  {new_tags}")
            else:
                unchanged += 1
        except Exception as e:
            errors.append((filepath.name, str(e)))
            print(f"ERROR {filepath.name}: {e}", file=sys.stderr)

    prefix = "DRY RUN — " if args.dry_run else ""
    print(f"\n{prefix}{changed} files changed, {unchanged} unchanged, {len(errors)} errors")

    if errors:
        print("\nErrors:")
        for name, err in errors:
            print(f"  {name}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
