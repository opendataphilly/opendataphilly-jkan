## How to import data from a CKAN site

### Steps

- Open a shell here, at `/import`
- Run `./import_from_ckan.sh https://www.opendataphilly.org/api/action/package_list?all_fields=False` to generate working_files from `opendataphilly-ckan`, including:
  - A file enumerating the names to fetch metadata for: `import/working_files/all_dataset_names.txt`
  - A file containing the fetched dataset metadata: `import/working_files/odp_datasets.txt`
  - A JSON equivalent of the above: `import/working_files/odp_datasets.json`
  - Running this command command also creates `import/working_files/_datasets` and fills it with YAML front matter based on the above JSON datasets file; likewise for `import/working_files/_organizations`; `import/working_files/img/organizations` contains the organization logos.
- Take a look and make sure you're happy with the output in `_datasets`
  - `ls working_files/_datasets | wc -l` can help you verify that you got everything
- Run `mv working_files/_datasets/* ../_datasets` to move generated datasets to where JKAN expects them. This may overwrite the contents of `_datasets`.
- Run `mv working_files/_organizations/* ../_organizations` to move generated organizations to where JKAN expects them. This may overwrite the contents of `_organizations`.
- Run `mv working_files/img/organizations/* ../img/organizations` to move downloaded organization logos to where JKAN expects them. This may overwrite the contents of `img/organizations`.
