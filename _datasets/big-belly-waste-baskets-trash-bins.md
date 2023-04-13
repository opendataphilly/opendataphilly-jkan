---
area_of_interest: null
category:
- Environment
created: '2015-01-16T17:07:17.251755'
license: Other (City of Philadelphia)
maintainer: Max Steinbrenner
maintainer_email: max.steinbrenner@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Big Belly brand waste baskets maintained/collected by the City of Philadelphia."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: 2015 Big Belly Waste Baskets (Trash Bins) (CSV)
  url: https://data.phila.gov/carto/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+wastebaskets_big_belly&filename=wastebaskets_big_belly&format=csv&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: 2015 Big Belly Waste Baskets (Trash Bins) (GeoJSON)
  url: https://data.phila.gov/carto/api/v2/sql?q=SELECT+*+FROM+wastebaskets_big_belly&filename=wastebaskets_big_belly&format=geojson&skipfields=cartodb_id
- description: ''
  format: SHP
  name: 2015 Big Belly Waste Baskets (Trash Bins) (SHP)
  url: https://data.phila.gov/carto/api/v2/sql?q=SELECT+*+FROM+wastebaskets_big_belly&filename=wastebaskets_big_belly&format=shp&skipfields=cartodb_id
- description: ''
  format: API Documentation
  name: 2015 Big Belly Waste Baskets (Trash Bins) (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#wastebaskets_big_belly
- description: ''
  format: CSV
  name: 2015 Big Belly Waste/Trash Bins (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/f8309c5b19e147cea5cb4d83f3d0d85f_0/downloads/data?format=csv&spatialRefId=4326
- description: ''
  format: SHP
  name: 2015 Big Belly Waste/Trash Bins (SHP)
  url: https://opendata.arcgis.com/api/v3/datasets/f8309c5b19e147cea5cb4d83f3d0d85f_0/downloads/data?format=shp&spatialRefId=4326
- description: ''
  format: GeoJSON
  name: 2015 Big Belly Waste/Trash Bins ( GeoJSON)
  url: https://opendata.arcgis.com/datasets/f8309c5b19e147cea5cb4d83f3d0d85f_0.geojson
- description: ''
  format: api
  name: 2015 Big Belly Waste/Trash Bins (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/WasteBaskets_Big_Belly/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Big Belly Waste/Trash Bins (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/555f8139f15fcb6c6ed4414f/representationdetails/556de53bcf0e0dca19464e91/
schema: philadelphia
source: ''
tags:
- Streets Department
time_period: null
title: Big Belly Waste Baskets (Trash Bins)
usage: null
---
