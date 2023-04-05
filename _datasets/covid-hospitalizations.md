---
category:
- Economy
- Health / Human Services
extras: {}
license: Other (City of Philadelphia)
maintainer: PublicHealthInfo@phila.gov
maintainer_email: PublicHealthInfo@phila.gov
notes: "***As of May 2022, these datasets moved from daily updates to weekly updates\
  \ every Monday.***\r\n\r\nA break down by census categories of the hospitalizations\
  \ to date within the city limits."
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: COVID Hospitalizations by Date (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_hospitalizations_by_date&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_hospitalizations_by_date
- description: ''
  format: API
  name: COVID Hospitalizations by Date (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_hospitalizations_by_date
- description: ''
  format: Metadata
  name: COVID Hospitalizations by Date (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5f0dce6cfdb1f30015f1f3f2/
- description: ''
  format: CSV
  name: COVID Hospitalizations by ZIP (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_hospitalizations_by_zip&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_hospitalizations_by_zip
- description: ''
  format: SHP
  name: COVID Hospitalizations by ZIP (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_hospitalizations_by_zip&filename=covid_hospitalizations_by_zip&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: COVID Hospitalizations by ZIP (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_hospitalizations_by_zip&filename=covid_hospitalizations_by_zip&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Hospitalizations by ZIP (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_hospitalizations_by_zip
- description: ''
  format: Metadata
  name: COVID Hospitalizations by ZIP (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efb6f4a2f3c4c00199b0c84/
- description: ''
  format: CSV
  name: COVID Hospitalizations by Race (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_hospitalizations_by_race&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_hospitalizations_by_race
- description: ''
  format: API
  name: COVID Hospitalizations by Race (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_hospitalizations_by_race
- description: ''
  format: Metadata
  name: COVID Hospitalizations by Race (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efb6a69ccf2e10015ba4010/
- description: ''
  format: CSV
  name: COVID Hospitalizations by Age (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_hospitalizations_by_age&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_hospitalizations_by_age
- description: ''
  format: API
  name: COVID Hospitalizations by Age (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_hospitalizations_by_age
- description: ''
  format: ''
  name: COVID Hospitalizations by Age (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efcee1236f87e001524346a/
- description: ''
  format: CSV
  name: COVID Hospitalizations by Sex (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_hospitalizations_by_sex&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_hospitalizations_by_sex
- description: ''
  format: API
  name: COVID Hospitalizations by Sex (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_hospitalizations_by_sex
- description: ''
  format: Metadata
  name: COVID Hospitalizations by Sex (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efcee5029365900154eb2f6/
schema: default
tags:
- COVID-19
- Philadelphia Department of Public Health
title: COVID Hospitalizations
---
