---
category:
- Health / Human Services
- Public Safety
extras: {}
license: Other (City of Philadelphia)
maintainer: ''
maintainer_email: ''
notes: "As part of the Philadelphia Police Department's (PPD) accountability processes,\
  \ PPD publishes three datasets: The Complaints Against Police (CAP) dataset documents\
  \ the civilian complaints alleging police misconduct; the CAP Findings dataset provides\
  \ demographic details of the police officer involved, the allegations, and the status\
  \ of the PPD's Internal Affairs Division's investigation of and findings (if available)\
  \ about the allegation; and the Complainant Demographics dataset shows the race,\
  \ sex, and age of each person who filed a complaint against a police officer by\
  \ complaint number. \r\n\r\nSee metadata links below for dataset and field descriptions.\r\
  \n\r\nIncludes data from the past five years. Updated monthly. "
organization: City of Philadelphia
resources:
- description: 'Updated monthly. '
  format: CSV
  name: Complaints Against Police (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complaints&filename=ppd_complaints&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: 'Updated monthly. '
  format: API
  name: Complaints Against Police (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppd_complaints
- description: ''
  format: HTML
  name: Complaints Against Police (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5a3827b4b9464c55711a0816/representationdetails/5a3827dbb954635579423e0f/
- description: 'Updated monthly. '
  format: CSV
  name: CAP Findings (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complaint_disciplines&filename=ppd_complaint_disciplines&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: 'Updated monthly. '
  format: API
  name: CAP Findings (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppd_complaint_disciplines
- description: ''
  format: HTML
  name: CAP Findings (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5a3827b4b9464c55711a0816/representationdetails/5a3827b6b9464c55711a081a/
- description: Updated monthly.
  format: CSV
  name: Complainant Demographics (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complainant_demographics&filename=ppd_complainant_demographics&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: Updated monthly.
  format: API
  name: Complainant Demographics (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppd_complainant_demographics
- description: ''
  format: HTML
  name: Complainant Demographics (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5a3827b4b9464c55711a0816/representationdetails/5da768d5e1847000154b928a/
- description: Updated monthly.
  format: CSV
  name: CAP History (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=ppd_complaints_history&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20ppd_complaints_history
- description: Updated monthly.
  format: API
  name: CAP History (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#ppd_complaints_history
- description: ''
  format: HTML
  name: CAP History (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5a3827b4b9464c55711a0816/representationdetails/63c86b4ebe68e70012069642/
schema: default
tags:
- Philadelphia Police Department
title: Complaints Against Police
---
