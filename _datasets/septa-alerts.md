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
notes: 'Provides access to SEPTA travel alerts via an API. All travel alerts can be 
  viewed at https://www3.septa.org/api/Alerts/.<br>
  <br>
  To retrieve travel alerts for a specific route or line, add the parameter: route/line name 
  to the URL.<br>
  <br>Example: https://www3.septa.org/api/Alerts/index.php?routes=bus_route_33
  <br>
  <br>The API endpoint at get_alert_data.php provides more verbose messages for either the whole system or a single route
  <br>Example: https://www3.septa.org/api/Alerts/get_alert_data.php?route_id=bus_route_33'
opendataphilly_rating: null
organization: SEPTA
resources:
- description: 'can return all alerts in SEPTA system or alerts for a specific route'
  format: JSON
  name: SEPTA Travel Alerts API with no message
  url: http://www3.septa.org/api/Alerts/index.php
- description: ''
  format: JSON
  name: SEPTA Travel Alerts API with full messages
  url: http://www3.septa.org/api/Alerts/get_alert_data.php
schema: philadelphia
source: null
tags: []
time_period: null
title: SEPTA Alerts
usage: Public Use
---
