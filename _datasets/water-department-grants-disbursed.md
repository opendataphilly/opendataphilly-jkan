---
category:
- Environment
extras:
  Area of Interest: Grants
  Department: Water Department
  Maintainer Phone: (215) 685-6300
  Time Period: FY 2014 to FY 2014
  Update Frequency: Quarterly
  Usage: No limitations.
license: Other (City of Philadelphia)
maintainer: Phil Pierdomenico
maintainer_email: raymond.pierdomenico@phila.gov
notes: "Collection Process:  This data set reflects the recipients, award amounts,\
  \ and project sites for grant money disbursed by the Philadelphia Water Department.\
  \ It includes the Stormwater Management Incentive Program, the Soak It Up! Adoption\
  \ Program Grant, the Green Acre Retrofit Program, and Business Incentive Program.\
  \ These grants are funded by the Water Department but managed by separate agencies.\r\
  \nData Purpose:  This data can be useful for non-commercial properties looking for\
  \ assistance to reduce their stormwater bill.\r\nIntended Audience:  It can also\
  \ be useful to community organizations interested in serving as stewards of green\
  \ infrastructure located in their area. And it can be useful to businesses impacted\
  \ by PWD projects."
organization: City of Philadelphia
resources:
- description: ''
  format: CSV
  name: Stormwater Grants Disbursed (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+stormwater_grants&filename=stormwater_grants&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Stormwater Grants Disbursed (SHP)
  url: https://phl.carto.com/api/v2/sql?filename=stormwater_grants&format=shp&skipfields=cartodb_id&q=SELECT
    * FROM stormwater_grants
- description: ''
  format: GeoJSON
  name: Stormwater Grants Disbursed (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?filename=stormwater_grants&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+stormwater_grants
- description: ''
  format: API Documentation
  name: Stormwater Grants Disbursed (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#stormwater_grants
- description: ''
  format: HTML
  name: Stormwater Grants Disbursed (Metadata)
  url: https://metadata.phila.gov/#home/datasetdetails/5543867620583086178c4f43/representationdetails/561801cc3951b18d0e488b58/
- description: ''
  format: CSV
  name: GSI SoakItUp Adoption Sites (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/98b55cc5364349b283f895e389fd6d25_0/downloads/data?format=csv&spatialRefId=4326
- description: ''
  format: SHP
  name: GSI SoakItUp Adoption Sites (SHP)
  url: https://opendata.arcgis.com/api/v3/datasets/98b55cc5364349b283f895e389fd6d25_0/downloads/data?format=shp&spatialRefId=4326
- description: ''
  format: GeoJSON
  name: GSI SoakItUp Adoption Sites (GeoJSON)
  url: https://opendata.arcgis.com/datasets/98b55cc5364349b283f895e389fd6d25_0.geojson
- description: ''
  format: API
  name: GSI SoakItUp Adoption Sites (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/GSI_SoakItUp_Adoption_Sites/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: GSI SoakItUp Adoption Sites (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5543867620583086178c4f43/representationdetails/5618025d210ba1dc0238ce6c/
schema: default
tags:
- Philadelphia Water Department
title: Water Department Grants Disbursed
---
