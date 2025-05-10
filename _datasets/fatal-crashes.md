---
area_of_interest: null
category: 
- Transportation
- Health / Human Services
license: City of Philadelphia License
maintainer: Captain Heinzeroth
maintainer_email: robert.heinzeroth@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "This data set shows all fatal crashes and their investigative outcomes from\
  \ PPD's Accident Investigation Unit (AID) from 1/1/19 to the present. The whole\
  \ dataset gets refreshed nightly. This means the dataset will show new records the\
  \ day after the source data has updated.\r\n\r\n__For those conducting analysis,\
  \ this dataset by PPD and [OTIS' crash data](https://opendataphilly.org/datasets/vehicular-crashes/)\
  \ should not be compared, or should be used together cautiously.__ The same crash\
  \ may show as in different locations between the two datasets since PPD data represent\
  \ the location of where crashes are initially _reported_ whereas OTIS' crash data\
  \ involves further investigation to confirm initial reports. If you want to analyze\
  \ the location of crashes in Philadelphia, use OTIS' dataset. If you want to understand\
  \ the investigative outcomes of crashes, use the PPD dataset.\r\n\r\n"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: Vision Zero dashboard on reducing traffic deaths. 
  format: HTML
  name: Reducing Traffic Deaths (Visualization)
  url: https://storymaps.arcgis.com/stories/814b1b2ace6f46f7b7e470504ac08b5e
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
schema: philadelphia
source: ''
tags:
- Philadelphia Police Department
- crashes
- accidents
- Vision Zero
time_period: null
title: Fatal Crashes
usage: null
---
