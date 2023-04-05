---
category: []
extras: {}
license: Other (City of Philadelphia)
maintainer: ligisteam@phila.gov
maintainer_email: LIGISTEAM@phila.gov
notes: "All investigations completed on a property with property maintenance violations\
  \ by an inspector of the Department of Licenses & Inspections.\r\n\r\n**Please note\
  \ that this is a very large dataset. To see all investigations, download all datasets\
  \ for all years.** \r\n\r\n**If you are comfortable with APIs, you can also use\
  \ the API links to access this data. You can learn more about how to use the API\
  \ at Carto\u2019s SQL API site and in the Carto guide in the section on making calls\
  \ to the API.**"
organization: City of Philadelphia
resources:
- description: ''
  format: Visualization
  name: L&I Inspections (Visualization)
  url: https://data.phila.gov/visualizations/li-inspections
- description: ''
  format: CSV
  name: L&I Case investigations - 2019 to present (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted >= '2019-01-01'
- description: ''
  format: CSV
  name: L&I Case investigations - 2016 to 2018 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted >= '2016-01-01' AND investigationcompleted < '2019-01-01'
- description: ''
  format: CSV
  name: L&I Case investigations - 2013 to 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted >= '2013-01-01' AND investigationcompleted < '2016-01-01'
- description: ''
  format: CSV
  name: L&I Case investigations - 2010 to 2012 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted >= '2010-01-01' AND investigationcompleted < '2013-01-01'
- description: ''
  format: CSV
  name: L&I Case investigations - 2007 to 2009 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted >= '2007-01-01' AND investigationcompleted < '2010-01-01'
- description: ''
  format: CSV
  name: L&I Case investigations - before 2007 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM case_investigations WHERE
    investigationcompleted < '2007-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - 2019 to present (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted >= '2019-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - 2016 to 2018 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted >= '2016-01-01' AND investigationcompleted
    < '2019-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - 2013 to 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted >= '2013-01-01' AND investigationcompleted
    < '2016-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - 2010 to 2012 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted >= '2010-01-01' AND investigationcompleted
    < '2013-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - 2007 to 2009 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted >= '2007-01-01' AND investigationcompleted
    < '2010-01-01'
- description: ''
  format: SHP
  name: L&I Case investigations - before 2007 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=case_investigations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM case_investigations WHERE investigationcompleted < '2007-01-01'
- description: ''
  format: API
  name: L&I Case investigations (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#case_investigations
- description: ''
  format: HTML
  name: 'L&I Case investigations (Metadata) '
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca785c4ae4cd66d3ff80/representationdetails/5e986970b2c39b001522fb9d/
schema: default
tags:
- Department of Licenses and Inspections
- Visualization
title: 'Licenses and Inspections: Case Investigations'
---
