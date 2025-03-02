---
area_of_interest: null
category:
- Environment
created: '2015-01-16T16:50:27.315346'
license: City of Philadelphia License
maintainer: ''
maintainer_email: ''
maintainer_link: null
maintainer_phone: null
notes: "Count of residents participating in the RecycleBank program by street segment."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: RecycleBank Participation (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+properties_not_reported_2015&filename=properties_not_reported_2015&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: RecycleBank Participation (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+recyclebank_participation&filename=recyclebank_participation&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: RecycleBank Participation (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+recyclebank_participation&filename=recyclebank_participation&format=geojson&skipfields=cartodb_id
- description: ''
  format: HTML
  name: RecycleBank Participation (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#recyclebank_participation
- description: ''
  format: HTML
  name: RecycleBank Participation (Metadata)
  url: http://cityofphiladelphia.github.io/metadata-catalog/#home/datasetdetails/5543866d20583086178c4f1b/representationdetails/55438ab39b989a05172d0d52/
schema: philadelphia
source: ''
tags:
- Streets Department
time_period: null
title: RecycleBank Participation
usage: null
---
