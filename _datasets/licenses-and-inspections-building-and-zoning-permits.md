---
area_of_interest: null
category: []
created: '2015-05-27T17:14:26.466583'
license: Other (City of Philadelphia)
maintainer: LIGISTEAM@phila.gov
maintainer_email: LIGISTEAM@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "The Department of Licenses & Inspections reviews construction plans and conducts\
  \ building inspections to ensure the safety of the workers and the public. \r\n\r\
  \n[Zoning permits](https://business.phila.gov/zoning-basics/) are issued to authorize\
  \ new construction or additions to a building or to authorize the change of use\
  \ in a building or ground.  \r\n\r\n[Building permits](https://www.phila.gov/services/permits-violations-licenses/build-rent-or-sell-a-property/get-a-building-permit/)\
  \ are required before the start of a specific construction activity to enlarge,\
  \ repair, change, add to or demolish a structure, and to install equipment or systems\
  \ in a structure.  Depending on the scale or type of construction activity, it may\
  \ need to be first authorized via a zoning permit. Subcontractors permits are also available. Plumbing and electrical permits,\
  \ among others, may also be required for new or existing buildings.\r\n\r\n**Please\
  \ note that this is a very large dataset. To see all permits, download all datasets\
  \ for all years.** \r\n\r\n**If you are comfortable with APIs, you can also use\
  \ the API links to access this data. You can learn more about how to use the API\
  \ at Carto\u2019s SQL API site and in the Carto guide in the section on making calls\
  \ to the API.**"
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: ''
  format: HTML
  name: L&I Building & Zoning Permits (Visualization)
  url: https://data.phila.gov/visualizations/li-building-permits
- description: ''
  format: CSV
  name: L&I Building & Zoning Permits - 2016 to present (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=permits&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM permits WHERE permitissuedate
    >= '2016-01-01'
- description: ''
  format: CSV
  name: L&I Building & Zoning Permits - 2007 to 2015 (CSV)
  url: https://phl.carto.com/api/v2/sql?filename=permits&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT
    *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng FROM permits WHERE permitissuedate
    >= '2007-01-01' AND permitissuedate < '2016-01-01'
- description: ''
  format: SHP
  name: L&I Building & Zoning Permits - 2016 to present (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=permits&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM permits WHERE permitissuedate >= '2016-01-01'
- description: ''
  format: SHP
  name: L&I Building & Zoning Permits - 2007 to 2015 (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=permits&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM permits WHERE permitissuedate >= '2007-01-01' AND permitissuedate < '2016-01-01'
- description: ''
  format: API
  name: L&I Building & Zoning Permits - Full Dataset (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#permits
- description: ''
  format: HTML
  name: L&I Building and Zoning Permits (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543868920583086178c4f8f/representationdetails/5e9a01ac801624001585ca11/
- description: ''
  format: CSV
  name: Subcontractors (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/2ef4d79cfec8447b82bfcb2169d99175_0/downloads/data?format=csv&spatialRefId=4326
- description: ''
  format: API
  name: Subcontractors (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/SUBCONTRACTORS/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Subcontractors (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543868920583086178c4f8f/representationdetails/60ad8730d71dfb001e62efa0/
schema: philadelphia
source: ''
tags:
- Department of Licenses and Inspections
time_period: null
title: Licenses and Inspections Building and Zoning Permits
usage: null
---
