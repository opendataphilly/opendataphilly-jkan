"""
import-chester-county.py

Synchronizes Chester County, PA open datasets from the ArcGIS Hub API into
the OpenDataPhilly JKAN repository by creating, updating, or removing dataset
markdown files in the _datasets directory.

Usage:
    python import/import-chester-county.py

Prerequisites:
    pip install requests python-frontmatter python-slugify
"""

import os
import sys
import time
import logging
from datetime import datetime, timezone
from pathlib import Path

import requests
import frontmatter
from slugify import slugify

# ---------------------------------------------------------------------------
# Configuration constants
# ---------------------------------------------------------------------------

# Path to the local clone of the OpenDataPhilly JKAN repository
# REPO_PATH = "/path/to/local/opendataphilly-jkan"
REPO_PATH = "C:\sandbox\OpenDataPhilly-jkan-chester-cty\opendataphilly-jkan"

# Directory where log files will be written
# LOG_DIR = "/path/to/logs"
LOG_DIR = "C:\sandbox\OpenDataPhilly-jkan-chester-cty\opendataphilly-jkan\import\logs"

# Base name used to construct log filenames
LOG_BASE_NAME = "odp-chester-sync"

# Base file name prefix for Chester County datasets saved in OpenDataPhilly
MD_BASE_NAME = "chester-cty-"

# ArcGIS Hub API base URL for dataset metadata
ARCGIS_API_BASE_URL = "https://hub.arcgis.com/api/v3/datasets/"

# ArcGIS Hub portal base URL (used for dataset "about" pages)
ARCGIS_HUB_BASE_URL = "https://chester-county-s-gis-hub-chesco.hub.arcgis.com/datasets/"

ARCGIS_ORG_ID = "G4S1dGvn7PIgYd6Y"
ARCGIS_SOURCE_PREFIX = "ChescoMaps"
ARCGIS_FILTER_PARAMETERS = (
    "filter[openData]=true"
    "&filter[source]=prefixAll(ChescoMaps)"
    "&filter[hubType]=prefixAll(Feature)"
    "&page[size]=99"
)
# Filter parameters documented at:
# https://gist.github.com/jgravois/1b7ec5080e992a59f65cf7a2190e4365#get-apiv3datasets

# Resource URL domains that indicate an ArcGIS-hosted dataset
ARCGIS_SOURCE_DOMAINS = [
    "chester-county-s-gis-hub-chesco.hub.arcgis.com",
    "hub.arcgis.com",
    "opendata.arcgis.com",
]

# License value written to all ODP dataset files.
# Set to None (null) until Chester County confirms their licensing terms.
# Change this constant when the license is confirmed.
DATA_LICENSE = None

# Group ID mapping: Chester County ArcGIS group ID -> category name used in CATEGORY_MAP
GROUP_ID_MAP = {
    "805a2f3557a04848a36a0cac74853bee": "Boundaries & Basemaps = Boundaries",
    "ac492e2c70b44431a5b3ccf5c2721cf8": "Parcel Data",
    "eb0718839d134a468b2cacad83647d90": "Community Safety",
    "b9a32bde3113433e990268c09bcd8932": "Historic",
    "d65cd4a6ae114927a4ee9754b72e1e23": "Hydro",
    "22cdccc001bb4d5f98743a88ecd75b54": "Education",
    "dc2b0918c9a5493f89651e5d93c60eea": "Elections",
    "a57097ec7eb9406595bfe358e148889b": "Housing, Census & Economy",
    "58626590ac2548a9921dd6eb66820047": "Land Use",
    "4b440536b41742f4ad888b06d3435ff9": "Parks & Recreation",
    "fcad5c38b09e474faa253d7b28a36e82": "Transportation",
}

# Category mapping: Chester County category -> ODP categories (list)
CATEGORY_MAP = {
    "Boundaries & Basemaps = Boundaries": ["Boundaries"],
    "Parcel Data": ["Real Estate / Land Records"],
    "Community Safety": ["Public Safety", "Health / Human Services"],
    "Historic": ["Planning / Zoning"],
    "Hydro": ["Environment"],
    "Education": ["Education"],
    "Elections": ["Elections / Politics"],
    "Housing, Census & Economy": ["Planning / Zoning", "Real Estate / Land Records", "Economy"],
    "Land Use": ["Planning / Zoning", "Real Estate / Land Records"],
    "Parks & Recreation": ["Parks / Recreation"],
    "Transportation": ["Transportation"],
    "Safety & Health": ["Health / Human Services", "Public Safety"],
    "TIP": ["Transportation", "Planning / Zoning"],
    "Transit": ["Transportation"],
}

# Update frequency mapping: ArcGIS updateFrequency value -> ISO 8601 repeating interval.
# Reserved for future use when ArcGIS exposes an updateFrequency field.
FREQUENCY_MAP = {
    "daily": "R/P1D",
    "weekly": "R/P1W",
    "monthly": "R/P1M",
    "annually": "R/P1Y",
    "as_needed": None,
    "not_planned": None,
}

# Dataset slugs to skip entirely during processing.
# Add slugified dataset names (e.g. "parcel-boundaries") to exclude them.
# The MD_BASE_NAME prefix should NOT be included in these values.
EXCLUDED_SLUGS: list[str] = []

# Prefix prepended to the title of datasets whose title does not already
# contain the word "Chester" (case-insensitive). Set to None to disable.
TITLE_PREFIX = "Chester County"

# Spatial reference ID used in ArcGIS download URLs.
# 4326 = WGS 84 (standard lat/lon); 2272 = Pennsylvania State Plane South (feet)
SPATIAL_REF_ID = "4326"

# When True, only the first 10 datasets are processed (for testing)
TEST_MODE = False

# When True, log all changes that would be made but do not write, update,
# or delete any files on disk
DRY_RUN = False

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

def setup_logging(log_dir: str, log_base_name: str) -> tuple[logging.Logger, str]:
    """Create a new timestamped log file and return the configured logger and filename."""
    log_dir_path = Path(log_dir)
    log_dir_path.mkdir(parents=True, exist_ok=True)

    now_utc = datetime.now(tz=timezone.utc)
    log_filename = f"{log_base_name}-{now_utc.strftime('%Y-%m-%d-%H%M%S')}.log"
    log_path = log_dir_path / log_filename

    logger = logging.getLogger("odp-chester-sync")
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    fmt = logging.Formatter("[%(asctime)s UTC] [%(levelname)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fmt.converter = time.gmtime  # force UTC timestamps
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger, log_filename


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def fetch_with_retry(url: str, logger: logging.Logger, timeout: int = 30) -> requests.Response:
    """
    Fetch a URL, retrying once after 5 seconds on failure.
    Raises requests.RequestException on persistent failure.
    """
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp
    except (requests.RequestException, requests.HTTPError) as exc:
        logger.warning(f"Request failed ({exc}), retrying in 5 seconds: {url}")
        time.sleep(5)
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp


# ---------------------------------------------------------------------------
# Date conversion
# ---------------------------------------------------------------------------

def epoch_ms_to_date(epoch_ms) -> str | None:
    """Convert Unix epoch milliseconds (int) to a YYYY-MM-DD string, or None."""
    if epoch_ms is None:
        return None
    try:
        return datetime.fromtimestamp(int(epoch_ms) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OSError):
        return None


# ---------------------------------------------------------------------------
# Step 2a: Enumerate existing Chester County ODP files
# ---------------------------------------------------------------------------

def get_existing_odp_files(repo_path: str, md_base_name: str) -> dict[str, Path]:
    """
    Return a dict mapping filename stem -> Path for all .md files in
    _datasets/ whose name starts with md_base_name.
    """
    datasets_dir = Path(repo_path) / "_datasets"
    result: dict[str, Path] = {}
    if not datasets_dir.is_dir():
        return result
    for p in datasets_dir.glob(f"{md_base_name}*.md"):
        result[p.stem] = p
    return result


# ---------------------------------------------------------------------------
# Step 2b: Fetch Chester County datasets from ArcGIS Hub
# ---------------------------------------------------------------------------

def fetch_arcgis_datasets(logger: logging.Logger) -> dict[str, dict]:
    """
    Paginate through the ArcGIS Hub API and return a dict mapping
    dataset id -> attributes for all open Chester County datasets.
    Aborts (raises SystemExit) if the listing endpoint is unreachable.
    """
    datasets: dict[str, dict] = {}
    url = f"{ARCGIS_API_BASE_URL}?{ARCGIS_FILTER_PARAMETERS}"
    page_num = 0

    while url:
        page_num += 1
        try:
            resp = fetch_with_retry(url, logger)
        except (requests.RequestException, requests.HTTPError) as exc:
            logger.error(f"ArcGIS listing endpoint failed: {exc}. Aborting run.")
            sys.exit(1)

        body = resp.json()
        records = body.get("data", [])
        page_count = len(records)

        for record in records:
            attrs = record.get("attributes", {})
            if not attrs.get("openData", False):
                continue
            dataset_id = record.get("id")
            if dataset_id:
                datasets[dataset_id] = attrs

        total = body.get("meta", {}).get("totalCount", 0)
        logger.info(
            f"Fetched page {page_num} of ArcGIS Hub results ({page_count} records); total: {total}"
        )

        next_url = body.get("links", {}).get("next")
        url = next_url if next_url else None

    return datasets


# ---------------------------------------------------------------------------
# Step 3b/3c: Build JKAN frontmatter dict from ArcGIS attributes
# ---------------------------------------------------------------------------

def clean_description(text: str | None) -> str | None:
    """Replace HTML <div> and </div> tags with <br/> in a description string."""
    if not text:
        return text
    import re
    return re.sub(r"</?div[^>]*>", "<br/>", text, flags=re.IGNORECASE)


def map_categories(
    arcgis_categories: list,
    arcgis_group_ids: list,
    filename: str,
    logger: logging.Logger,
) -> list[str]:
    """
    Map ArcGIS category strings and group IDs to ODP category values.
    Both sources are checked; results are deduplicated.
    """
    logger.info(f"{filename}: ArcGIS categories = {arcgis_categories or '(none)'}")
    logger.info(f"{filename}: ArcGIS groupIds = {arcgis_group_ids or '(none)'}")

    # Resolve group IDs to category name strings first
    resolved_cats: list[str] = list(arcgis_categories or [])
    for gid in (arcgis_group_ids or []):
        cat_name = GROUP_ID_MAP.get(gid)
        if cat_name:
            resolved_cats.append(cat_name)
        else:
            logger.warning(f"{filename}: Unknown groupId \"{gid}\" — skipping.")

    odp_categories: list[str] = []
    seen: set[str] = set()

    for cat in resolved_cats:
        if cat in CATEGORY_MAP:
            for odp_cat in CATEGORY_MAP[cat]:
                if odp_cat not in seen:
                    odp_categories.append(odp_cat)
                    seen.add(odp_cat)
        else:
            logger.warning(
                f"{filename}: Unknown category \"{cat}\" — skipping."
            )

    return odp_categories


def build_resources(dataset_id: str, dataset_name: str) -> list[dict]:
    """Build the four standard resource entries for a dataset."""
    base_download = (
        f"{ARCGIS_API_BASE_URL}{dataset_id}/downloads/data"
        f"?format={{fmt}}&spatialRefId={SPATIAL_REF_ID}&where=1%3D1"
    )
    return [
        {
            "name": f"{dataset_name} (CSV)",
            "url": base_download.format(fmt="csv"),
            "format": "CSV",
        },
        {
            "name": f"{dataset_name} (GeoJSON)",
            "url": base_download.format(fmt="geojson"),
            "format": "GeoJSON",
        },
        {
            "name": f"{dataset_name} (SHP)",
            "url": base_download.format(fmt="shp"),
            "format": "SHP",
        },
        {
            "name": f"{dataset_name} (Metadata)",
            "url": f"{ARCGIS_HUB_BASE_URL}{dataset_id}/about",
            "format": "HTML",
        },
    ]


def build_frontmatter(
    dataset_id: str,
    attrs: dict,
    filename: str,
    logger: logging.Logger,
) -> dict:
    """Construct the full JKAN frontmatter dict from ArcGIS attributes."""
    name = attrs.get("name", "")
    if TITLE_PREFIX and "chester" not in name.lower():
        title = f"{TITLE_PREFIX} {name}"
    else:
        title = name

    odp_categories = map_categories(
        attrs.get("categories", []) or [],
        attrs.get("groupIds", []) or [],
        filename,
        logger,
    )

    tags = attrs.get("tags") or []

    return {
        "title": title,
        "organization": "Chester County GIS",
        "notes": clean_description(attrs.get("description")),
        "area_of_interest": "Chester County, PA",
        "created": epoch_ms_to_date(attrs.get("created")),
        "category": odp_categories,
        "license": DATA_LICENSE,
        "maintainer": "Chester County GIS",
        "maintainer_email": "gis@chesco.org",
        "maintainer_link": "https://chester-county-s-gis-hub-chesco.hub.arcgis.com/",
        "maintainer_phone": None,
        "metadata_modified": epoch_ms_to_date(attrs.get("itemModified")),
        "modified": epoch_ms_to_date(attrs.get("modified")),
        "resources": build_resources(dataset_id, name),
        "source": "Chester County GIS",
        "tags": tags,
        "time_period": None,
        "usage": None,
    }


# ---------------------------------------------------------------------------
# Frontmatter comparison
# ---------------------------------------------------------------------------

def diff_frontmatter(existing: dict, new: dict) -> list[str]:
    """Return a list of field names that differ between existing and new dicts."""
    all_keys = set(existing.keys()) | set(new.keys())
    changed = []
    for key in sorted(all_keys):
        if existing.get(key) != new.get(key):
            changed.append(key)
    return changed


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

def write_md_file(path: Path, fm_dict: dict) -> None:
    """Serialize frontmatter dict to a JKAN markdown file (empty body)."""
    post = frontmatter.Post("", **fm_dict)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(frontmatter.dumps(post))
        fh.write("\n")


def read_md_frontmatter(path: Path) -> dict:
    """Parse and return the frontmatter dict from an existing markdown file."""
    with open(path, "r", encoding="utf-8") as fh:
        post = frontmatter.load(fh)
    return dict(post.metadata)


# ---------------------------------------------------------------------------
# Slug collision guard
# ---------------------------------------------------------------------------

def is_collision(filename: str, existing_odp_files: dict[str, Path], repo_path: str) -> bool:
    """
    Return True if the target filename exists in _datasets/ but does NOT
    start with MD_BASE_NAME (i.e., it belongs to a different publisher).
    """
    stem = Path(filename).stem
    datasets_dir = Path(repo_path) / "_datasets"
    candidate = datasets_dir / filename
    if not candidate.exists():
        return False
    # File exists; check if it's already a Chester County file
    return stem not in existing_odp_files


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # ------------------------------------------------------------------
    # Step 1: Initialize logging
    # ------------------------------------------------------------------
    logger, log_filename = setup_logging(LOG_DIR, LOG_BASE_NAME)
    logger.info("=== Run started ===")
    logger.info(f"Log file: {log_filename}")

    if DRY_RUN:
        logger.warning("DRY RUN ENABLED — no files will be written, updated, or deleted.")

    # ------------------------------------------------------------------
    # Step 2a: Enumerate existing Chester County ODP files
    # ------------------------------------------------------------------
    existing_odp_files = get_existing_odp_files(REPO_PATH, MD_BASE_NAME)
    logger.info(
        f"Found {len(existing_odp_files)} existing ODP files with prefix \"{MD_BASE_NAME}\""
    )

    # ------------------------------------------------------------------
    # Step 2b: Fetch ArcGIS Hub datasets
    # ------------------------------------------------------------------
    arcgis_datasets = fetch_arcgis_datasets(logger)

    # ------------------------------------------------------------------
    # Step 2c: Apply TEST_MODE truncation
    # ------------------------------------------------------------------
    if TEST_MODE:
        arcgis_datasets = dict(list(arcgis_datasets.items())[:10])
        logger.warning("TEST MODE ENABLED — processing first 10 datasets only.")

    # ------------------------------------------------------------------
    # Step 3: Loop 1 — Add and Update ODP files
    # ------------------------------------------------------------------
    counts = {"added": 0, "updated": 0, "deleted": 0}

    # Build a set of expected filename stems from the current ArcGIS results
    # (used later in Loop 2 to detect removals)
    expected_stems: set[str] = set()

    datasets_dir = Path(REPO_PATH) / "_datasets"

    for dataset_id, attrs in arcgis_datasets.items():
        name = attrs.get("name", "")
        slug = slugify(name)
        filename = f"{MD_BASE_NAME}{slug}.md"
        stem = f"{MD_BASE_NAME}{slug}"
        expected_stems.add(stem)
        # logger.info(f"{filename}: owner = {attrs.get('owner')}")

        # Exclusion list
        if slug in EXCLUDED_SLUGS:
            logger.info(f"SKIP {filename} (in EXCLUDED_SLUGS)")
            continue

        # Slug collision guard
        if is_collision(filename, existing_odp_files, REPO_PATH):
            logger.error(
                f"Slug collision: {filename} already exists and does not belong to "
                f"Chester County. Skipping dataset \"{name}\" ({dataset_id})."
            )
            continue

        new_fm = build_frontmatter(dataset_id, attrs, filename, logger)
        target_path = datasets_dir / filename

        if stem not in existing_odp_files:
            # New dataset
            if DRY_RUN:
                logger.warning(f"DRY RUN — would ADD {filename} (no file written)")
            else:
                try:
                    write_md_file(target_path, new_fm)
                    logger.info(f"ADD {filename}")
                except OSError as exc:
                    logger.error(f"Could not write {filename}: {exc}")
                    continue
            counts["added"] += 1
        else:
            # Existing dataset — compare fields
            try:
                existing_fm = read_md_frontmatter(existing_odp_files[stem])
            except OSError as exc:
                logger.error(f"Could not read {filename}: {exc}")
                continue

            changed_fields = diff_frontmatter(existing_fm, new_fm)
            if changed_fields:
                fields_str = ", ".join(changed_fields)
                if DRY_RUN:
                    logger.warning(
                        f"DRY RUN — would UPDATE {filename} "
                        f"(fields: {fields_str}) (no file written)"
                    )
                else:
                    try:
                        write_md_file(target_path, new_fm)
                        logger.info(f"UPDATE {filename} (fields changed: {fields_str})")
                    except OSError as exc:
                        logger.error(f"Could not write {filename}: {exc}")
                        continue
                counts["updated"] += 1
            # else: no changes — silent skip

    # ------------------------------------------------------------------
    # Step 4: Loop 2 — Delete removed datasets
    # ------------------------------------------------------------------
    for stem, path in existing_odp_files.items():
        if stem not in expected_stems:
            filename = path.name
            if DRY_RUN:
                logger.warning(f"DRY RUN — would DELETE {filename} (no file deleted)")
            else:
                try:
                    path.unlink()
                    logger.info(f"DELETE {filename} (no longer in Chester County catalog)")
                except OSError as exc:
                    logger.error(f"Could not delete {filename}: {exc}")
                    continue
            counts["deleted"] += 1

    # ------------------------------------------------------------------
    # Step 5: Finalize and report
    # ------------------------------------------------------------------
    added = counts["added"]
    updated = counts["updated"]
    deleted = counts["deleted"]
    total_changes = added + updated + deleted

    if DRY_RUN:
        if total_changes:
            logger.info(
                f"DRY RUN complete. Would have added {added}, "
                f"updated {updated}, deleted {deleted} file(s)."
            )
        else:
            logger.info("DRY RUN complete. No changes found.")
    else:
        if total_changes:
            logger.info(
                f"Run complete. Added {added}, updated {updated}, deleted {deleted} file(s)."
            )
        else:
            logger.info("Run complete. No changes found.")


if __name__ == "__main__":
    main()
