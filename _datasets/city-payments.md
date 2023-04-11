---
area_of_interest: null
category:
- Budget / Finance
- Economy
- Education
- Elections / Politics
- Environment
- Food
- Health / Human Services
- Parks / Recreation
- Planning / Zoning
- Public Safety
- Real Estate / Land Records
- Transportation
created: '2019-03-13T21:17:04.722160'
license: Other (City of Philadelphia)
maintainer: Catherine Lamb
maintainer_email: catherine.lamb@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "This dataset includes checks and ACH (direct deposit) payments made by the\
  \ City during the fiscal year, which runs from July 1st 2016 through June 31st 2017.\r\
  \n\r\nPlease see [full metadata](http://metadata.phila.gov/#home/datasetdetails/5c4243d6a074de085a899716/)\
  \ to learn more detail about important notes to this data, such as:\r\n\r\n- This\
  \ data cannot be compared with other financial and accounting reports released by\
  \ the City.\r\n- Legal and security-sensitive data has been rolled up to the aggregate\
  \ dataset.\r\n- This dataset does not include [salary](https://www.opendataphilly.org/dataset/employee-salaries-overtime)\
  \ and benefits data or payments the City makes to fund the operations of the First\
  \ Judicial District.\r\n- Vendors should use the [vendor payment website](https://secure.phila.gov/finance/vendorpayments/),\
  \ not this dataset, to track payments."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: A data visualization of the City of Philadelphia's FY2017 payments.
  format: HTML
  name: FY2017 Detailed City Payments (Visualization)
  url: https://data.phila.gov/visualizations/payments
- description: "This dataset includes checks and ACH (direct deposit) payments made\
    \ by the City during the fiscal year, which runs from July 1st 2016 through June\
    \ 3oth 2017. Sensitive data not included: Some payments have been removed from\
    \ this dataset for security, privacy, or other legal confidentiality reasons.\
    \ Please see the city payments aggregates dataset for transaction totals by department,\
    \ character code, sub-object code, and document reference number prefix for all\
    \ payments including those that were removed from the full payments dataset. Please\
    \ note that due to the removed payments, totals from the two datasets will not\
    \ match.\r\n\r\nPlease see metadata for additional considerations."
  format: CSV
  name: FY 2017 Detailed City Payments  (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+city_payments_fy2017&filename=city_payments_fy2017&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: "This dataset includes checks and ACH payments made by the City during\
    \ the fiscal year, which runs from July 1st through June 31st. Sensitive data\
    \ not included: Some payments have been removed from this dataset for security,\
    \ privacy, or other legal confidentiality reasons. Please see the city payments\
    \ aggregates dataset for transaction totals by department, character code, sub-object\
    \ code, and document reference number prefix for all payments including those\
    \ that were removed from the full payments dataset. Please note that due to the\
    \ removed payments, totals from the two datasets will not match.\r\n\r\nPlease\
    \ see metadata for additional considerations."
  format: api
  name: FY 2017 Detailed City Payments (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#city_payments_fy2017
- description: ''
  format: HTML
  name: FY 2017 Detailed City Payments (Metadata)
  url: http://metadata.phila.gov/index.html#home/datasetdetails/5c4243d6a074de085a899716/representationdetails/5c4243d7a074de085a89971a/?view_287_per_page=50&view_287_page=1
- description: A data visualization of the City of Philadelphia's FY2017 aggregate
    payments.
  format: HTML
  name: FY2017 Aggregate City Payments (Visualization)
  url: https://data.phila.gov/visualizations/payments-aggregate
- description: "This dataset includes aggregate information for checks and ACH (direct\
    \ deposit) payments made by the City during the fiscal year, which runs from July\
    \ 1st 2016 through June 30th 2017.\r\n\r\nPlease note: The total transaction amounts\
    \ in this dataset include totals from the detailed city payments dataset as well\
    \ as those that were removed from that dataset due to security, privacy, or other\
    \ legal confidentiality reasons."
  format: CSV
  name: FY 2017 Aggregated City Payments (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+city_payments_aggregates_fy2017&filename=city_payments_aggregates_fy2017&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: "This dataset includes aggregate information for checks and ACH (direct\
    \ deposit) payments made by the City during the fiscal year, which runs from July\
    \ 1st 2016 through June 30th 2017.\r\n\r\nPlease note: The total transaction amounts\
    \ in this dataset include totals from the detailed city payments dataset as well\
    \ as those that were removed from that dataset due to security, privacy, or other\
    \ legal confidentiality reasons."
  format: API
  name: 'FY 2017 Aggregated City Payments (API) '
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#city_payments_aggregates_fy2017
- description: ''
  format: HTML
  name: FY 2017 Aggregated City Payments (Metadata)
  url: http://metadata.phila.gov/index.html#home/datasetdetails/5c4243d6a074de085a899716/representationdetails/5c42446833d76c0858f4cd57/
schema: philadelphia
source: ''
tags:
- expenditures
- payments
- spending
time_period: null
title: City Payments
usage: null
---
