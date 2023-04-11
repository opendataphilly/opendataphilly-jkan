---
area_of_interest: null
category:
- Economy
- Planning / Zoning
- Public Safety
- Real Estate / Land Records
created: '2017-11-02T18:34:24.957412'
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Inventory of building demolitions occurring within the City of Philadelphia.\
  \ This includes both demolitions performed by private owners/contractors and by\
  \ the Department of Licenses and Inspections due to dangerous building conditions.\
  \ \r\n\r\nUpdated daily. \r\n\r\nTrouble downloading or have questions about this\
  \ City dataset? Visit the [OpenDataPhilly Discussion Group](http://www.phila.gov/data/discuss/)"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: Demolitions (Visualization)
  url: https://data.phila.gov/visualizations/li-demolitions/
- description: ''
  format: CSV
  name: L&I Demolitions (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+demolitions&filename=demolitions&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Demolitions (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+demolitions&filename=demolitions&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Demolitions (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+demolitions&filename=demolitions&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Demolitions (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#demolitions
- description: ''
  format: HTML
  name: L&I Demolitions (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/58dbd271fe779d33cf0e8cad/representationdetails/5e989bd68d478300195737b0/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
time_period: null
title: Building Demolitions
usage: null
---
