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
notes: 'SEPTA SMS Transit enables users to request scheduled trip information via 
  text message. Users subscribe to the service via text. After setting up an account, 
  users can receive schedule information by texting the Stop ID number for a bus, 
  trolley, or subway stop to 41411. They will receive a return text with information 
  on the four next scheduled trips from that stop. Users can include the specific 
  route designation in the text to receive information on a certain route if the 
  stop serves multiple routes.
  In addition to using the SMS, there 
  is also a simulator which people can use to experiment at no cost. 
  
  Finally, the SMS data can be accessed from an API.  The data returned by the API
  is currently text format, separated.  The API can be accessed in the format:
  https://www3.septa.org/sms/var1/var2/var3/var4/var5  <br>
  
  \[var1\] = stop id <br>
  \[var2\] = route id  OR  i/o for inbound/outbound <br>
  \[var3\] = i/o for inbound/outbound only if route id is supplied <br>
  \[var4\] = returns schedule times on or after specified date, format: MM/DD/YYYY. Defaults to current day. <br>
  \[var5\] = returns schedule times on or after specified time, format: HH:mm:ss. Defaults to current time. <br>
  <br>
  Stops fall into one of three categories, here is an explanation with some sample links:

  <ol>
    <li>Stops with service provided by only one route, stop is not the first or last stop
  andall travel is in a single direction:
      
      <br><br>[https://www3.septa.org/sms/321](https://www3.septa.org/sms/321)<br>
  Returns the next 4 scheduled trolleys (All Route 13) at Chester Ave &
  49th St.</li>
    
    <li>Stops with service provided by multiple routes, 
  but all travel is in one direction:
  <br><br>

  https://www3.septa.org/sms/20645/<br>
  Returns the next 4 scheduled trolleys at 22nd St. Station. Note the results shows
  trolleys regardless or route.  To grep just a single route, for a multi-route, uni-directional stop, add another var: <br>
      
  https://www3.septa.org/sms/20645/13/<br>
  Returns only the Route 13 trolleys at 22nd St. Station</li>
  
  <li>Stops with travel in multi-directions.  This is usually end points,
   like the trolley loop at Juniper and they may or may not have multiple routes.
    For example:<br>
    
    https://www3.septa.org/sms/283 <br>
    Returns the next 2 inbound and 2 outbound times for all routes

    https://www3.septa.org/sms/283/13/<br>
    Returns the next 2 inbound and 2 outbound times for only Route 13

    https://www3.septa.org/sms/283/o <br>
    Returns the next 4 outbound times for all routes

    https://www3.septa.org/sms/283/13/o <br>
    Returns the next 4 outbound times for only Route 13 </li>

  </ol>
   '
opendataphilly_rating: null
organization: SEPTA
resources:
- description: ''
  format: API
  name: SMS Transit API (text)
  url: https://www3.septa.org/sms/
- description: ''
  format: HTML
  name: SMS Transit Simulator
  url: https://www3.septa.org/sms/simulator
schema: philadelphia
source: null
tags: []
time_period: null
title: SEPTA SMS Transit
usage: Public Use
---
