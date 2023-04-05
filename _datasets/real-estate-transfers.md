---
category:
- Economy
- Planning / Zoning
- Real Estate / Land Records
extras: {}
license: Other (City of Philadelphia)
maintainer: Alex Waldman
maintainer_email: alex.waldman@phila.gov
notes: "The Department of Records (DOR) published data for all documents recorded\
  \ since December 06, 1999, including all real estate transfers in Philadelphia.\
  \ Document type, grantor, and grantee information is presented by address for each\
  \ transaction. More specifically, the real estate transfers data shows the dates\
  \ and location of property sales, deeds, mortgages, and sheriff deeds, and includes\
  \ associated data, such as any realty transfer tax paid.  This table contains both\
  \ raw source data as well as calculated and geocoded/data fields. \r\n\r\n**Please\
  \ note that this is a very large dataset and Excel will *not* load all of the records.\
  \ If you're only comfortable with Excel, please use either the links for individual\
  \ years, or the [data visualization](https://data.phila.gov/visualizations/real-estate-transfers)\
  \ which allows you to filter the dataset by your specific interests (i.e. a zip\
  \ code) and then export a custom CSV from the table at the bottom of the visualization.\
  \ We provide the CSV of All Years mostly for developers to use when coding.\r\n\
  If you are comfortable with APIs, you could also use the API links to access this\
  \ data. You can learn more about how to use the API at [Carto\u2019s SQL API site](https://carto.com/developers/sql-api/)\
  \  and in the [Carto guide in the section on making calls to the API](https://carto.com/developers/sql-api/guides/making-calls/).**"
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: Real Estate Transfers (Visualization)
  url: https://data.phila.gov/visualizations/real-estate-transfers
- description: "Please note that this is a very large dataset and Excel will not load\
    \ all of the records. If you're only comfortable with Excel, please use either\
    \ the links for individual years, or the data visualization which allows you to\
    \ filter the dataset by your specific interests (i.e. a zip code) and then export\
    \ a custom CSV from the table at the bottom of the visualization. We provide the\
    \ CSV of All Years mostly for developers to use when coding. \r\n\r\nIf you are\
    \ comfortable with APIs, you could also use the API links to access this data.\
    \ You can learn more about how to use the API at Carto\u2019s SQL API site and\
    \ in the Carto guide in the section on making calls to the API."
  format: CSV
  name: Real Estate Transfers - All Years (CSV)
  url: https://opendata-downloads.s3.amazonaws.com/rtt_summary.csv
- description: ''
  format: CSV
  name: Real Estate Transfers - 2020 - present (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2020-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2018-2019 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2018-01-01' AND display_date < '2020-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2016-2017 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2016-01-01' AND display_date < '2018-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2014-2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2014-01-01' AND display_date < '2016-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2012-2013 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2012-01-01' AND display_date < '2014-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2010-2011 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2010-01-01' AND display_date < '2012-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2008-2009 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2008-01-01' AND display_date < '2010-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2006-2007 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2006-01-01' AND display_date < '2008-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2004-2005 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2004-01-01' AND display_date < '2006-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2002-2003 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    >= '2002-01-01' AND display_date < '2004-01-01'
- description: ''
  format: CSV
  name: Real Estate Transfers - 2001 and before (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM RTT_SUMMARY WHERE display_date
    < '2002-01-01'
- description: ''
  format: GDB
  name: Real Estate Transfers - All Years (FGDB)
  url: https://opendata-downloads.s3.amazonaws.com/rtt_summary.gdb.zip
- description: ''
  format: SHP
  name: Real Estate Transfers - 2020 - present (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2020-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2018-2019 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2018-01-01' AND display_date < '2020-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2016-2017 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2016-01-01' AND display_date < '2018-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2014-2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2014-01-01' AND display_date < '2016-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2012-2013 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2012-01-01' AND display_date < '2014-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2010-2011 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2010-01-01' AND display_date < '2012-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2008-2009 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2008-01-01' AND display_date < '2010-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2006-2007 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2006-01-01' AND display_date < '2008-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2004-2005 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2004-01-01' AND display_date < '2006-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2002-2003 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date >= '2002-01-01' AND display_date < '2004-01-01'
- description: ''
  format: SHP
  name: Real Estate Transfers - 2001 and before (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=RTT_SUMMARY&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM RTT_SUMMARY WHERE display_date < '2002-01-01'
- description: API Documentation for the Full Dataset
  format: api
  name: Real Estate Transfers (API Documentation)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#RTT_SUMMARY
- description: ''
  format: HTML
  name: Real Estate Transfers (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5a04b8d39202605970a7457d/representationdetails/5a04b8d39202605970a74581/
schema: default
tags:
- Department of Records
- visualization
title: Real Estate Transfers
---
