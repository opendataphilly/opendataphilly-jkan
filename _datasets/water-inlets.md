---
category:
- Environment
extras:
  Area of Interest: City of Philadelphia
  Department: Philadelphia Water Department
  Usage: Public Use; Free
license: Other (City of Philadelphia)
maintainer: Larry Szarek
maintainer_email: Larry.Szarek@phila.gov
notes: "This point layer contains all the wastewater and stormwater inlets in Philadelphia\
  \ with latitude and longitude coordinates. \r\n\r\nTrouble downloading or have questions\
  \ about this City dataset? Visit the [OpenDataPhilly Discussion Group](http://www.phila.gov/data/discuss/)"
organization: City of Philadelphia
resources:
- description: ''
  format: Application
  name: Map of Water Inlets (Visualization)
  url: https://cityofphiladelphia.carto.com/u/phl/builder/f6b161cf-b680-4dcd-b1f1-6d6472a2d436/embed
- description: ''
  format: CSV
  name: Water Inlets (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+inlets&filename=inlets&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Water Inlets (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+inlets&filename=inlets&format=shp&skipfields=cartodb_id
- description: ''
  format: JSON
  name: Water Inlets (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+inlets&filename=inlets&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Water Inlets (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#inlets
- description: ''
  format: HTML
  name: Water Inlets (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5543864920583086178c4e87/representationdetails/55438a889b989a05172d0d07/
schema: default
tags:
- Philadelphia Water Department
- visualization
title: Water Inlets
---
