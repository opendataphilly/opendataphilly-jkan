---
area_of_interest: null
category:
- Planning / Zoning
- Public Safety
- Real Estate / Land Records
created: '2016-09-22T14:01:30.276425'
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "The Department of Licenses and Inspections accepts applications for appeals\
  \ of various violations, refusals, revocations, and denials to the following Boards:\r\
  \n*Board of Building Standards \r\n*Licenses and Inspections (L&I) Review Board\r\
  \n*Zoning Board of Adjustments \r\n\r\nFor more information, please visit http://www.phila.gov/li/Pages/Appeals.aspx\r\
  \n\r\nThe Court Appeals datasets provides details about Appeals that went to court\
  \ and what the status/results of the court proceedings are. Some Appeal numbers\
  \ could have multiple appeal types, so those are provided as a dataset below as\
  \ well. \r\n\r\nThe Board Decisions datasets shows the decisions made by the Appeal\
  \ Boards (LIRB, ZBA, BBS).\r\n\r\nTrouble downloading or have questions about this\
  \ City dataset? Visit the [OpenDataPhilly Discussion Group](http://www.phila.gov/data/discuss/)"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: 'L&I Appeals (CSV) '
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+appeals&filename=appeals&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: 'L&I Appeals (SHP) '
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+appeals&filename=appeals&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: 'L&I Appeals (GeoJSON) '
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+appeals&filename=appeals&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: 'L&I Appeals (API) '
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#appeals
- description: ''
  format: HTML
  name: 'L&I Appeals (Metadata) '
  url: https://metadata.phila.gov/#home/datasetdetails/5543864d20583086178c4e9c/representationdetails/5e9751361ed3930016d62645/
- description: ''
  format: CSV
  name: L&I Court Appeals (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+court_appeals&filename=court_appeals&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Court Appeals (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+court_appeals&filename=court_appeals&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Court Appeals (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+court_appeals&filename=court_appeals&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Court Appeals (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#court_appeals
- description: ''
  format: HTML
  name: L&I Court Appeals (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5982021bae62375051e8e369/representationdetails/5e98979c1c7151001706ef09/
- description: ''
  format: CSV
  name: L&I Board Decisions (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+board_decisions&filename=board_decisions&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Board Decisions (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+board_decisions&filename=board_decisions&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Board Decisions (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+board_decisions&filename=board_decisions&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Board Decisions (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#board_decisions L&I
    Board Decisions (Metadata)
- description: ''
  format: HTML
  name: L&I Board Decisions (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5981e6ae90e53c5054148db1/representationdetails/5e9864449452850017b87407/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
time_period: null
title: Licenses and Inspections Appeals of Code Violations and Permit Refusals
usage: null
---
