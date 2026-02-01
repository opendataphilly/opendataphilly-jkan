---
area_of_interest: Philadelphia County
category:
  - Economy
  - Education
  - Environment
  - Health / Human Services
  - Planning / Zoning
  - Real Estate / Land Records
  - Transportation
license: Creative Commons CC Zero
maintainer: U.S. Census Bureau
maintainer_email: census.ask@census.gov
maintainer_link: https://www.census.gov/data/developers/about.html
maintainer_phone: null
notes: |
  Comprehensive access to American Community Survey (ACS) 5-Year Estimates
  for Philadelphia County, Pennsylvania. The ACS is the premier source for
  detailed demographic, social, economic, and housing data about communities
  across the United States.

  This dataset provides API access to 20,000+ variables covering topics
  including:

  - Demographics (age, race, ethnicity, citizenship)
  - Economics (income, poverty, employment, industry, occupation)
  - Housing (tenure, value, costs, conditions, utilities)
  - Education (enrollment, attainment)
  - Transportation (commute mode, travel time, vehicle availability)
  - Health Insurance coverage
  - Veterans and military service
  - Disability status
  - Language spoken at home
  - Ancestry and place of birth
  - Computer and internet access

  The ACS 5-Year Estimates combine 5 years of survey data to provide reliable
  estimates for small geographic areas. Data is updated annually (typically
  released in December). Census geography identifiers can be joined with
  Philadelphia boundary files for spatial analysis.

  Available Geography Levels:
  - County (Philadelphia County aggregate)
  - Census Tract (408 tracts)
  - Block Group (1,816 block groups)
  - County Subdivision

  Key Variable Examples:
  - B01003_001E: Total Population
  - B19013_001E: Median Household Income
  - B17001_002E: Population Below Poverty Level
  - B15003_022E: Bachelor's Degree or Higher
  - B25077_001E: Median Home Value
  - B25064_001E: Median Gross Rent
  - B08301: Means of Transportation to Work (multiple variables)
  - B03002: Hispanic/Latino Origin by Race (multiple variables)
  - B27001: Health Insurance Coverage (multiple variables)

  For complete variable lists and definitions, see the Census Variable Search
  Tool below. No API key required for basic use, but free registration
  provides higher rate limits.
modified: 2023-12-07
organization: U.S. Census Bureau
resources:
  - description: >
      Interactive tool to search and browse all 20,000+ available ACS
      variables. Essential for finding specific demographic, economic, or
      housing variables. Search by keyword or browse by topic.
    format: HTML
    name: ACS Census Variable Search Tool (2018-2022)
    url: https://api.census.gov/data/2022/acs/acs5/variables.html
  - description: >
      Census API endpoint for Philadelphia County aggregate data. Modify the
      get= parameter to include any ACS variables. Example returns total
      population (B01003_001E). Free access, no API key required for basic use.
    format: API
    name: ACS 5-Year Population (2018-2022) - Philadelphia County Level
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E&for=county:101&in=state:42
  - description: >
      Census API endpoint for all Philadelphia census tracts. Returns data
      for 408 census tracts. Modify the get= parameter to query any ACS
      variables. Example includes total population (B01003_001E).
    format: API
    name: ACS 5-Year Population (2018-2022) - Census Tract Level
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E&for=tract:*&in=state:42&in=county:101
  - description: >
      Census API endpoint for all Philadelphia block groups. Returns data for
      1,816 block groups. Most granular geography available. Modify the get=
      parameter to query any ACS variables. Example includes total population (B01003_001E).
    format: API
    name: ACS 5-Year Population (2018-2022) - Block Group Level
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E&for=block%20group:*&in=state:42&in=county:101&in=tract:*
  - description: >
      Example API query for multiple economic variables: median household
      income, poverty rate, employment status, and median home value
      (B19013_001E, B17001_001E, B17001_002E, B23025_003E, B25077_001E) 
      by census tract. 
    format: API
    name: Example - Economic Indicators by Tract
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B19013_001E,B17001_001E,B17001_002E,B23025_003E,B25077_001E&for=tract:*&in=state:42&in=county:101
  - description: >
      Example API query for demographic variables: total population,
      race/ethnicity breakdown by census tract. Includes White alone, Black
      alone, Asian alone, and Hispanic/Latino (B01003_001E, B03002_003E, B03002_004E, B03002_006E ,B03002_012E).
    format: API
    name: Example - Demographics by Tract
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E,B03002_003E,B03002_004E,B03002_006E,B03002_012E&for=tract:*&in=state:42&in=county:101
  - description: >
      Example API query for housing variables: total housing units, occupied
      units, median home value, median rent, owner vs renter occupied by
      census tract (B25001_001E, B25002_002E, B25077_001E, B25064_001E, B25003_001E, B25003_002E, B25003_003E&).
    format: API
    name: Example - Housing Characteristics by Tract
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B25001_001E,B25002_002E,B25077_001E,B25064_001E,B25003_001E,B25003_002E,B25003_003E&for=tract:*&in=state:42&in=county:101
  - description: >
      Example API query for transportation data: means of transportation to
      work including car, public transit, walked, worked from home by census
      tract (B08301_001E, B08301_002E, B08301_010E, B08301_019E, B08301_021E&).
    format: API
    name: Example - Commute Patterns by Tract (2018-2022)
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B08301_001E,B08301_002E,B08301_010E,B08301_019E,B08301_021E&for=tract:*&in=state:42&in=county:101
  - description: >
      Example API query for educational attainment: population 25+ by
      educational level including less than high school, high school
      graduate, some college, bachelor's degree, graduate degree 
      (B15003_001E, B15003_017E, B15003_018E, B15003_022E, B15003_023E).
    format: API
    name: Example - Education Attainment by Tract (2018-2022)
    url: https://api.census.gov/data/2022/acs/acs5?get=NAME,B15003_001E,B15003_017E,B15003_018E,B15003_022E,B15003_023E&for=tract:*&in=state:42&in=county:101
  - description: >
      Comprehensive Census API documentation including query syntax,
      geography options, variable naming conventions, and usage examples.
      Includes information on obtaining a free API key for higher rate
      limits.
    format: HTML
    name: Census API User Guide
    url: https://www.census.gov/data/developers/data-sets/acs-5year.html
  - description: >
      Detailed documentation for the ACS 5-Year dataset including all
      available geographies, groups, variables, and examples. Technical
      reference for advanced users.
    format: HTML
    name: ACS 5-Year Technical Documentation (2018-2022)
    url: https://api.census.gov/data/2022/acs/acs5.html
  - description: >
      Official ACS handbook with detailed information about survey
      methodology, data collection, estimation procedures, and how to
      properly interpret and use ACS data.
    format: PDF
    name: What is the American Community Survey?
    url: https://www.census.gov/programs-surveys/acs/about.html
  - description: >
      Python examples and Jupyter notebooks demonstrating how to access
      Census API data, perform analysis, and create visualizations. Includes
      examples for joining with geographic data.
    format: HTML
    name: Census API Examples (GitHub)
    url: https://github.com/uscensusbureau/census-api-notebook
schema: null
source_url: https://www.census.gov/programs-surveys/acs
tags:
  - census
  - demographics
  - income
  - poverty
  - housing
  - education
  - transportation
  - employment
  - american community survey
title: Census ACS 5-Year Estimates - Philadelphia
---
