---
area_of_interest: Southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery, Philadelphia counties)
category:
- Transportation
created: '2014-12-08'
license: License Not Specified
maintainer: SEPTA Planning Division
maintainer_email: planning@septa.org
maintainer_link: https://wwww.septa.org/open-data/
maintainer_phone: null
notes: 'TransitView provides real-time information about SEPTA buses and trolleys. 
  TransitViewAll returns all current bus and trolley locations. TrnasitView accepts
  a route number and retuns locations for all vehicles on that route.
  
  Example: https://www3.septa.org/api/TransitView/index.php?route=33 returns all vehicles on bus route 33' 
modified: R/PT5M
organization: SEPTA
resources:
- description: 'returns all bus and trolley locations'
  format: JSON
  name: TransitView All Locations API
  url: https://www3.septa.org/api/TransitViewAll/index.php
- description: 'returns bus and trolley locations for a specific route number'
  format: JSON
  name: TransitView Route Locations API
  url: https://www3.septa.org/api/TransitView/index.php
schema: philadelphia
source: SEPTA
tags: 
- SEPTA
- public transit
time_period: Current
title: SEPTA TransitView
usage: Public Use
---
