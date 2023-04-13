---
area_of_interest: null
category:
- Public Safety
- Real Estate / Land Records
created: '2015-05-27T17:25:21.594800'
license: Other (City of Philadelphia)
maintainer: LIGISTEAM@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "Violations issued by the Department of Licenses and Inspections in reference\
  \ to the Philadelphia Building Construction and Occupancy Code.\r\n\r\n**Please\
  \ note that L&I Violations is a very large dataset. To see all violations, download\
  \ all datasets for all years.** \r\n\r\n**If you are comfortable with APIs, you\
  \ can also use the API links to access this data. You can learn more about how to\
  \ use the API at Carto\u2019s SQL API site and in the Carto guide in the section\
  \ on making calls to the API.**\r\
  \n"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: L&I Violations (Visualization)
  url: https://data.phila.gov/visualizations/li-violations
- description: ''
  format: CSV
  name: L&I Violations - 2019 to present (CSV)
  url: https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM violations WHERE violationdate
    >= '2019-01-01'
- description: ''
  format: CSV
  name: L&I Violations - 2016 to 2018 (CSV)
  url: https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM violations WHERE violationdate
    >= '2016-01-01' AND violationdate < '2019-01-01'
- description: ''
  format: CSV
  name: L&I Violations - 2013 to 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM violations WHERE violationdate
    >= '2013-01-01' AND violationdate < '2016-01-01'
- description: ''
  format: CSV
  name: L&I Violations - 2010 to 2012 (CSV)
  url: https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM violations WHERE violationdate
    >= '2010-01-01' AND violationdate < '2013-01-01'
- description: ''
  format: CSV
  name: L&I Violations - 2007 to 2009 (CSV)
  url: https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM violations WHERE violationdate
    >= '2007-01-01' AND violationdate < '2010-01-01'
- description: ''
  format: SHP
  name: L&I Violations - 2019 to present (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=violations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM violations WHERE violationdate >= '2019-01-01'
- description: ''
  format: SHP
  name: L&I Violations - 2016 to 2018 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=violations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM violations WHERE violationdate >= '2016-01-01' AND violationdate < '2019-01-01'
- description: ''
  format: SHP
  name: L&I Violations - 2013 to 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=violations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM violations WHERE violationdate >= '2013-01-01' AND violationdate < '2016-01-01'
- description: ''
  format: SHP
  name: L&I Violations - 2010 to 2012 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=violations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM violations WHERE violationdate >= '2010-01-01' AND violationdate < '2013-01-01'
- description: ''
  format: SHP
  name: L&I Violations - 2007 to 2009 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=violations&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM violations WHERE violationdate >= '2007-01-01' AND violationdate < '2010-01-01'
- description: ''
  format: API
  name: L&I Violations (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#violations
- description: ''
  format: HTML
  name: L&I Violations (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca7a5c4ae4cd66d3ff86/representationdetails/5e99bab227c80700158695b0/
- description: ''
  format: Visualization
  name: L&I Unsafe Buildings (Visualization)
  url: https://data.phila.gov/visualizations/li-unsafe
- description: ''
  format: CSV
  name: L&I Unsafe Buildings (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+unsafe&filename=unsafe&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Unsafe Buildings (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+unsafe&filename=unsafe&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Unsafe Buildings (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+unsafe&filename=unsafe&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Unsafe Buildings (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#unsafe
- description: ''
  format: HTML
  name: L&I Unsafe Buildings (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca7a5c4ae4cd66d3ff86/representationdetails/5e98b247c4d4770015ca69f7/
- description: ''
  format: Visualization
  name: L&I Imminently Dangerous (Visualization)
  url: https://data.phila.gov/visualizations/li-imminently-dangerous
- description: ''
  format: CSV
  name: L&I Imminently Dangerous Buildings (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+imm_dang&filename=imm_dang&format=csv&skipfields=cartodb_id
- description: ''
  format: SHP
  name: L&I Imminently Dangerous Buildings (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+imm_dang&filename=imm_dang&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: L&I Imminently Dangerous Buildings (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+imm_dang&filename=imm_dang&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: L&I Imminently Dangerous Buildings (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#imm_dang
- description: ''
  format: HTML
  name: L&I Imminently Dangerous Buildings (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca7a5c4ae4cd66d3ff86/representationdetails/5e98add33441510015135305/
- description: ''
  format: CSV
  name: L&I Violation Definition (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/d9753daaefcb47cebabbfb9f9f344a91_0/downloads/data?format=csv&spatialRefId=4326
- description: ''
  format: SHP
  name: L&I Violation Definition (SHP)
  url: https://opendata.arcgis.com/api/v3/datasets/d9753daaefcb47cebabbfb9f9f344a91_0/downloads/data?format=shp&spatialRefId=4326
- description: ''
  format: GeoJSON
  name: L&I Violation Definition (GeoJSON)
  url: https://opendata.arcgis.com/datasets/d9753daaefcb47cebabbfb9f9f344a91_0.geojson
- description: ''
  format: API
  name: L&I Violation Definition (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/VIOLATION_DEFINITION/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: L&I Violation Definition (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca7a5c4ae4cd66d3ff86/representationdetails/60f6cc83d3d51d00211c2c5e/
- description: ''
  format: CSV
  name: L&I Contractor Violations (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/dbc8c4b06d3c40aab87d48a5fcdafc58_0/downloads/data?format=csv&spatialRefId=4326
- description: ''
  format: SHP
  name: L&I Contractor Violations (SHP)
  url: https://opendata.arcgis.com/api/v3/datasets/dbc8c4b06d3c40aab87d48a5fcdafc58_0/downloads/data?format=shp&spatialRefId=4326
- description: ''
  format: GeoJSON
  name: L&I Contractor Violations (GeoJSON)
  url: https://opendata.arcgis.com/datasets/dbc8c4b06d3c40aab87d48a5fcdafc58_0.geojson
- description: ''
  format: API
  name: L&I Contractor Violations (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/CONTRACTOR_VIOLATIONS/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: L&I Contractor Violations (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543ca7a5c4ae4cd66d3ff86/representationdetails/60a56925ef206f001ed69179/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
time_period: null
title: Licenses and Inspections Code Violations
usage: null
---
