---
category:
- Environment
- Health / Human Services
extras: {}
license: Other (City of Philadelphia)
maintainer: ''
maintainer_email: ''
notes: "This represents all service and information requests since December 8th, 2014\
  \ submitted to Philly311 via the 311 mobile application, calls, walk-ins, emails,\
  \ the 311 website or social media. \r\n\r\n**Please note that this is a very large\
  \ dataset. Unless you are comfortable working with APIs, we recommend using the\
  \ [visualization](https://data.phila.gov/visualizations/311-requests/) to explore\
  \ the data.**\r\n\r\nIf you are comfortable with APIs, you can also use the API\
  \ links to access this data. You can learn more about how to use the API at [Carto\u2019\
  s SQL API site](https://carto.com/developers/sql-api/)  and in the [Carto guide\
  \ in the section on making calls to the API](https://carto.com/developers/sql-api/guides/making-calls/).**"
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: 311 Requests - Full Dataset (Visualization)
  url: https://data.phila.gov/visualizations/311-requests/
- description: ''
  format: CSV
  name: 311 Requests for 2022 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272022-01-01%27%20AND%20requested_datetime%20%3C%20%272023-01-01%27
- description: ''
  format: CSV
  name: 311 Requests for 2021 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272021-01-01%27%20AND%20requested_datetime%20%3C%20%272022-01-01%27
- description: ''
  format: CSV
  name: 311 Requests for 2020 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2020-01-01' AND requested_datetime
    < '2021-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2019 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2019-01-01' AND requested_datetime
    < '2020-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2018 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2018-01-01' AND requested_datetime
    < '2019-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2017 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2017-01-01' AND requested_datetime
    < '2018-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2016 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2016-01-01' AND requested_datetime
    < '2017-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2015-01-01' AND requested_datetime
    < '2016-01-01'
- description: ''
  format: CSV
  name: 311 Requests for 2014 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2014-01-01' AND requested_datetime
    < '2015-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2020 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2020-01-01' AND requested_datetime
    < '2021-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2019 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2019-01-01' AND requested_datetime
    < '2020-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2018 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2018-01-01' AND requested_datetime
    < '2019-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2017 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2017-01-01' AND requested_datetime
    < '2018-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2016 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2016-01-01' AND requested_datetime
    < '2017-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2015-01-01' AND requested_datetime
    < '2016-01-01'
- description: ''
  format: SHP
  name: 311 Requests for 2014 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM public_cases_fc WHERE requested_datetime >= '2014-01-01' AND requested_datetime
    < '2015-01-01'
- description: ''
  format: API Documentation
  name: 311 Requests - Full Dataset (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#public_cases_fc
- description: ''
  format: HTML
  name: 311 Requests (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5543864d20583086178c4e98/representationdetails/5762e19fa237544b2ecfe722/
schema: default
tags: []
title: 311 Service and Information Requests
---
