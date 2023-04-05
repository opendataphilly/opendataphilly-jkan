---
category:
- Education
- Health / Human Services
- Public Safety
extras: {}
license: Other (City of Philadelphia)
maintainer: ''
maintainer_email: ''
notes: "This dataset includes the number of newly identified (incident) children with\
  \ blood lead levels (BLL) \u22655 \xB5g/dL, the number of children screened, and\
  \ the percent of children screened with BLLs \u22655 \xB5g/dL. The ZIP code data\
  \ is for 2015 and the census tract data is for 2013-2015.\r\n\r\nCell counts with\
  \ missing values are those with less than six observations, which was truncated\
  \ to ensure confidentiality. Cells with values of zero were included."
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: 2015 by Zip Code (Visualization)
  url: https://cityofphiladelphia.carto.com/u/phl/builder/78752738-f709-4d53-83e5-91049bdcb3b7/embed
- description: ''
  format: CSV
  name: Philadelphia Child Blood Lead Levels By Zip Code (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_zip&filename=child_blood_lead_levels_by_zip&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Philadelphia Child Blood Lead Levels By Zip Code (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_zip&filename=child_blood_lead_levels_by_zip&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Philadelphia Child Blood Lead Levels By Zip Code (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_zip&filename=child_blood_lead_levels_by_zip&format=geojson&skipfields=cartodb_id
- description: ''
  format: api
  name: Philadelphia Child Blood Lead Levels By Zip Code (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#child_blood_lead_levels_by_zip
- description: ''
  format: HTML
  name: 2013-2015 by Census Tract (Visualization)
  url: https://cityofphiladelphia.carto.com/u/phl/builder/48588973-75e1-4912-99c8-168bb1dc7378/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B39.80062349201905%2C-75.6731414794922%5D%2C%22sw%22%3A%5B40.18831582616864%2C-74.68025207519533%5D%2C%22center%22%3A%5B39.99474476071587%2C-75.17669677734376%5D%2C%22zoom%22%3A11%7D%7D
- description: ''
  format: CSV
  name: Philadelphia Child Blood Lead Levels By Census Tract (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_ct&filename=child_blood_lead_levels_by_ct&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Philadelphia Child Blood Lead Levels By Census Tract (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_ct&filename=child_blood_lead_levels_by_ct&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Philadelphia Child Blood Lead Levels By Census Tract (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+child_blood_lead_levels_by_ct&filename=child_blood_lead_levels_by_ct&format=geojson&skipfields=cartodb_id
- description: ''
  format: api
  name: Philadelphia Child Blood Lead Levels By Census Tract (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#child_blood_lead_levels_by_ct
- description: ''
  format: HTML
  name: Philadelphia Child Blood Lead Levels (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/594d26988d68a4593a61bcf0/
schema: default
tags:
- Philadelphia Department of Public Health
title: Philadelphia Child Blood Lead Levels
---
