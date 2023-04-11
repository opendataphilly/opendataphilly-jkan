---
area_of_interest: null
category:
- Environment
- Health / Human Services
- Parks / Recreation
created: '2019-06-18T15:51:31.276548'
license: Other (City of Philadelphia)
maintainer: Chris Park
maintainer_email: chris.park@phila.gov
maintainer_link: null
maintainer_phone: null
notes: Displays the locations of adult exercise equipment located within or are maintained
  by Philadelphia Parks and Recreation (PPR).
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: PPR Adult Exercise Equipment (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+ppr_adult_exercise_equipment&filename=ppr_adult_exercise_equipment&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: PPR Adult Exercise Equipment (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_adult_exercise_equipment&filename=ppr_adult_exercise_equipment&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: PPR Adult Exercise Equipment (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_adult_exercise_equipment&filename=ppr_adult_exercise_equipment&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: PPR Adult Exercise Equipment (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppr_adult_exercise_equipment
- description: ''
  format: HTML
  name: PPR Adult Exercise Equipment (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5ce2e5bf7be0b90007a9fd88/representationdetails/5ce2e5c07be0b90007a9fda0/
schema: philadelphia
source: ''
tags:
- Philadelphia Parks and Recreation
time_period: null
title: PPR Adult Exercise Equipment
usage: null
---
