---
area_of_interest: null
category: []
created: '2016-09-22T18:07:28.682465'
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Address, date of abatement, and more for properties that have been cleaned\
  \ and sealed by the L&I Clean & Seal Unit.\r\n\r\n\r\
  \n"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: L&I Clean and Seal (Visualization)
  url: https://data.phila.gov/visualizations/li-clean-seal
- description: ''
  format: CSV
  name: L&I Clean and Seal (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+clean_seal&filename=clean_seal&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Clean and Seal (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+clean_seal&filename=clean_seal&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Clean and Seal (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+clean_seal&filename=clean_seal&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Clean and Seal (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#clean_seal
- description: ''
  format: HTML
  name: L&I Clean and Seal (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca725c4ae4cd66d3ff68/representationdetails/5e9875c5e5e4450016073dd3/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
time_period: null
title: Licenses and Inspections Clean and Seal
usage: null
---
