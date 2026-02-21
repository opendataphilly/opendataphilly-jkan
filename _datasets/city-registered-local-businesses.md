---
area_of_interest: null
category:
- Budget / Finance
- Economy
license: City of Philadelphia License
maintainer: ''
maintainer_email: 'lbecertification@phila.gov'
maintainer_link: null
maintainer_phone: null
notes: "The City of Philadelphia gives preference to certified local businesses through\
  \ its Local Business Entity program. This dataset provides a list of currently certified\
  \ local businesses registered with the City of Philadelphia.\r\n\r\nFor more information,\
  \ visit:\r\nhttps://www.phila.gov/departments/procurement-department/local-preference/"
modified: null
organization: City of Philadelphia
resources:
- description: ''
  format: App
  name: Search local business entities app (HTML)
  url: https://www.phila.gov/departments/procurement-department/local-preference/local-business-entity-listing/
- description: ''
  format: CSV
  name: City-Registered Local Businesses (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=registered_local_businesses&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * FROM registered_local_businesses ORDER BY business_name ASC
- description: ''
  format: API
  name: City-Registered Local Businesses (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#registered_local_businesses
    ORDER BY business_name ASC
- description: ''
  format: HTML
  name: City-Registered Local Businesses (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/609bdbbeb73ca4001bcbf275/representationdetails/609bdbbfb73ca4001bcbf279/
schema: philadelphia
source: ''
tags:
- Department of Procurement
- business
- businesses
- contracting
- contracts
time_period: null
title: City-Registered Local Businesses
usage: null
---
