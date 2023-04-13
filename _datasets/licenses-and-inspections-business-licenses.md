---
area_of_interest: null
category:
- Economy
- Planning / Zoning
- Real Estate / Land Records
created: '2016-09-22T21:14:38.869844'
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Information regarding applications for licenses required by the City to conduct\
  \ certain business activities. Licenses are required for individuals and businesses\
  \ to engage in select commercial activities. For example, vendors and restaurants\
  \ require a license in order to sell goods and food and trades-people, such as plumbers\
  \ and contractors, require a license in order to practice their trade.\r\n\r\nInformation\
  \ includes license application type, applicant, property for which the license would\
  \ be issued, application date, issue date, and expiration date. Data is accurate;\
  \ however, it may be misinterpreted by an unfamiliar user.\r\n\r\n"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: Business Licenses (Visualization)
  url: https://data.phila.gov/visualizations/li-business-licenses
- description: ''
  format: CSV
  name: L&I Business Licenses (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+business_licenses&filename=business_licenses&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Business Licenses (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+business_licenses&filename=business_licenses&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Business Licenses (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+business_licenses&filename=business_licenses&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Business Licenses (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#business_licenses
- description: ''
  format: HTML
  name: L&I Business Licenses (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543865a20583086178c4ed2/representationdetails/5e985a5e344ed50018936bb8/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
- Visualization
time_period: null
title: Licenses and Inspections Business Licenses
usage: null
---
