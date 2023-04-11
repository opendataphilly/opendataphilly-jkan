---
area_of_interest: null
category:
- Public Safety
created: '2016-04-21T22:08:24.449402'
license: Other (City of Philadelphia)
maintainer: publicsafetygis@phila.gov
maintainer_email: publicsafetygis@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Police investigations of pedestrians and vehicles from the Philadelphia Police\
  \ Department. Provides details related to the location of the investigation, type\
  \ of investigation, demographics of the individual investigated, and the actions\
  \ taken.\r\n\r\n**Please note that this is a large dataset and therefore CSV and\
  \ SHP files might give an error when you try to download them. If possible, use\
  \ the API link below, instead of CSV/SHP formats, to access the data. If you can't\
  \ use the API and you have trouble downloading the full CSV or SHP files, we\u2019\
  ve split up the dataset by year. Please be sure to download data for all of the\
  \ years to see the full dataset. You can learn more about how to use the API at\
  \ [Carto\u2019s SQL API site](https://carto.com/developers/sql-api/) and in the\
  \ [Carto guide in the section on making calls to the API](https://carto.com/developers/sql-api/guides/making-calls/).**\r\
  \n\r\nTrouble downloading or have questions about this City dataset? Visit the [OpenDataPhilly\
  \ Discussion Group](http://www.phila.gov/data/discuss/)"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: Guided tour of the data, contextualized with other datasets
  format: Visualization
  name: Vehicle & Pedestrian Inv. (Map Journal)
  url: http://philadelphia.maps.arcgis.com/apps/MapJournal/index.html?appid=d498be2dde18426193679f5e9ce0e6e5
- description: 'Interactive visualization of the data. '
  format: Visualization
  name: Vehicle & Pedestrian Inv. (Visualization)
  url: https://data.phila.gov/visualizations/vehicle-pedestrian-investigations
- description: ''
  format: CSV
  name: 2021 Vehicle & Pedestrian Inv.(CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272021-01-01%27
- description: ''
  format: CSV
  name: 2020 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272020-01-01%27%20AND%20datetimeoccur%20%3C%20%272021-01-01%27
- description: ''
  format: CSV
  name: 2019 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2019-01-01' AND datetimeoccur < '2020-01-01'
- description: ''
  format: CSV
  name: 2018 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2018-01-01' AND datetimeoccur < '2019-01-01'
- description: ''
  format: CSV
  name: 2017 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2017-01-01' AND datetimeoccur < '2018-01-01'
- description: ''
  format: CSV
  name: 2016 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2016-01-01' AND datetimeoccur < '2017-01-01'
- description: ''
  format: CSV
  name: 2015 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2015-01-01' AND datetimeoccur < '2016-01-01'
- description: ''
  format: CSV
  name: 2014 Vehicle & Pedestrian Inv. (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM car_ped_stops WHERE datetimeoccur
    >= '2014-01-01' AND datetimeoccur < '2015-01-01'
- description: ''
  format: SHP
  name: 2021 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT%20*%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272021-01-01%27
- description: ''
  format: SHP
  name: 2020 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2020-01-01'%20AND%20datetimeoccur%20%3C%20%272021-01-01%27
- description: ''
  format: SHP
  name: 2019 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2019-01-01' AND datetimeoccur < '2020-01-01'
- description: ''
  format: SHP
  name: 2018 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2018-01-01' AND datetimeoccur < '2019-01-01'
- description: ''
  format: SHP
  name: 2017 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2017-01-01' AND datetimeoccur < '2018-01-01'
- description: ''
  format: SHP
  name: 2016 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2016-01-01' AND datetimeoccur < '2017-01-01'
- description: ''
  format: SHP
  name: 2015 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2015-01-01' AND datetimeoccur < '2016-01-01'
- description: ''
  format: SHP
  name: 2014 Vehicle & Pedestrian Inv. (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM car_ped_stops WHERE datetimeoccur >= '2014-01-01' AND datetimeoccur < '2015-01-01'
- description: ''
  format: API Documentation
  name: Vehicle & Pedestrian Inv. (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#car_ped_stops
- description: 2014-Present
  format: HTML
  name: Vehicle & Pedestrian Inv. (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/571787614fc865407e3cf2b4/representationdetails/571787614fc865407e3cf2b8/
schema: philadelphia
source: ''
tags:
- Philadelphia Police Department
time_period: null
title: Vehicle & Pedestrian Investigations
usage: null
---
