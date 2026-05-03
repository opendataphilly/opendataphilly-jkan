"""
odp-check-data-links.py

Iterates through JKAN markdown dataset files, tests each resource URL
and optional maintainer_link, logs results, and prints a progress indicator.
"""

import logging
import time
from datetime import date
from pathlib import Path

import frontmatter
import requests

# --- Configuration ---
TEST_MODE     = True           # If True, process only TEST_SIZE datasets
TEST_SIZE     = 10             # Number of datasets to process in TEST_MODE
FETCH_TIMEOUT = 10             # Seconds to wait for each HTTP response
LOG_BASE_NAME = "odp-link-check"

# Paths are resolved relative to this script's parent directory so the script
# works regardless of the working directory it is invoked from.
_REPO_ROOT   = Path(__file__).resolve().parent.parent
LOG_DIR      = _REPO_ROOT / "import/logs"
DATASET_PATH = _REPO_ROOT / "_datasets"

# ---------------------------------------------------------------------------

OK               = "OK"
REDIRECT         = "REDIRECT"
FORBIDDEN        = "FORBIDDEN"
NOT_FOUND        = "NOT FOUND"
SERVER_ERROR     = "SERVER ERROR"
OTHER_ERROR      = "OTHER ERROR"
TIMEOUT          = "TIMEOUT"
CONNECTION_ERROR = "CONNECTION ERROR"

ERROR_STATUSES = {FORBIDDEN, NOT_FOUND, SERVER_ERROR, OTHER_ERROR, TIMEOUT, CONNECTION_ERROR}


def setup_logging() -> tuple[logging.Logger, Path]:
    log_path = Path(LOG_DIR)
    log_path.mkdir(parents=True, exist_ok=True)
    log_file = log_path / f"{LOG_BASE_NAME}-{date.today().isoformat()}.log"

    logger = logging.getLogger("odp")
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)

    return logger, log_file


def fetch_url(url: str) -> tuple[str, str, str | None]:
    """
    Return (status_label, details, final_url).
    Tries HEAD first; falls back to GET on 405.
    Retries once after a brief pause on network-level errors.
    """
    def _attempt(method: str) -> requests.Response:
        return requests.request(
            method, url, timeout=FETCH_TIMEOUT,
            allow_redirects=True,
            headers={"User-Agent": "odp-link-checker/1.0"},
        )

    for attempt in range(2):
        try:
            resp = _attempt("HEAD")
            if resp.status_code == 405:
                resp = _attempt("GET")

            redirected = len(resp.history) > 0
            if redirected:
                return REDIRECT, "", resp.url

            code = resp.status_code
            if 200 <= code < 300:
                return OK, "", resp.url
            if code == 403:
                return FORBIDDEN, str(code), resp.url
            if code == 404:
                return NOT_FOUND, str(code), resp.url
            if 500 <= code < 600:
                return SERVER_ERROR, str(code), resp.url
            return OTHER_ERROR, str(code), resp.url

        except requests.exceptions.Timeout:
            if attempt == 0:
                time.sleep(1)
                continue
            return TIMEOUT, "Request timed out", None
        except requests.exceptions.RequestException as exc:
            if attempt == 0:
                time.sleep(1)
                continue
            return CONNECTION_ERROR, str(exc), None

    return CONNECTION_ERROR, "Unknown error", None  # unreachable


def log_result(
    logger: logging.Logger,
    title: str,
    link_name: str,
    label: str,
    url: str,
    details: str,
    final_url: str | None,
) -> None:
    prefix = f"{title} | {link_name}"
    if label == OK:
        logger.info("%s | OK | %s", prefix, url)
    elif label == REDIRECT:
        logger.warning("%s | REDIRECT %s -> %s", prefix, url, final_url)
    else:
        logger.error("%s | %s | %s | %s", prefix, label, url, details)


def check_dataset(dataset_file: Path, logger: logging.Logger) -> dict:
    """
    Process one dataset file.
    Returns {"errors": [...], "stats": {"total": n, "ok": n, "redirects": n}}.
    """
    post = frontmatter.load(str(dataset_file))
    title = post.get("title") or dataset_file.stem

    urls: list[tuple[str, str]] = []
    for resource in post.get("resources") or []:
        url = (resource.get("url") or "").strip()
        if url:
            urls.append((resource.get("name") or "unnamed resource", url))

    maintainer_link = (post.get("maintainer_link") or "").strip()
    if maintainer_link:
        urls.append(("maintainer_link", maintainer_link))

    errors: list[dict] = []
    stats = {"total": 0, "ok": 0, "redirects": 0}

    for link_name, url in urls:
        label, details, final_url = fetch_url(url)
        log_result(logger, title, link_name, label, url, details, final_url)
        stats["total"] += 1
        if label == OK:
            stats["ok"] += 1
        elif label == REDIRECT:
            stats["redirects"] += 1
        if label in ERROR_STATUSES:
            errors.append({"title": title, "name": link_name, "label": label, "url": url})

    return {"errors": errors, "stats": stats}


def write_summary(
    logger: logging.Logger,
    dataset_count: int,
    total_urls: int,
    ok_count: int,
    redirect_count: int,
    errors: list[dict],
) -> None:
    lines = [
        "========== RUN SUMMARY ==========",
        f"Datasets processed : {dataset_count}",
        f"Total URLs tested  : {total_urls}",
        f"  OK               : {ok_count}",
        f"  Redirects (WARN) : {redirect_count}",
        f"  Errors           : {len(errors)}",
        "",
        "ERRORED URLs:",
    ]
    if errors:
        for e in errors:
            lines.append(f"  - {e['title']} | {e['name']} | {e['label']} | {e['url']}")
    else:
        lines.append("  None")
    lines.append("=================================")
    logger.info("\n".join(lines))


def main() -> None:
    logger, log_file = setup_logging()

    all_files = sorted(Path(DATASET_PATH).glob("*.md"))

    if TEST_MODE:
        files = all_files[:TEST_SIZE]
        logger.info("TEST MODE: processing %d of %d datasets", len(files), len(all_files))
    else:
        files = all_files

    total_datasets = len(files)
    all_errors: list[dict] = []
    total_urls = ok_count = redirect_count = 0

    for idx, dataset_file in enumerate(files, start=1):
        pct = int(idx / total_datasets * 100)
        print(f"\rChecking links... {pct}% ({idx}/{total_datasets} datasets)", end="", flush=True)

        result = check_dataset(dataset_file, logger)
        all_errors.extend(result["errors"])
        total_urls     += result["stats"]["total"]
        ok_count       += result["stats"]["ok"]
        redirect_count += result["stats"]["redirects"]

    print(f"\nDone. Results written to {log_file.resolve()}")
    write_summary(logger, total_datasets, total_urls, ok_count, redirect_count, all_errors)


if __name__ == "__main__":
    main()
