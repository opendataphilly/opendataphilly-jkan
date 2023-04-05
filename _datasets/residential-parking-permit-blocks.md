---
category:
- Transportation
extras:
  Agency: Philadelphia Parking Authority
license: Other (City of Philadelphia)
maintainer: ''
maintainer_email: ''
notes: 
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Residential Parking Permit Blocks (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+residential_parking_permit_blocks&filename=residential_parking_permit_blocks&format=csv&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Residential Parking Permit Blocks (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+residential_parking_permit_blocks&filename=residential_parking_permit_blocks&format=geojson&skipfields=cartodb_id
- description: ''
  format: SHP
  name: Residential Parking Permit Blocks (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+residential_parking_permit_blocks&filename=residential_parking_permit_blocks&format=shp&skipfields=cartodb_id
- description: ''
  format: API Documentation
  name: Residential Parking Permit Blocks (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#residential_parking_permit_blocks
- description: ''
  format: HTML
  name: Residential Parking Permit Blocks Metadata
  url: http://metadata.phila.gov/#home/datasetdetails/556dfd836c7888b92ed5a367/representationdetails/556dfe215b3f4fa164630a33/
schema: default
tags:
- Philadelphia Parking Authority
title: Residential Parking Permit Blocks
---
