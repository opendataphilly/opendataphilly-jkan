---
category:
- Elections / Politics
extras:
  Area of Interest: City of Philadelphia
  Department: City Commissioners
  Maintainer Link: "www.philadelphiavotes.com/\u200E"
  Maintainer Phone: 215-557-3600
  Usage: Public Use; Free
license: Other (City of Philadelphia)
maintainer: Seth Bluestein
maintainer_email: seth.bluestein@phila.gov
notes: "The locations of polling places in Philadelphia, along with parking code and\
  \ building accessibility code attribute markers. Data is originally provided by\
  \ the Philadelphia City Commissioners and is continuously updated in correspondence\
  \ with the City Commissioners website, www.philadelphiavotes.com."
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Polling Places (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+polling_places&filename=polling_places&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Polling Places (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+polling_places&filename=polling_places&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Polling Places (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+polling_places&filename=polling_places&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Polling Places (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#polling_places
- description: ''
  format: Metadata
  name: Polling Places (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543867e20583086178c4f68/representationdetails/5571b1bce4fb1d91393c2157/
schema: default
tags:
- City Commissioners
title: Polling Places
---
