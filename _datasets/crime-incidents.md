---
area_of_interest: null
category:
- Public Safety
created: '2016-04-21T22:27:16.878591'
license: Other (City of Philadelphia)
maintainer: publicsafetygis@phila.gov
maintainer_email: publicsafetygis@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Crime incidents from the Philadelphia Police Department. Part I crimes include\
  \ violent offenses such as aggravated assault, rape, arson, among others. Part II\
  \ crimes include simple assault, prostitution, gambling, fraud, and other non-violent\
  \ offenses.\r\n\r\n**Please note that this is a very large dataset. To see all incidents,\
  \ download all datasets for all years.** \r\n\r\n**If you are comfortable with APIs,\
  \ you can also use the API links to access this data. You can learn more about how\
  \ to use the API at Carto\u2019s SQL API site and in the Carto guide in the section\
  \ on making calls to the API.**"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: 'An online appication that displays summary statistics and enables mapping of recent incidents within a radius of an address.'
  format: HTML
  name: Crime Maps and Stats Application
  url: https://www.phillypolice.com/crimestats
- description: ''
  format: HTML
  name: Crime Incidents (Visualization)
  url: https://data.phila.gov/visualizations/crime-incidents
- description: ''
  format: CSV
  name: Crime Incidents from 2024 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272024-01-01%27%20AND%20dispatch_date_time%20%3C%20%272025-01-01%27
- description: ''
  format: CSV
  name: Crime Incidents from 2023 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272023-01-01%27%20AND%20dispatch_date_time%20%3C%20%272024-01-01%27
- description: ''
  format: CSV
  name: Crime Incidents from 2022 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272022-01-01%27%20AND%20dispatch_date_time%20%3C%20%272023-01-01%27
- description: ''
  format: CSV
  name: Crime Incidents from 2021 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272021-01-01%27%20AND%20dispatch_date_time%20%3C%20%272022-01-01%27
- description: ''
  format: CSV
  name: Crime Incidents from 2020 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272020-01-01%27%20AND%20dispatch_date_time%20%3C%20%272021-01-01%27
- description: ''
  format: CSV
  name: Crime Incidents from 2019 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2019-01-01' AND dispatch_date_time < '2020-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2018 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2018-01-01' AND dispatch_date_time < '2019-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2017 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2017-01-01' AND dispatch_date_time < '2018-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2016 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2016-01-01' AND dispatch_date_time < '2017-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2015-01-01' AND dispatch_date_time < '2016-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2014 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2014-01-01' AND dispatch_date_time < '2015-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2013 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2013-01-01' AND dispatch_date_time < '2014-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2012 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2012-01-01' AND dispatch_date_time < '2013-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2011 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2011-01-01' AND dispatch_date_time < '2012-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2010 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2010-01-01' AND dispatch_date_time < '2011-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2009 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2009-01-01' AND dispatch_date_time < '2010-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2008 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2008-01-01' AND dispatch_date_time < '2009-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2007 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2007-01-01' AND dispatch_date_time < '2008-01-01'
- description: ''
  format: CSV
  name: Crime Incidents from 2006 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    * , ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM incidents_part1_part2 WHERE
    dispatch_date_time >= '2006-01-01' AND dispatch_date_time < '2007-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2024 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT%20*%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272024-01-01%27%20AND%20dispatch_date_time%20%3C%20%272025-01-01%27
- description: ''
  format: SHP
  name: Crime Incidents from 2023 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT%20*%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272023-01-01%27%20AND%20dispatch_date_time%20%3C%20%272024-01-01%27
- description: ''
  format: SHP
  name: Crime Incidents from 2022 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT%20*%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272022-01-01%27%20AND%20dispatch_date_time%20%3C%20%272023-01-01%27
- description: ''
  format: SHP
  name: Crime Incidents from 2021 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT%20*%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272021-01-01%27%20AND%20dispatch_date_time%20%3C%20%272022-01-01%27
- description: ''
  format: SHP
  name: Crime Incidents from 2020 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2020-01-01' AND dispatch_date_time
    < '2021-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2019 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2019-01-01' AND dispatch_date_time
    < '2020-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2018 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2018-01-01' AND dispatch_date_time
    < '2019-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2017 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2017-01-01' AND dispatch_date_time
    < '2018-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2016 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2016-01-01' AND dispatch_date_time
    < '2017-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2015-01-01' AND dispatch_date_time
    < '2016-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2014 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2014-01-01' AND dispatch_date_time
    < '2015-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2013 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2013-01-01' AND dispatch_date_time
    < '2014-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2012 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2012-01-01' AND dispatch_date_time
    < '2013-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2011 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2011-01-01' AND dispatch_date_time
    < '2012-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2010 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2010-01-01' AND dispatch_date_time
    < '2011-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2009 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2009-01-01' AND dispatch_date_time
    < '2010-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2008 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2008-01-01' AND dispatch_date_time
    < '2009-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2007 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2007-01-01' AND dispatch_date_time
    < '2008-01-01'
- description: ''
  format: SHP
  name: Crime Incidents from 2006 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM incidents_part1_part2 WHERE dispatch_date_time >= '2006-01-01' AND dispatch_date_time
    < '2007-01-01'
- description: ''
  format: API Documentation
  name: Crime Incidents - Full Dataset (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#incidents_part1_part2
- description: 2006 - Present
  format: HTML
  name: Crime Incidents (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5543868920583086178c4f8e/representationdetails/570e7621c03327dc14f4b68d/
schema: philadelphia
source: ''
tags:
- Philadelphia Police Department
time_period: null
title: Crime Incidents
usage: null
---
