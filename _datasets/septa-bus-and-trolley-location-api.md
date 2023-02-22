---
category:
- Transportation
extras:
  Area of Interest: Southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery,
    Philadelphia counties)
  Metadata Contact: Michael Zaleski
  OpenDataPhilly Rating: '8'
  Usage: Public use
license: License Not Specified
maintainer: null
maintainer_email: MZaleski@septa.org
notes: "This REST API provides real-time SEPTA vehicle positions based on a GPS data\
  \ feed for each bus and trolley.  There are two services - one returning JSON points\
  \ for the current locations of all vehicles on a particular route and one returning\
  \ a KML route.\r\n<br><br>\r\n<div style='font-weight:bold;'>JSON</div>\r\n\r\n\
  The JSON API has one variable at the end of the URL in the format:\r\n<br>\r\nhttp://www3.septa.org/transitview/bus_route_data/var1\r\
  \n<br><br>\r\n[var1] is the route name.  It must be alpha-numeric and must be a\
  \ valid SEPTA route.  Lettered routes are not case sensitive for the JSON service\
  \ but must be in caps for the KML service.\r\n<br><br>\r\nAn example:\r\nhttp://www3.septa.org/transitview/bus_route_data/23\r\
  \n <br><br>\r\n<div style='font-weight:bold;'>KML</div>\r\nThe KML service trace\
  \ file shows the patterns that the route follows.  The API has one variable in the\
  \ format:\r\n <br>\r\nhttp://www3.septa.org/transitview/kml/var1\r\n<br><br>\r\n\
  [var1] is the name of the route.  Lettered routes must be in Caps, such as:\r\n\
  http://www3.septa.org/transitview/kml/G"
organization: SEPTA
resources:
- description: ''
  format: api
  name: SEPTA Vehicle Location API (JSON)
  url: http://www3.septa.org/transitview/bus_route_data/
- description: ''
  format: KML
  name: SEPTA Vehicle Route API (KML)
  url: http://www3.septa.org/transitview/kml/
schema: default
tags: []
title: SEPTA Bus and Trolley Location API
---
