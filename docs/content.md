# Adding and editing content

## How content is organized

Editable JKAN content comprises datasets and organizations, and these live in the following directories:
- `_datasets`
- `_organizations`

## Adding content

In order to add an organization, for example, you just need to create a new markdown file under `_organizations` and fill it with YAML following the schema of the sample organization. Datasets work the same way but with their respective directories.

### Dataset template

```
---
category:
- A category matching a file in _dataset_categories (see name property)
- You can apply multiple categories just by adding another line
maintainer: Put the maintainer name here
maintainer_email: Put the maintainer email here
notes: "This will become the description on the detail page"
organization: An organization matching a file in _organizations (see title property)
resources:
- description: Optionally, put a resource description here
  format: Put the resource format here, e.g. CSV, API Documentation (shows as a tag after the name)
  name: Put the resource name here
  url: Put the resource URL here
- description: Optionally, put a resource description here
  format: Put another resource format here, e.g. CSV, API Documentation (shows as a tag after the name)
  name: Put another resource name here
  url: Put another resource URL here
schema: default
title: The title of your dataset
---
```

### Organization template

```
---
description: Put an organization description here
logo: Optionally, include a path or url for a logo image (e.g. img/organizations/somelogo.jpg)
schema: default
title: Organization name
---
```

## Editing content

Editing is similarly just a matter of editing an existing markdown file.

## Test before posting a PR

Please test your changes locally before submitting a pull request. See the instructions for [running locally](running-locally.md), and make sure that any datasets or organizations that you create or edit look how you expect!

Routes to check:
- http://localhost:4000/organizations/new-or-edited-organization
- http://localhost:4000/datasets/new-or-edited-dataset
