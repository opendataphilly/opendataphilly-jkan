---
area_of_interest: Southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery,
  Philadelphia counties)
category:
- Transportation
created: '2014-12-08T22:43:00.116427'
license: License Not Specified
maintainer: null
maintainer_email: MZaleski@septa.org
maintainer_link: http://www.septa.org/cs/comment/
maintainer_phone: 215-580-7800
notes: "SEPTA SMS Transit enables users to request scheduled trip information via\
  \ text message. Users subscribe to the service via text. After setting up an account,\
  \ users can receive schedule information by texting the Stop ID number for a bus,\
  \ trolley, or subway stop to 41411. They will receive a return text with information\
  \ on the four next scheduled trips from that stop. Users can include the specific\
  \ route designation in the text to receive information on a certain route if the\
  \ stop serves multiple routes.\r\n<br><br>\r\nIn addition to using the SMS, there\
  \ is also a simulator which people can use to experiment at no cost.\r\n<br><br>\r\
  \nFinally, the SMS data can be accessed from an API.  The data returned by the API\
  \ is currently text format, \\n separated.  SEPTA expects to add JSON and XML versions\
  \ later.  The API can be accessed in the format:  \r\nhttp://www3.septa.org/sms/var1/var2/var3/\r\
  \n <br><br>\r\n[var1] = stop id\r\n<br>\r\n[var2] = route id  OR  i/o for inbound/outbound\r\
  \n<br>\r\n[var3] = i/o for inbound/outbound only if route id is supplied\r\n <br><br>\r\
  \nStops fall into one of three categories, here's an explanation with some sample\
  \ links:\r\n<br><br>\r\n<ol style=\"list-style: decimal inside none;\">\r\n<li>\r\
  \nStops with service provided by only one route, stop is not the first or last stop\
  \ and\r\nall travel is in a single direction:\r\n<br><br>\r\nhttp://www3.septa.org/sms/321\r\
  \n<br>\r\nReturns the next 4 scheduled trolleys (All Route 13) at Chester Ave &\
  \ 49th St.\r\n<br><br>\r\n</li><li>\r\nStops with service provided by multiple routes,\
  \ but all travel is in one direction:\r\n<br><br>\r\nhttp://www3.septa.org/sms/20645/\r\
  \n<br>\r\nReturns the next 4 scheduled trolleys at 22nd St. Station. Note the results\
  \ shows\r\ntrolleys regardless or route.  To grep just a single route, for a multi-route,\
  \ uni-directional\r\nstop, add another var:\r\n<br><br>\r\nhttp://www3.septa.org/sms/20645/13/\r\
  \n<br>\r\nReturns only the Route 13 trolleys at 22nd St. Station\r\n<br><br>\r\n\
  </li><li>\r\nStops with travel in multi-directions.  This is usually end points,\
  \ like the trolley\r\nloop at Juniper and they may or may not have multiple routes.\
  \  For example:\r\n<br><br>\r\nhttp://www3.septa.org/sms/283\r\n<br>\r\nReturns\
  \ the next 2 inbound and 2 outbound times for all routes\r\n<br><br>\r\nhttp://www3.septa.org/sms/283/13/\r\
  \n<br>\r\nReturns the next 2 inbound and 2 outbound times for only Route 13\r\n\
  <br><br>\r\nhttp://www3.septa.org/sms/283/o \r\n<br>\r\nReturns the next 4 outbound\
  \ times for all routes\r\n<br><br>\r\nhttp://www3.septa.org/sms/283/13/o \r\n<br>\r\
  \nReturns the next 4 outbound times for only Route 13\r\n </li>\r\n</ol>\r\n\r\n\
  \ "
opendataphilly_rating: null
organization: SEPTA
resources:
- description: ''
  format: HTML
  name: SMS Transit Information Page
  url: http://septa.org/about/web/sms.html
- description: ''
  format: HTML
  name: SMS Transit Simulator
  url: http://www3.septa.org/sms/simulator
- description: ''
  format: api
  name: SMS Transit API (text)
  url: http://www3.septa.org/sms/
schema: philadelphia
source: null
tags: []
time_period: null
title: SEPTA SMS Transit
usage: Public Use
---
