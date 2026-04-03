import os
import re
import logging
import datetime
import frontmatter
import requests
import isodate

# ---------------------------------------------------------------------------
# Configuration constants — edit these to match your local environment
# ---------------------------------------------------------------------------

# Path to the local clone of the OpenDataPhilly JKAN repository
REPO_PATH = "C:\sandbox\OpenDataPhilly-jkan"

# Directory where log files will be written
LOG_DIR = "C:\sandbox\OpenDataPhilly-jkan\import\logs"

# Base name used to construct log filenames
LOG_BASE_NAME = "odp-phl-modified"

# ArcGIS Hub API base URL for dataset metadata
ARCGIS_API_BASE_URL = "https://hub.arcgis.com/api/v3/datasets"

# Resource URL domains that indicate an ArcGIS-hosted dataset
ARCGIS_SOURCE_DOMAINS = [
    "data-phl.opendata.arcgis.com",
    "hub.arcgis.com",
    "opendata.arcgis.com",
]

# When True, only the first 10 datasets are processed (for testing)
TEST_MODE = True

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

# Custom log level for UPDATE messages (between INFO and WARNING)
UPDATE_LEVEL = 25
logging.addLevelName(UPDATE_LEVEL, "UPDATE")


def log_update(self, message, *args, **kwargs):
    if self.isEnabledFor(UPDATE_LEVEL):
        self._log(UPDATE_LEVEL, message, args, **kwargs)


logging.Logger.update = log_update

SKIP_LEVEL = 21
logging.addLevelName(SKIP_LEVEL, "SKIP")


def log_skip(self, message, *args, **kwargs):
    if self.isEnabledFor(SKIP_LEVEL):
        self._log(SKIP_LEVEL, message, args, **kwargs)


logging.Logger.skip = log_skip


def setup_logging():
    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.strftime("%Y-%m-%d-%H%M%S")
    log_filename = f"{LOG_BASE_NAME}-{timestamp}.log"
    log_path = os.path.join(LOG_DIR, log_filename)

    os.makedirs(LOG_DIR, exist_ok=True)

    formatter = logging.Formatter(
        fmt="[%(asctime)s UTC] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    formatter.converter = lambda *args: datetime.datetime.now(
        datetime.timezone.utc
    ).timetuple()

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger("odp_modified")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("=== Run started ===")
    logger.info(f"Log file: {log_filename}")

    return logger


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_REPEATING_INTERVAL_RE = re.compile(r"^R\d*/P.*")


def is_repeating_interval(value):
    """Return True if the value looks like an ISO 8601 repeating interval."""
    s = str(value).strip()
    return bool(_REPEATING_INTERVAL_RE.match(s))


def find_arcgis_resource_url(resources):
    """Return the URL of the first resource whose URL contains an ArcGIS domain."""
    for resource in resources or []:
        url = resource.get("url", "") or ""
        for domain in ARCGIS_SOURCE_DOMAINS:
            if domain in url:
                return url
    return None


_DATASET_ID_RE = re.compile(r"/(?:datasets|maps)/([0-9a-fA-F]+(?:_\d+)?)")


def extract_dataset_id(url):
    """Extract and return the ArcGIS dataset ID (including layer suffix if present) from a URL."""
    match = _DATASET_ID_RE.search(url)
    if not match:
        return None
    return match.group(1)


def fetch_arcgis_modified(dataset_id):
    """
    Fetch the 'Data Updated' timestamp from the ArcGIS Hub API.
    Returns a datetime.date on success, raises on failure.
    """
    url = f"{ARCGIS_API_BASE_URL}/{dataset_id}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    ms_timestamp = data["data"]["attributes"]["modified"]
    dt = datetime.datetime.fromtimestamp(ms_timestamp / 1000, tz=datetime.timezone.utc)
    return dt.date()


def parse_existing_date(value):
    """
    Parse an existing modified date string as YYYY-MM-DD.
    Returns a datetime.date or raises ValueError.
    """
    s = str(value).strip()
    return datetime.date.fromisoformat(s)


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_dataset(filepath, logger):
    """
    Process a single dataset markdown file.
    Returns one of: "updated", "skipped", "error", "unchanged"
    """
    filename = os.path.basename(filepath)

    # 3a. Parse front matter
    try:
        post = frontmatter.load(filepath)
    except Exception as exc:
        logger.error(f"{filename}: failed to parse front matter — {exc}")
        return "error"

    # 3b. Check modified field for repeating interval
    modified_value = post.get("modified", None)
    if modified_value is not None and is_repeating_interval(modified_value):
        logger.skip(f"{filename}: modified field is a repeating interval ({modified_value}), ignoring.")
        return "skipped"

    # 3c. Identify ArcGIS Online resources
    resources = post.get("resources", [])
    arcgis_url = find_arcgis_resource_url(resources)
    if arcgis_url is None:
        logger.skip(f"{filename}: no ArcGIS Online resources found.")
        return "skipped"

    # 3d. Extract dataset ID
    dataset_id = extract_dataset_id(arcgis_url)
    if dataset_id is None:
        logger.error(f"{filename}: could not extract ArcGIS dataset ID from URL {arcgis_url}.")
        return "error"

    # 3e. Fetch ArcGIS metadata
    try:
        arcgis_date = fetch_arcgis_modified(dataset_id)
    except Exception as exc:
        logger.error(f"{filename}: ArcGIS API request failed for dataset {dataset_id} — {exc}")
        return "error"

    # 3g. Compare and update
    if not modified_value:
        # Empty or absent
        post["modified"] = arcgis_date.isoformat()
        logger.log(UPDATE_LEVEL, f"{filename}: modified was empty, set to {arcgis_date}.")
    else:
        try:
            existing_date = parse_existing_date(modified_value)
        except (ValueError, TypeError):
            logger.error(f"{filename}: could not parse modified value '{modified_value}' as a date.")
            return "error"

        if arcgis_date > existing_date:
            logger.log(UPDATE_LEVEL, f"{filename}: modified updated from {existing_date} to {arcgis_date}.")
            post["modified"] = arcgis_date.isoformat()
        elif existing_date.isoformat() != str(modified_value).strip():
            # Date is same or older but format differs — normalize
            post["modified"] = existing_date.isoformat()
        else:
            return "unchanged"

    # Write updated front matter back to file
    try:
        with open(filepath, "wb") as fh:
            frontmatter.dump(post, fh)
    except Exception as exc:
        logger.error(f"{filename}: failed to write updated file — {exc}")
        return "error"

    return "updated"


def main():
    logger = setup_logging()

    datasets_dir = os.path.join(REPO_PATH, "_datasets")
    all_files = sorted(
        os.path.join(datasets_dir, f)
        for f in os.listdir(datasets_dir)
        if f.endswith(".md")
    )

    if TEST_MODE:
        logger.warning("TEST MODE ENABLED — processing first 10 datasets only.")
        all_files = all_files[:10]

    logger.info(f"{len(all_files)} dataset files found.")

    updated = 0
    skipped = 0
    errors = 0

    for filepath in all_files:
        result = process_dataset(filepath, logger)
        if result == "updated":
            updated += 1
        elif result == "skipped":
            skipped += 1
        elif result == "error":
            errors += 1
        # "unchanged" counts toward neither updated nor skipped

    logger.info(f"Run complete. {updated} dataset(s) updated, {skipped} skipped, {errors} errors.")


if __name__ == "__main__":
    main()
