---
area_of_interest: City of Philadelphia
category:
- Elections / Politics
created: '2014-12-08T22:26:32.294770'
license: Other (City of Philadelphia)
maintainer: Seth Bluestein
maintainer_email: seth.bluestein@phila.gov
maintainer_link: "www.philadelphiavotes.com/\u200E"
maintainer_phone: 215-557-3600
notes: "The locations of polling places in Philadelphia, along with parking code and\
  \ building accessibility code attribute markers. Data is originally provided by\
  \ the Philadelphia City Commissioners and is continuously updated in correspondence\
  \ with the City Commissioners website, www.philadelphiavotes.com."
opendataphilly_rating: null
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
schema: philadelphia
source: ''
tags:
- City Commissioners
time_period: null
title: Polling Places
usage: Public Use; Free
---
