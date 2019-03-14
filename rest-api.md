### REST APIs

+ API = Application Program Interface
+ REST = Representational State Transfer

##### API Endpoint Examples

+ Resources

```
/api/v1/games --> Collection of Resources (Collection URL)
/api/v1/games/1234 --> Single Resource (Detail URL)
```

+ GET - is used for fetching either a collection of resources or a single resource. All of our previous URLS would be GET-able.
+ POST - is used to add a new resource to a collection. For example, we wouldn't POST to /players/567 or /games/1234 because they aren't collections. we would, however, POST to /players or /games to create a new player ot a new game.
+ PUT - is the HTTP method, or verb, that we use when we want to update a record. We wouldn't use PUT on a collection or list of URLS.
+ DELETE - us used for sending a DELETE request to a detail record, a URL for a single record, should delete just that record. Sending DELETE to an entire collection would delete the whole collection but that's usually not implemented, with good reason.

##### Common HTTP Headers

+ Accept - Specifies the file format that the requester wants (JSON/XML/HTML, etc)
+ Accept-Language - english/spanish/russian.
+ Cache-Control - If the request can be completed from cached data store or not.

##### REST API Best Practices

+ Ensure to check API documentation to see which header types the API accepts.
+ Ensure providing an API version number.
    + Support legacy APIs as long as possible.
+ When using a thrid-party API 

##### Additional Header Information
+ Content-Type --> What type of response was returned - such as JSON.
    + The default content type is HTML.