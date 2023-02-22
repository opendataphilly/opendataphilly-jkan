---
category:
- Environment
- Health / Human Services
- Parks / Recreation
extras: {}
license: Other (City of Philadelphia)
maintainer: Chris Park
maintainer_email: chris.park@phila.gov
notes: "2018 data: This dataset was developed as part of an Urban Tree Canopy (UTC)\
  \ assessment for Philadelphia,Pennsylvania. It shows how tree canopy changed during\
  \ the period 2008-2018, highlighting trees that were gained or lost during the 10-year\
  \ period. It is intended for use in monitoring patterns of change in Philadelphia,Pennsylvania\
  \ tree canopy.\r\n\r\n2015 data: Collection of tree canopy outlines and points generated\
  \ by Intergraph Government Solutions (IGS) for trees >6' diameter. Update generated\
  \ off the 2015 Leaf-Off 3\" AccuPLUS Imagery representing changes in tree canopy\
  \ visible within the imagery. Heights have been derived separately for each tree\
  \ canopy outline from 2015 LiDAR data capture."
organization: City of Philadelphia
resources:
- description: ''
  format: visualization
  name: PPR 2015 Tree Canopy Outlines (Visualization)
  url: https://cityofphiladelphia.carto.com/u/phl/builder/0869b21d-4b57-4910-9bb4-46a0509d6f14/embed
- description: ''
  format: CSV
  name: 2008 - 2018 Tree Canopy Change (CSV)
  url: https://opendata.arcgis.com/datasets/de383e47c72045cbbd9af780d1117ff3_0.csv
- description: ''
  format: SHP
  name: 2008 - 2018 Tree Canopy Change (SHP)
  url: https://opendata.arcgis.com/datasets/de383e47c72045cbbd9af780d1117ff3_0.zip
- description: ''
  format: GeoJSON
  name: 2008 - 2018 Tree Canopy Change (GeoJSON)
  url: https://opendata.arcgis.com/datasets/de383e47c72045cbbd9af780d1117ff3_0.geojson
- description: ''
  format: GDB
  name: 2008 - 2018 Tree Canopy Change (FGDB)
  url: https://opendata.arcgis.com/datasets/de383e47c72045cbbd9af780d1117ff3_0.gdb
- description: ''
  format: API
  name: 2008 - 2018 Tree Canopy Change (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/TreeCanopyChange_2008_2018/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: 2008 - 2018 Tree Canopy Change (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5dd7098722804b0016de910e/representationdetails/5dd7098822804b0016de9112/
- description: ''
  format: CSV
  name: PPR 2015 Tree Canopy Outlines (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+ppr_tree_canopy_outlines_2015&filename=ppr_tree_canopy_outlines_2015&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: PPR 2015 Tree Canopy Outlines (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tree_canopy_outlines_2015&filename=ppr_tree_canopy_outlines_2015&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: PPR 2015 Tree Canopy Outlines (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tree_canopy_outlines_2015&filename=ppr_tree_canopy_outlines_2015&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: PPR 2015 Tree Canopy Outlines (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppr_tree_canopy_outlines_2015
- description: ''
  format: HTML
  name: PPR 2015 Tree Canopy Outlines (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5c49d8cb63a2aa28893742e6/representationdetails/5c49d8cc63a2aa28893742eb/
- description: ''
  format: CSV
  name: PPR 2015 Tree Canopy Points (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+ppr_tree_canopy_points_2015&filename=ppr_tree_canopy_points_2015&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: PPR 2015 Tree Canopy Points (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tree_canopy_points_2015&filename=ppr_tree_canopy_points_2015&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: PPR 2015 Tree Canopy Points (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppr_tree_canopy_points_2015&filename=ppr_tree_canopy_points_2015&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: PPR 2015 Tree Canopy Points (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppr_tree_canopy_points_2015
- description: ''
  format: HTML
  name: PPR 2015 Tree Canopy Points (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5c49edcfcf1222529a2e3b32/representationdetails/5c49edcfcf1222529a2e3b36?ref=ref%3Dview_280_search%253Dcanopy%2526view_280_page%253D1
schema: default
tags:
- Philadelphia Parks and Recreation
- canopy
- trees
- urban forest
title: PPR Tree Canopy
---
