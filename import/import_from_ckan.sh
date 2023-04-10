#!/bin/bash

function usage() {
    echo -n \
         "Usage: $(basename "$0") ckan_site_to_import

Imports data from a CKAN site. Requires one positional argument giving the site to import from.
"
}

if [ "${1:-}" = "--help" ] || [[ $# -eq 0 ]]
then
    usage
else
    if [ ! -d working_files ] # only generates working files if the dir doesn't exist
    then
        echo "Seems like you need working files. Generating them now!"
        mkdir working_files
        # Get dataset names from ckan_site_to_import
        curl -k "${1}" | jq -r '.result | .[]' > working_files/all_dataset_names.txt

        # Get the datasets and filter out failed requests
        # shellcheck disable=SC2002
        cat working_files/all_dataset_names.txt | xargs -d"\n" --replace='{}' curl -k -fw "\n" 'https://ckan.opendataphilly.org/api/action/package_show?id={}&include_datasets=False&include_password_hash=True' > working_files/odp_datasets.txt

        # Convert JSONL/JSONND to JSON
        # shellcheck disable=SC2002
        cat working_files/odp_datasets.txt | jq -s > working_files/odp_datasets.json

    else
        echo "Seems like you already have working files, so I'll try to use those! If you don't, please delete the /working_files directory and I'll regenerate them."
    fi

    python3 ckan2jkan.py
fi
