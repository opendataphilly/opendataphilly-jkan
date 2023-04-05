---
category:
- Environment
- Real Estate / Land Records
extras:
  Department: Streets Department
  Department Phone: 215-686-5560
license: Other (City of Philadelphia)
maintainer: Dominick Cassise
maintainer_email: dominick.cassise@phila.gov
notes: "A code violation notice is issued from the Street's department when a person\
  \ has violated one or more codes in the City of Philadelphia or violated one or\
  \ more Streets Department rules and regulations. A code violation notice (CVN) is\
  \ a penalty punishable by a fine up to $300.00.\r\n\r\nAddresses have been generalized\
  \ to the hundred-block level (ie. 1234 Market Street becomes 1200 block of Market\
  \ Street). Please note that the CVN dataset does not include all CVNs. Some are\
  \ issued as paper tickets. As of 2018, a reporting system upgrade is underway. Once\
  \ complete, the City plans to update this information to include all CVNs.\r\n\r\
  \n**Please note that this is a very large dataset. To see all CVNs, download all\
  \ datasets for all years.** \r\n\r\n**If you are comfortable with APIs, you can\
  \ also use the API links to access this data. You can learn more about how to use\
  \ the API at Carto\u2019s SQL API site and in the Carto guide in the section on\
  \ making calls to the API.**"
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Code Violation Notices from 2020 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2020-01-01' AND date_added < '2021-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2019 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2019-01-01' AND date_added < '2020-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2018 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2018-01-01' AND date_added < '2019-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2017 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2017-01-01' AND date_added < '2018-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2016 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2016-01-01' AND date_added < '2017-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2015-01-01' AND date_added < '2016-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2014 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2014-01-01' AND date_added < '2015-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2013 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2013-01-01' AND date_added < '2014-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2012 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2012-01-01' AND date_added < '2013-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2011 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2011-01-01' AND date_added < '2012-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2010 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2010-01-01' AND date_added < '2011-01-01'
- description: ''
  format: CSV
  name: Code Violation Notices from 2009 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM streets_code_violation_notices
    WHERE date_added >= '2009-01-01' AND date_added < '2010-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2020 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2020-01-01' AND date_added
    < '2021-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2019 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2019-01-01' AND date_added
    < '2020-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2018 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2018-01-01' AND date_added
    < '2019-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2017 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2017-01-01' AND date_added
    < '2018-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2016 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2016-01-01' AND date_added
    < '2017-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2015-01-01' AND date_added
    < '2016-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2014 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2014-01-01' AND date_added
    < '2015-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2013 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2013-01-01' AND date_added
    < '2014-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2012 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2012-01-01' AND date_added
    < '2013-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2011 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2011-01-01' AND date_added
    < '2012-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2010 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2010-01-01' AND date_added
    < '2011-01-01'
- description: ''
  format: SHP
  name: Code Violation Notices from 2009 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=streets_code_violation_notices&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM streets_code_violation_notices WHERE date_added >= '2009-01-01' AND date_added
    < '2010-01-01'
- description: ''
  format: API Documentation
  name: Code Violation Notices - Full Dataset (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#streets_code_violation_notices
- description: ''
  format: HTML
  name: Code Violation Notices Metadata
  url: http://metadata.phila.gov/#home/datasetdetails/5543865120583086178c4ead/
schema: default
tags:
- Streets Department
title: Street's Code Violation Notices
---
