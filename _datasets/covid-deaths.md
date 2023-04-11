---
area_of_interest: null
category:
- Economy
- Health / Human Services
created: '2020-05-05T17:48:08.839201'
license: Other (City of Philadelphia)
maintainer: PublicHealthInfo@phila.gov
maintainer_email: PublicHealthInfo@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "***As of May 2022, these datasets moved from daily updates to weekly updates\
  \ every Monday.***\r\n\r\n**For greatest accuracy, please use the latest dataset\
  \ for all analysis and reporting as opposed to any data you downloaded prior to\
  \ September 29, 2020. All datasets now reflect counts from test collection dates\
  \ instead of the previously displayed result dates.  These changes will adjust,\
  \ for example, the count of cases for each day. PDPH has also added 376 confirmed\
  \ COVID-19 cases (positive tests) that were previously missing from the data.**\r\
  \n\r\nDeidentified, aggregate datasets showing COVID deaths by date, zip, race,\
  \ or age. You can [find COVID cases datasets here](https://www.opendataphilly.org/dataset/covid-cases).\
  \ To protect the confidentiality of residents, PDPH suppresses the exact data for\
  \ any categories that have less than 6 counts (i.e. of cases or fatalities).\r\n\
  \r\nTrouble downloading or have questions about this City dataset? Visit the [OpenDataPhilly\
  \ Discussion Group](http://www.phila.gov/data/discuss/)"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: COVID Deaths by Date (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_deaths_by_date&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_deaths_by_date
- description: ''
  format: API
  name: COVID Deaths by Date (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_deaths_by_date
- description: ''
  format: Metadata
  name: COVID Deaths by Date (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5eb30f62d4c4600016078aad/representationdetails/5eb30f63d4c4600016078ab3/
- description: ''
  format: CSV
  name: COVID Deaths by ZIP (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_deaths_by_zip&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_deaths_by_zip
- description: ''
  format: SHP
  name: COVID Deaths by ZIP (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_deaths_by_zip&filename=covid_deaths_by_zip&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: COVID Deaths by ZIP (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_deaths_by_zip&filename=covid_deaths_by_zip&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Deaths by ZIP (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_deaths_by_zip
- description: ''
  format: Metadata
  name: COVID Deaths by ZIP (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5eb30f62d4c4600016078aad/representationdetails/5ed10dae6ab1ff00174a54c9/
- description: ''
  format: CSV
  name: COVID Death by Race (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_deaths_by_race&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_deaths_by_race
- description: ''
  format: API
  name: COVID Deaths by Race (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_deaths_by_race
- description: ''
  format: Metadata
  name: COVID Deaths by Race (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5eb30f62d4c4600016078aad/representationdetails/5efb45f7862e1c001a29864a/
- description: ''
  format: CSV
  name: COVID Deaths by Age (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_deaths_by_age&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_deaths_by_age
- description: ''
  format: API
  name: COVID Deaths by Age (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_deaths_by_age
- description: ''
  format: Metadata
  name: COVID Deaths by Age (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5eb30f62d4c4600016078aad/representationdetails/5ed10dcbfcaa5a001553c1d4?ref=ref%3Dview_280_search%253Dcovid%252520deaths%2526view_280_page%253D1
schema: philadelphia
source: ''
tags:
- COVID-19
- Coronavirus
- Philadelphia Department of Public Health
time_period: null
title: COVID Deaths
usage: null
---
