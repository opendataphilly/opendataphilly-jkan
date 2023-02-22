---
category:
- Health / Human Services
- Public Safety
extras: {}
license: Other (City of Philadelphia)
maintainer: Aviva Tevah
maintainer_email: Aviva.Tevah@Phila.gov
notes: "This dataset includes people released to Philadelphia from the Philadelphia\
  \ Department of Prisons (PDP) and the Pennsylvania Department of Correction (PA\
  \ DOC). Individual-level data for releases from Federal (BOP) incarceration was\
  \ not available, and makes up less than 2% of people released to Philadelphia in\
  \ the year analyzed. The dataset also only includes people released to Philadelphia\
  \ who have been charged with a criminal non-summary type offense in the Philadelphia\
  \ adult criminal justice system.\r\n\r\nTrouble downloading or have questions about\
  \ this City dataset? Visit the [OpenDataPhilly Discussion Group](http://www.phila.gov/data/discuss/)"
organization: City of Philadelphia
resources:
- description: 'Update Frequency: Annually'
  format: visualization
  name: 2015 Releases (Visualization)
  url: https://data.phila.gov/visualizations/prison-releases/
- description: 'Update Frequency: Annually'
  format: CSV
  name: 2015 releases (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+pdp_state_releases&filename=pdp_state_releases&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: 'Update Frequency: Annually'
  format: SHP
  name: ' 2015 releases (SHP)'
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+pdp_state_releases&filename=pdp_state_releases&format=shp&skipfields=cartodb_id
- description: 'Update Frequency: Annually'
  format: GeoJSON
  name: 2015 releases (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+pdp_state_releases&filename=pdp_state_releases&format=geojson&skipfields=cartodb_id
- description: 'Update Frequency: Annually'
  format: API
  name: ' 2015 releases (API)'
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#pdp_state_releases
- description: 'Update Frequency: As needed'
  format: HTML
  name: 2015 releases (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5aa2d3a0fa1ccb42fc2b00df/representationdetails/5aa2d3a1fa1ccb42fc2b00e3/
schema: default
tags:
- Office of Criminal Justice
title: People Released to Philadelphia from Prison & Jail
---
