---
category: []
extras: {}
license: Other (City of Philadelphia)
maintainer: Captain Mark Overwise
maintainer_email: mark.overwise@phila.gov
notes: "This data set shows all fatal crashes and their investigative outcomes from\
  \ PPD's Accident Investigation Unit (AID) from 1/1/19 to the present. The whole\
  \ dataset gets refreshed nightly. This means the dataset will show new records the\
  \ day after the source data has updated.\r\n\r\n__For those conducting analysis,\
  \ this dataset by PPD and [OTIS' crash data](https://www.opendataphilly.org/dataset/vehicular-crash-data)\
  \ should not be compared, or should be used together cautiously.__ The same crash\
  \ may show as in different locations between the two datasets since PPD data represent\
  \ the location of where crashes are initially _reported_ whereas OTIS' crash data\
  \ involves further investigation to confirm initial reports. If you want to analyze\
  \ the location of crashes in Philadelphia, use OTIS' dataset. If you want to understand\
  \ the investigative outcomes of crashes, use the PPD dataset.\r\n\r\nTrouble downloading\
  \ or have questions about this City dataset? Visit the [OpenDataPhilly Discussion\
  \ Group](http://www.phila.gov/data/discuss/)"
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Fatal Crashes (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=fatal_crashes&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM fatal_crashes
- description: ''
  format: SHP
  name: Fatal Crashes (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=fatal_crashes&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM fatal_crashes
- description: ''
  format: GeoJSON
  name: Fatal Crashes (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?filename=fatal_crashes&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+fatal_crashes
- description: ''
  format: API
  name: Fatal Crashes (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#fatal_crashes&_ga=2.159128115.869140587.1676312538-1066601619.1667858192
- description: ''
  format: HTML
  name: Fatal Crashes (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5d89169eb5d0de0010bf1ed1/representationdetails/5d89169fb5d0de0010bf1ed5/
schema: default
tags:
- Philadelphia Police Department
title: Fatal Crashes
---
