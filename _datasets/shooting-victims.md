---
category:
- Public Safety
extras:
  department: Police Department
license: Other (City of Philadelphia)
maintainer: publicsafetygis@phila.gov
maintainer_email: publicsafetygis@phila.gov
notes: "City-wide shooting victims, including Police Officer-involved shootings\r\n\
  \r\nTrouble downloading or have questions about this City dataset? Visit the [OpenDataPhilly\
  \ Discussion Group](http://www.phila.gov/data/discuss/)"
organization: City of Philadelphia
resources:
- description: Guided tour of the data, contextualized with other datasets
  format: Visualization
  name: Shooting Victims (Map Journal)
  url: http://philadelphia.maps.arcgis.com/apps/MapJournal/index.html?appid=d498be2dde18426193679f5e9ce0e6e5
- description: ''
  format: Visualization
  name: Shooting Victims (Visualization)
  url: https://data.phila.gov/visualizations/shooting-victims
- description: ''
  format: CSV
  name: Shooting Victims (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+shootings&filename=shootings&format=csv&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Shooting Victims (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+shootings&filename=shootings&format=geojson&skipfields=cartodb_id
- description: ''
  format: SHP
  name: Shooting Victims (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+shootings&filename=shootings&format=shp&skipfields=cartodb_id
- description: ''
  format: API Documentation
  name: Shooting Victims (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#shootings
- description: ''
  format: HTML
  name: Shooting Victims (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5719551277d6389f3005a610/representationdetails/5719551277d6389f3005a614/
schema: default
tags:
- Philadelphia Police Department
title: Shooting Victims
---
