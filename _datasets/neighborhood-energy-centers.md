---
area_of_interest: null
category:
- Environment
- Health / Human Services
created: '2019-05-22T17:46:14.482318'
license: Other (City of Philadelphia)
maintainer: Portia Egan
maintainer_email: portia.egan@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "DHCD supports the Energy Coordinating Agency\u2019s (ECA) Neighborhood Energy\
  \ Centers, through which residents can complete applications to seek bill payment\
  \ assistance, learn how to conserve water, gas and electricity, and obtain energy\
  \ counseling."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Neighborhood Energy Centers (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+neighborhood_energy_centers&filename=neighborhood_energy_centers&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Neighborhood Energy Centers (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+neighborhood_energy_centers&filename=neighborhood_energy_centers&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Neighborhood Energy Centers (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+neighborhood_energy_centers&filename=neighborhood_energy_centers&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Neighborhood Energy Centers (API)
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+neighborhood_energy_centers
- description: ''
  format: HTML
  name: Neighborhood Energy Centers (Metadata)
  url: https://metadata.phila.gov/index.html#home/datasetdetails/5cdace7d97ffd6000baedab5/representationdetails/5cdace7f97ffd6000baedab9/
schema: philadelphia
source: ''
tags: []
time_period: null
title: Neighborhood Energy Centers
usage: null
---
