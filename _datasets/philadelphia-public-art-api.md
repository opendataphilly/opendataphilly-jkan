---
category: []
extras: {}
license: License Not Specified
maintainer: ''
maintainer_email: ''
notes: "A read-only, RESTful JSON API.\r\nThe core function of the API is to return\
  \ descriptions of pieces of public art in Philadelphia\r\nDocumentation includes\
  \ a JavaScript tester with visible source code.\r\nThere are two primary types of\
  \ data returned by this API: those that exist purely for navigation and those that\
  \ return descriptions of art.\r\nThe JSON format for the artworks is consistent\
  \ in all responses.\r\nSome responses describe collections of art. Some collection\
  \ types include extra information specific to the collection itself.\r\nMostly conforms\
  \ to a HATEOAS model of navigation and the use of the \"links\":{\"rel\":\"X\",\"\
  href\":\"Y\"} structure.\r\nAlso supports a geolocation call which returns a collection\
  \ that is defined by bb and ll URL arguments"
organization: Philart.net
resources:
- description: Documentation page for the Philadelphia Public Art API.
  format: HTML
  name: API Info
  url: http://philart.net/api.html
- description: Top level data.
  format: JSON
  name: API
  url: http://www.philart.net/api.json
schema: default
tags:
- Arts
title: Philadelphia Public Art API
---
