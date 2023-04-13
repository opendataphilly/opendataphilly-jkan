---
area_of_interest: null
category: []
created: '2016-09-22T14:31:12.542396'
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Complaints that were entered via 311 or by an individual in the department.\
  \ Complaints were formerly known as 'Service Requests' in L&I's old enterprise database\
  \ called 'Hansen', which was decommissioned in March 2020.\r\n\r\nEach row in the\
  \ table represents a single 'call'. Calls are sometimes bunched into one 'Complaint'\
  \ all sharing the same unique number.\r\n\r\n\r\
  \n"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: Visualization
  name: L&I Complaints (Visualization)
  url: https://data.phila.gov/visualizations/li-complaints
- description: ''
  format: CSV
  name: L&I Complaints (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+complaints&filename=complaints&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Complaints (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+complaints&filename=complaints&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Complaints (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+complaints&filename=complaints&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Complaints (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#complaints
- description: ''
  format: HTML
  name: L&I Complaints (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca6d5c4ae4cd66d3ff52/representationdetails/5e5d50e0fbc9650019b56025/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
- Visualization
time_period: null
title: Licenses and Inspections Complaints
usage: null
---
