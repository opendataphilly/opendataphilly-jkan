---
area_of_interest: null
category:
- Economy
- Health / Human Services
created: '2021-02-03T14:44:35.061685'
license: Other (City of Philadelphia)
maintainer: PublicHealthInfo@phila.gov
maintainer_email: PublicHealthInfo@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "***As of May 2022, these datasets moved from daily updates to weekly updates\
  \ every Monday.***\r\n\r\nShows distribution counts of first and second dose, as\
  \ well as total dose information for all vaccinations performed by the health department.\
  \ Also provides vaccinations by census tract, ZIP code, date, age, race, and sex.\
  \ Vaccinations include residents and non-residents of Philadelphia. Updates daily."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Total COVID Vaccinations (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccine_totals&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccine_totals
- description: ''
  format: API
  name: Total COVID Vaccinations (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccine_totals
- description: ''
  format: HTML
  name: Total COVID Vaccinations (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/601abebaf910a2001ce794e6/
- description: ''
  format: CSV
  name: 'COVID Vaccinations by Census Tract (CSV) '
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_census_tract&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_census_tract
- description: ''
  format: SHP
  name: 'COVID Vaccinations by Census Tract (SHP) '
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_census_tract&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM covid_vaccines_by_census_tract
- description: ''
  format: GeoJSON
  name: 'COVID Vaccinations by Census Tract (GeoJSON) '
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_census_tract&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+covid_vaccines_by_census_tract
- description: ''
  format: API
  name: 'COVID Vaccinations by Census Tract (API) '
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_census_tract
- description: ''
  format: HTML
  name: COVID Vaccinations by Census Tract (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/60b93022a59bf60021d2a63a/
- description: ''
  format: CSV
  name: COVID Vaccinations by ZIP (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_zip&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_zip
- description: ''
  format: ''
  name: COVID Vaccinations by ZIP (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_zip&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM covid_vaccines_by_zip
- description: ''
  format: GeoJSON
  name: COVID Vaccinations by ZIP (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_zip&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+covid_vaccines_by_zip
- description: ''
  format: ''
  name: COVID Vaccinations by ZIP (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_zip
- description: ''
  format: HTML
  name: COVID Vaccinations by ZIP (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/604bc9df25f75f001bf4c03d/
- description: ''
  format: CSV
  name: COVID Vaccinations by Date (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_date&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_date
- description: ''
  format: API
  name: COVID Vaccinations by Date (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_date
- description: ''
  format: HTML
  name: COVID Vaccinations by Date (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/620e6ec35a07ee001ede79b2/
- description: ''
  format: CSV
  name: COVID Vaccinations by ZIP and Date (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_date&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_zip_date
- description: ''
  format: API
  name: COVID Vaccinations by ZIP and Date (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_zip_date
- description: ''
  format: HTML
  name: COVID Vaccinations by ZIP and Date (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/620e6bfdcfada4001e5cce43/
- description: ''
  format: CSV
  name: COVID Vaccinations by Race (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_race&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_race
- description: ''
  format: API
  name: COVID Vaccinations by Race (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_race
- description: ''
  format: HTML
  name: COVID Vaccinations by Race (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/604bcba25b321d001b5a6a6b/
- description: ''
  format: CSV
  name: COVID Vaccinations by Age (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_age&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_age
- description: ''
  format: API
  name: COVID Vaccinations by Age (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_age
- description: ''
  format: HTML
  name: COVID Vaccinations by Age (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/604bca9194d0cd001e9b8676/
- description: ''
  format: CSV
  name: COVID Vaccinations by Sex (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_vaccines_by_sex&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_vaccines_by_sex
- description: ''
  format: API
  name: COVID Vaccinations by Sex (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_vaccines_by_sex
- description: ''
  format: HTML
  name: COVID Vaccinations by Sex (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/604fb6ffc2a893001c2ca8c9/
schema: philadelphia
source: ''
tags:
- COVID-19
- Philadelphia Department of Public Health
- Vaccine
- equity
time_period: null
title: COVID-19 Vaccinations
usage: null
---
