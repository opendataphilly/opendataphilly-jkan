# 0001 - Search by Location

## Context

There is currently no way to access a fine-grain view of datasets that could be relevant to a user's administrative boundary of interest. The need for additional locational analysis on the user's end may discourage engagement with OpenDataPhilly and its catalog. Engagement in the project will be encouraged if users have the ability to access data specific to their area of interest.

## Decision

The key component of this project is a github action that produces location metadata for datasets, which can be used to expand the search feature. This action performs the following:
- Stands up an ephemeral PostGRES database
- Imports the datasets into the database
- Determines what administrative boundaries each dataset falls under
- Produces a JSON file consumable by the front-end

The github action will be triggered when a pull request is merged that adds a dataset or updates the dataset's resources. The result will be that the generated JSON file is checked in.

In the front end, the administrative boundaries will be searchable via an embedded Leaflet map on the homepage and via the existing search feature.

## Consequences

There is a possibility that a long running github action could incur some costs, which can be paid for or avoided by implementing self-hosted runners into the process. The free tier permints 2,000 mins per month and 500 MB of storage.

A long running action could also increase deployment time- this is not typically a large concern.

Some handling will have to be done for datasets that are relevant to the whole city or for which the analysis fails to determine any spatial connection to the administrative boundaries included in the analysis.
