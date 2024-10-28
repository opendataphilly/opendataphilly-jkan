---
area_of_interest: null
category:
- Elections / Politics
license: Other (City of Philadelphia)
maintainer: City Commissioner's Office
maintainer_email: vote@phila.gov
maintainer_link: null
maintainer_phone: null
notes: "The current dataset captures voter registration counts and voter "turnout," or the percentage of registered voters who voted in each election, since 2017.
  The data is aggregated at various levels including the political precinct (division), political ward, and city-wide and shows results for different elections (primary, general,
  special). Historical releases of this data prior to 2017 were separate datasets, one for voter turnout and one for voter registration."
opendataphilly_rating: null
organization: City of Philadelphia
resources:
- description: 'This data is aggregated city-wide to the current available year.'
  format: CSV
  name: Current City-wide Election Turnout & Registration (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/c768d2802da940c8b631d8e4ef9f403b_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1
- description: 'This data is aggregated city-wide to the current available year.'
  format: API
  name: Current Citywide Election Turnout & Registration (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/election_turnout_city/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Current Citywide Election Turnout & Registration (Metadata)
  url: https://metadata.phila.gov/index.html#home/datasetdetails/6633fd84caf00b00299deb53/representationdetails/663407e3caf00b00299e4553/
- description: 'This data is aggregated at the political ward level to the current available year.'
  format: CSV
  name: Current Wards Election Turnout & Registration (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/e864188e5aa54aeb9b1406b4e2e2505d_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1
- description: 'This data is aggregated at the political ward level to the current available year.'
  format: API
  name: Current Wards Election Turnout & Registration (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/election_turnout_ward/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Current Wards Election Turnout & Registration (Metadata)
  url: https://metadata.phila.gov/index.html#home/datasetdetails/6633fd84caf00b00299deb53/representationdetails/663408552495ad00292706b3/
- description: 'This data is aggregated at the political ward level and displays the Top 5 and Bottom 5 political wards by turnout for each election to the current available year.'
  format: CSV
  name: Current Wards Rank Election Turnout & Registration (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/51f9f31165464025b399a2f98d0c2f4f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1
- description: 'This data is aggregated at the political ward level and displays the Top 5 and Bottom 5 political wards by turnout for each election to the current available year.'
  format: API
  name: Current Wards Rank Election Turnout & Registration (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/election_turnout_ward_rank_5/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Current Wards Rank Election Turnout & Registration (Metadata)
  url: https://metadata.phila.gov/index.html#home/datasetdetails/6633fd84caf00b00299deb53/representationdetails/663408811fe0bf00284a7c70/
- description: 'This data is aggregated at the political division (aka precinct) level to the current available year.'
  format: CSV
  name: Current Precinct Election Turnout & Registration (CSV)
  url: https://opendata.arcgis.com/api/v3/datasets/218a797676f74ee694dc7a49e5360870_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1
- description: 'This data is aggregated at the political division (aka precinct) level to the current available year.'
  format: API
  name: Current Precinct Election Turnout & Registration (API)
  url: https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/election_turnout_division/FeatureServer/0/query?outFields=*&where=1%3D1
- description: ''
  format: HTML
  name: Current Precinct Election Turnout & Registration (Metadata)
  url: https://metadata.phila.gov/index.html#home/datasetdetails/6633fd84caf00b00299deb53/representationdetails/66340816d6478f0028e18ab7/
- description: ''
  format: CSV
  name: Voter Registry 2016 General by Precinct (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_precinct&filename=qualified_voter_listing_2016_general_by_precinct&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Voter Registry 2016 General by Precinct (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_precinct&filename=qualified_voter_listing_2016_general_by_precinct&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Voter Registry 2016 General by Precinct (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_precinct&filename=qualified_voter_listing_2016_general_by_precinct&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Voter Registry 2016 General by Precinct (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2016_general_by_precinct
- description: "\r\n"
  format: CSV
  name: Voter Registry 2016 General by Ward (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_ward&filename=qualified_voter_listing_2016_general_by_ward&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: Voter Registry 2016 General by Ward (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_ward&filename=qualified_voter_listing_2016_general_by_ward&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: ' Voter Registry 2016 General by Ward (GeoJSON)'
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_general_by_ward&filename=qualified_voter_listing_2016_general_by_ward&format=geojson&skipfields=cartodb_id
- description: ''
  format: API
  name: Voter Registry 2016 General by Ward (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2016_general_by_ward
- description: ''
  format: CSV
  name: Voter Registry 2016 Primary by Precinct (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_precinct&filename=qualified_voter_listing_2016_primary_by_precinct&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: "\r\n"
  format: SHP
  name: Voter Registry 2016 Primary by Precinct (SHP)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_precinct&filename=qualified_voter_listing_2016_primary_by_precinct&format=shp&skipfields=cartodb_id
- description: "\r\n"
  format: GeoJSON
  name: Voter Registry 2016 Primary by Precinct (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_precinct&filename=qualified_voter_listing_2016_primary_by_precinct&format=geojson&skipfields=cartodb_id
- description: "\r\n"
  format: API
  name: Voter Registry 2016 Primary by Precinct (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2016_primary_by_precinct
- description: ''
  format: CSV
  name: Voter Registry 2016 Primary by Ward (CSV)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_ward&filename=qualified_voter_listing_2016_primary_by_ward&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: SHP
  name: ' Voter Registry 2016 Primary by Ward (SHP)'
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_ward&filename=qualified_voter_listing_2016_primary_by_ward&format=shp&skipfields=cartodb_id
- description: ''
  format: GeoJSON
  name: Voter Registry 2016 Primary by Ward (GeoJSON)
  url: https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+qualified_voter_listing_2016_primary_by_ward&filename=qualified_voter_listing_2016_primary_by_ward&format=geojson&skipfields=cartodb_id
- description: "\r\n"
  format: API
  name: Voter Registry 2016 Primary by Ward (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2016_primary_by_ward
- description: ''
  format: CSV
  name: Voter Registry 2015 Special Election (CSV)
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+qualified_voter_listing_2015_special_election&format=csv&filename=qualified_voter_listing_2015_special_election&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Registry 2015 Special Election (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2015_special_election
- description: ''
  format: CSV
  name: Voter Registry 2015 Primary (CSV)
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+qualified_voter_listing_2015_primary_election&format=csv&filename=qualified_voter_listing_2015_primary_election&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Registry 2015 Primary (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2015_primary_election
- description: ''
  format: CSV
  name: Voter Registry 2014 General (CSV)
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+qualified_voter_listing_2014_general_election&format=csv&filename=qualified_voter_listing_2014_general_election&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Registry 2014 General (API)
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#qualified_voter_listing_2014_general_election
- description: ''
  format: HTML
  name: Voter Registry (Metadata)
  url: http://metadata.phila.gov/#home/datasetdetails/5543868620583086178c4f83/
- description: ''
  format: CSV
  name: Voter Turnout 2016 Primary Election CSV
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+voter_turnout_primary_election_2016&format=csv&filename=voter_turnout_primary_election_2016&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api documentation
  name: Voter Turnout 2016 Primary Election API
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#voter_turnout_primary_election_2016
- description: ''
  format: CSV
  name: 'Voter Turnout 2016 General Election CSV '
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+voter_turnout_general_election_2016&format=csv&filename=voter_turnout_general_election_2016&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api documentation
  name: Voter Turnout 2016 General Election  API
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#voter_turnout_general_election_2016
- description: ''
  format: CSV
  name: Voter Turnout 2015 Special Election CSV
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+voter_turnout_special_election_2015&format=csv&filename=voter_turnout_special_election_2015&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Turnout 2015 Special Election API
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#voter_turnout_special_election_2015
- description: ''
  format: HTML
  name: Voter Turnout 2015 Special Election Metadata
  url: http://metadata.phila.gov/#home/datasetdetails/5543868120583086178c4f73/representationdetails/55898161ae4c07cd6655e30f/
- description: ''
  format: CSV
  name: Voter Turnout 2015 Primary Election CSV
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+voter_turnout_primary_election_2015&format=csv&filename=voter_turnout_primary_election_2015&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Turnout 2015 Primary Election API
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#voter_turnout_primary_election_2015
- description: ''
  format: HTML
  name: Voter Turnout 2015 Special Metadata
  url: http://metadata.phila.gov/#home/datasetdetails/5543868120583086178c4f73/representationdetails/55438acf9b989a05172d0d81/
- description: ''
  format: CSV
  name: Voter Turnout 2014 General Election CSV
  url: https://phl.carto.com/api/v2/sql?q=select+*+from+voter_turnout_general_election_2014&format=csv&filename=voter_turnout_general_election_2014&skipfields=cartodb_id,the_geom,the_geom_webmercator
- description: ''
  format: api
  name: Voter Turnout 2014 General Election API
  url: https://cityofphiladelphia.github.io/carto-api-explorer/#voter_turnout_general_election_2014
- description: ''
  format: HTML
  name: Voter Turnout 2014 General Metadata
  url: http://metadata.phila.gov/#home/datasetdetails/5543868120583086178c4f73/representationdetails/55438acf9b989a05172d0d82/
schema: philadelphia
source: ''
tags:
- City Commissioners
time_period: null
title: Voter Election Registration and Turnout
usage: null
---
