---
area_of_interest: Southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery, Philadelphia counties)
category:
- Transportation
created: '2020-01-01'
license: License Not Specified
maintainer: SEPTA Planning Division
maintainer_email: planning@septa.org
maintainer_link: https://wwww.septa.org/open-data/
maintainer_phone: null
notes: 'Trip data, stop lists, schedules, and KML geometry for SEPTA Metro routes.
  Rail lines (L1, B1, M1) have no onboard GPS — expect null coordinates. Trolley
  routes (T1-T5, G1, D1/D2) have partial GPS on surface segments.

  Example: https://www3.septa.org/api/v2/trips/?route_id=L1'
modified: R/PT1M
organization: SEPTA
resources:
- description: 'active trip locations for a Metro route'
  format: JSON
  name: Metro Trips by Route API
  url: https://www3.septa.org/api/v2/trips/?route_id=L1
- description: 'stop-time details for a specific trip'
  format: JSON
  name: Metro Trip Update API
  url: https://www3.septa.org/api/v2/trip-update/?trip_id=705003
- description: 'ordered stop list for a Metro route'
  format: JSON
  name: Metro Stops by Route API
  url: https://www3.septa.org/api/v2/stops/?route_id=L1
- description: 'scheduled arrivals for a stop on a given route'
  format: JSON
  name: Metro Stop Schedule API
  url: https://www3.septa.org/api/v2/stop-schedule/?route_id=L1&stop_id=32158
- description: 'KML geometry for a Metro route or trip (using L1 route as an example)'
  format: KML
  name: Metro Route KML API
  url: https://www3.septa.org/api/v2/kml/?route=L1&type=route
schema: philadelphia
source: SEPTA
tags:
- SEPTA
- public transit
- metro
time_period: Real-time updates
title: SEPTA Metro APIs
usage: Public Use
---
