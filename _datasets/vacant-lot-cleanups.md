---
category:
- Real Estate / Land Records
extras:
  Department: Community Life Improvement Program
license: Other (City of Philadelphia)
maintainer: ''
maintainer_email: ''
notes: "Dates and locations of when lots were cleaned (removing weeds, debris, etc.)\
  \ through the City of Philadelphia's Community Life Improvement Program."
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Vacant Lot Cleanups (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+vacant_lot_cleanups&filename=vacant_lot_cleanups&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: Vacant Lot Cleanups (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+vacant_lot_cleanups&filename=vacant_lot_cleanups&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Vacant Lot Cleanups (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+vacant_lot_cleanups&filename=vacant_lot_cleanups&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Vacant Lot Cleanups (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#vacant_lot_cleanups
- description: ''
  format: HTML
  name: Vacant Lot Cleanups (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543866820583086178c4f08/representationdetails/55438aa99b989a05172d0d40/
schema: default
tags:
- Community Life Improvement Program
title: Vacant Lot Cleanups
---
