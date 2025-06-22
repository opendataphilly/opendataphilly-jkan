---
area_of_interest: null
category:
- Budget / Finance
- Economy
- Food
- Health / Human Services
created: '2019-10-08T18:23:41.220926'
license: City of Philadelphia License
maintainer: Rebecca Lopez-Kriss
maintainer_email: rebecca.lopezkriss@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "**This data has stopped receiving updates. We're working to reestablish automation\
  \ by the end of 2022.**\r\n\r\nThis dataset provides a list of businesses that have\
  \ registered as sweetened beverage distributors or dealers that file and pay the\
  \ tax. The search application built off of this dataset allows businesses to find\
  \ or confirm that their distributors or dealers are registered. Please note that\
  \ this dataset shows only those Registered Distributors and Registered Dealers who\
  \ consented to share their information publicly and thus this list may not be a\
  \ comprehensive list of all who have registered. \r\n\r\n[Find out more about the\
  \ Philadelphia Beverage Tax here](https://www.phila.gov/services/payments-assistance-taxes/business-taxes/philadelphia-beverage-tax/)."
modified: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: Registered Distributors (Application)
  url: https://www.phila.gov/pbt-registered-distributors/#/
- description: ''
  format: CSV
  name: Registered Distributors (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+beverage_tax_registration_data&filename=beverage_tax_registration_data&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Registered Distributors (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+beverage_tax_registration_data&filename=beverage_tax_registration_data5&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Registered Distributors (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+beverage_tax_registration_data&filename=beverage_tax_registration_data&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Registered Distributors (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#beverage_tax_registration_data
- description: ''
  format: HTML
  name: Registered Distributors (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5d1bb61aa234db0010b16483/representationdetails/5d1bb61ba234db0010b16487/
schema: philadelphia
source: ''
tags:
- Revenue Department
time_period: null
title: Philadelphia Beverage Tax Registered Distributors and Dealers
usage: null
---
