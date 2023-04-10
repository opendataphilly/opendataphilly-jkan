#!/usr/bin/python3

import argparse
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path

import requests
import yaml

working_files_dir = "working_files"
datasets_output_dir = f"{working_files_dir}/_datasets"
organizations_output_dir = f"{working_files_dir}/_organizations"
img_output_dir = f"{working_files_dir}/img"
organization_logos_output_path = "img/organizations"
organization_logos_output_dir = f"{working_files_dir}/{organization_logos_output_path}"
organizations_logos_input_url = "https://ckan.opendataphilly.org/uploads/group"


# Copied Django's slugify from https://github.com/django/django/blob/main/django/utils/text.py
# It's somewhat overkill for our case (which is just generating valid filenames), but it's relatively
# short, we're familiar with it, and it should be thoroughly battle-tested at this point.
def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def make_resource(ckan_resource):
    """Convert a CKAN resource metadata into JKAN frontmatter"""
    return {
        "name": ckan_resource.get("name"),
        "url": ckan_resource.get("url"),
        "format": ckan_resource.get("format"),
        "description": ckan_resource.get("description"),
    }


def download_organization_logo(image_url):
    url = f"{organizations_logos_input_url}/{image_url}"
    try:
        from urllib3.exceptions import InsecureRequestWarning

        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        r = requests.get(
            url, stream=True, verify=False
        )  # stream so image isn't downloaded to memory
        if r.status_code == 200:
            with open(f"{organization_logos_output_dir}/{image_url}", "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            return True
        else:
            print(f"Failed with {r.status_code}: {url}")
            return False
    except Exception as e:
        print(f"Failed with url: {url}\n{e}")
        return False


def make_dataset_frontmatter(ckan_ds):
    """Formats a CKAN dataset metadata into JKAN frontmatter for a dataset"""
    data = ckan_ds["result"]
    extras = {extra.get("key"): extra.get("value") for extra in data.get("extras", [])}

    return {
        "area_of_interest": extras.get("Area of Interest"),
        "maintainer_link": extras.get("Maintainer Link"),
        "maintainer_phone": extras.get("Maintainer Phone"),
        "opendataphilly_rating": extras.get("OpenDataPhilly Rating"),
        "time_period": extras.get("Time Period"),
        "usage": extras.get("Usage"),
        "category": [group.get("title") for group in data.get("groups", [])],
        "created": data.get("metadata_created"),
        "license": data.get("license_title"),
        "maintainer": data.get("maintainer"),
        "maintainer_email": data.get("maintainer_email"),
        "notes": data.get("notes"),
        "source": data.get("url"),
        "organization": data.get("organization", {}).get("title", None),
        "resources": [
            make_resource(resource) for resource in data.get("resources", [])
        ],
        "schema": "philadelphia",
        "tags": [tag.get("display_name") for tag in data.get("tags", [])],
        "title": data[
            "title"
        ],  # title is required by write_yaml; throw if it's missing
    }


def make_organization_frontmatter(ckan_ds):
    """Formats a CKAN dataset metadata into JKAN frontmatter for an organization"""
    data = ckan_ds["result"]
    org = data.get("organization", {})
    image_url = org.get("image_url", None)
    if download_organization_logo(image_url) is True:
        # if download_organization_logo is successful, treat image_url as internal url
        # otherwise, try it as an external url
        image_url = f"{organization_logos_output_path}/{image_url}"

    return {
        "description": org.get("description", None),
        "logo": image_url,
        "schema": "default",
        "tags": [tag.get("display_name") for tag in data.get("tags")],
        "title": org.get("title", None),
    }


def write_frontmatter(metadata, output_path):
    filename = (
        slugify(metadata.get("name", metadata["title"]), allow_unicode=True) + ".md"
    )
    with open((Path(output_path) / filename), "w") as outfile:
        outfile.write("---\n")
        outfile.write(yaml.dump(metadata))
        outfile.write("---\n")


if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(
        description="Convert CKAN dataset metadat in JSON into JKAN frontmatter"
    )
    parser.add_argument(
        "--input_file",
        help="Path to a dump of CKAN datasets, in JSON format",
        default=f"{working_files_dir}/odp_datasets.json",
        action="store",
    )
    args = parser.parse_args()
    # Create output paths if they don't already exist
    if not Path(working_files_dir).is_dir():
        os.makedirs(working_files_dir)
    if not Path(datasets_output_dir).is_dir():
        os.makedirs(datasets_output_dir)
    if not Path(organizations_output_dir).is_dir():
        os.makedirs(organizations_output_dir)
    if not Path(img_output_dir).is_dir():
        os.makedirs(img_output_dir)
    if not Path(organization_logos_output_dir).is_dir():
        os.makedirs(organization_logos_output_dir)

    # Open input
    with open(args.input_file) as input_file:
        dataset_json_array = json.load(input_file)
        for dataset_json in dataset_json_array:
            if dataset_json["result"]["type"] == "dataset":
                # Generate output
                dataset_frontmatter = make_dataset_frontmatter(dataset_json)
                organization_frontmatter = make_organization_frontmatter(dataset_json)
                # Write output
                write_frontmatter(dataset_frontmatter, datasets_output_dir)
                write_frontmatter(organization_frontmatter, organizations_output_dir)

    print("Done! Look in the import README to see what to do with these files")
