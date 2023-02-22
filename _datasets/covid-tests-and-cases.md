---
category:
- Economy
- Health / Human Services
extras: {}
license: Other (City of Philadelphia)
maintainer: PublicHealthInfo@phila.gov
maintainer_email: PublicHealthInfo@phila.gov
notes: "***As of May 2022, these datasets moved from daily updates to weekly updates\
  \ every Monday.***\r\n\r\n**For greatest accuracy, please use the latest dataset\
  \ for all analysis and reporting as opposed to any data you downloaded prior to\
  \ September 29, 2020. All datasets now reflect counts from test collection dates\
  \ instead of the previously displayed result dates. To keep things clear, the field\
  \ name in the COVID Outcome by Date files also changed from 'Result_Date' to 'CollectionDate.'\
  \  These changes will adjust, for example, the count of cases for each day. PDPH\
  \ has also added 376 confirmed COVID-19 cases (positive tests) that were previously\
  \ missing from the data.**\r\n\r\nDeidentified, aggregate datasets showing COVID\
  \ tests by date, zip, and outcome and cases by race, age or sex.  To protect the\
  \ confidentiality of residents, PDPH suppresses the exact data for any categories\
  \ that have less than 6 counts (i.e. of tests or fatalities).\r\n\r\nTrouble downloading\
  \ or have questions about this City dataset? Visit the [OpenDataPhilly Discussion\
  \ Group](http://www.phila.gov/data/discuss/)"
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: COVID Tests by Outcome (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_outcome&filename=covid_cases_by_outcome&format=csv&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Tests by Outcome (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_outcome
- description: ''
  format: Metadata
  name: COVID Tests by Outcome (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5eda5c1bfcec2f0015af6656/
- description: '**For greatest accuracy, please use the latest dataset for all analysis
    and reporting as opposed to any data you downloaded prior to September 29, 2020.
    All datasets now reflect counts from test collection dates instead of the previously
    displayed result dates. To keep things clear, the field name in the COVID Outcome
    by Date files also changed from ''Result_Date'' to ''CollectionDate.''  These
    changes will adjust, for example, the count of cases for each day. PDPH has also
    added 376 confirmed COVID-19 cases (positive tests) that were previously missing
    from the data.**'
  format: CSV
  name: COVID Tests by Date (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_date&filename=covid_cases_by_date&format=csv&skipfields=cartodb_id
- description: '**For greatest accuracy, please use the latest dataset for all analysis
    and reporting as opposed to any data you downloaded prior to September 29, 2020.
    All datasets now reflect counts from test collection dates instead of the previously
    displayed result dates. To keep things clear, the field name in the COVID Outcome
    by Date files also changed from ''Result_Date'' to ''CollectionDate.''  These
    changes will adjust, for example, the count of cases for each day. PDPH has also
    added 376 confirmed COVID-19 cases (positive tests) that were previously missing
    from the data.**'
  format: API
  name: COVID Tests by Date (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_date
- description: ''
  format: HTML
  name: COVID Tests by Date (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5ea73b68890f920015c190d3/
- description: ''
  format: CSV
  name: COVID Tests by ZIP (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_zip&filename=covid_cases_by_zip&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: COVID Tests by ZIP (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_zip&filename=covid_cases_by_zip&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: COVID Tests by ZIP (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_zip&filename=covid_cases_by_zip&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Tests by ZIP (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_zip
- description: ''
  format: HTML
  name: COVID Tests by ZIP (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5ea73ae520b5b10015e10d10/
- description: ''
  format: CSV
  name: COVID Cases by Age (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_age&filename=covid_cases_by_age&format=csv&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Cases by Age (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_age
- description: ''
  format: HTML
  name: COVID Cases by Age (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5ea725f6890f920015c17afc/
- description: ''
  format: CSV
  name: COVID Cases by Sex (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+covid_cases_by_sex&filename=covid_cases_by_sex&format=csv&skipfields=cartodb_id
- description: ''
  format: API
  name: COVID Cases by Sex (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_sex
- description: ''
  format: HTML
  name: COVID Cases by Sex (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5ea73b819b544f0016339e8b/
- description: 'This dataset shows the total number of people by race that have tested
    positive for COVID. The number that have tested negative by race is not reported
    often enough on negative tests to include in this dataset. '
  format: CSV
  name: COVID Cases by Race (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=covid_cases_by_race&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM covid_cases_by_race
- description: 'This dataset shows the total number of people by race that have tested
    positive for COVID. The number that have tested negative by race is not reported
    often enough on negative tests to include in this dataset. '
  format: API
  name: COVID Cases by Race (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#covid_cases_by_race
- description: ''
  format: Metadata
  name: COVID Cases by Race (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5f0db610b084460016abaf14/
schema: default
tags:
- COVID-19
- Coronavirus
- Philadelphia Department of Public Health
title: COVID Tests and Cases
---
