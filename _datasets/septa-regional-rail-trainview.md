---
area_of_interest: Southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery, Philadelphia counties)
category:
- Transportation
created: '2014-12-08'
license: License Not Specified
maintainer: SEPTA
maintainer_email: septoid@gmail.com
maintainer_link: https://wwww.septa.org/open-data/
maintainer_phone: null
notes: '
  The TrainView API returns information on all current regional rail trains.
<br><br>
  The NextToArrive API returns departure and arrival times between two different stations.
  Please refer to the Regional Rail Inputs page (see below) to see all valid inputs.
<ul>
 <li>req1 is the starting Regional Rail station</li>
 <li>req2 is the ending Regional Rail station</li>
 <li>req3 is an integer with the number of results to show</li>
</ul>
<br><br>
  The Arrival/Departure API returns a list/queue of regional rail trains to arrive at a station in two/both directions.
  The direction is demarcated as either Northbound or Southbound. The directions are obviously
  not geographical references, but rather a reference to the old Reading and Pennsy Railroads.
  The key to understanding the direction is by using Suburban Station as a starting point:
  Any trains that move eastbound towards Market East are all considered Northbound; trains
  going from suburban t o 30th St are all Southbound. The path field describes more accurately
  the path of travel along various branches. Every regional stop is a valid parameter.
  Please refer to the Regional Rail Inputs page (see below) to see all valid inputs.
'

opendataphilly_rating: null
organization: SEPTA
resources:
- description: 'Creates a list of all Regional Rail trains on the system. Showing the trains ID number, its starting location, its destination, and if its late or not'
  format: JSON
  name: Regional Rail TrainView API
  url: https://www3.septa.org/api/TrainView/index.php
- description: 'Creates a list of departure/arrival times between two stations'
  format: JSON
  name: Regional Rail NextToArrive API
  url: https://www3.septa.org/api/TrainView/index.php
- description: 'Accepts station, results (number of results), and and direction (N/S)'
  format: JSON
  name: Regional Rail Station Arrivals and Departures API
  url: https://www3.septa.org/api/Arrivals/index.php
- description: 'List of regional rail station ids'
  format: HTML
  name: Regional Rail Station Inputs
  url: https://www3.septa.org/VIRegionalRail.html
schema: philadelphia
source: null
tags: []
time_period: null
title: SEPTA Regional Rail APIs
usage: Public Use
---
