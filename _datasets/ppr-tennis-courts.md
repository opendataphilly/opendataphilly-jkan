---
area_of_interest: null
category:
- Health / Human Services
- Parks / Recreation
created: '2019-06-18T15:06:01.708170'
license: Other (City of Philadelphia)
maintainer: Chris Park
maintainer_email: chris.park@phila.gov
maintainer_link: null
maintainer_phone: null
notes: Displays the locations of tennis courts located within properties maintained
  by Philadelphia Parks and Recreation (PPR).
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Tennis Courts (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+ppr_tennis_courts&filename=ppr_tennis_courts&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Tennis Courts (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tennis_courts&filename=ppr_tennis_courts&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Tennis Courts (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tennis_courts&filename=ppr_tennis_courts&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Tennis Courts (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppr_tennis_courts
- description: ''
  format: HTML
  name: Tennis Courts (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5ce2faa71f71bc045f20aac7/representationdetails/5ce2faa91f71bc045f20aade/
schema: philadelphia
source: ''
tags:
- Philadelphia Parks and Recreation
time_period: null
title: PPR Tennis Courts
usage: null
---
