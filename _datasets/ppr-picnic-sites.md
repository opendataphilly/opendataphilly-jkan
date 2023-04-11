---
area_of_interest: null
category:
- Environment
- Health / Human Services
- Parks / Recreation
created: '2019-06-18T15:26:54.259554'
license: Other (City of Philadelphia)
maintainer: Chris Park
maintainer_email: chris.park@phila.gov
maintainer_link: null
maintainer_phone: null
notes: Displays the locations of picnic sites located within Philadelphia Parks and
  Recreation boundaries. Picnic sites are denoted as any location with a picnic table.
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Picnic Sites (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+ppr_picnic_sites&filename=ppr_picnic_sites&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Picnic Sites (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_picnic_sites&filename=ppr_picnic_sites&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Picnic Sites (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_picnic_sites&filename=ppr_picnic_sites&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Picnic Sites (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppr_picnic_sites
- description: ''
  format: HTML
  name: Picnic Sites (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5ce320f835d1480006084e0a/representationdetails/5ce320f835d1480006084e0e/
schema: philadelphia
source: ''
tags:
- Philadelphia Parks and Recreation
time_period: null
title: PPR Picnic Sites
usage: null
---
