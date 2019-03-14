### HTTP Basics

##### HTTP Reponses

+ Reponses in the 200 range are successful
+ Reponses in the 300 range have moved
+ Reponses in the 400 range are error in the client's request
+ Reponses in the 500 range something went wrong on the server side

+ HTTP is Stateless
    + No record of previous interactions, and each interaction is processed only with the informatiom that comes with that particular interaction.

##### HTTP Get Request Query Strings

+ Get requests are read only requests.
+ Query strings always start with a '?'
+ Each key and value is separated by '='
+ Each pair of key/value is separated by '&'
+ Example. "google.com?q=my-search-query"

##### There are 5 basic factors to an HTML form
1. Form tags
1. Form method attribute - optional, defaults to 'get'
1. Form action attribute - named input elements
1. Form elements for user to provide info
1. Submit button - optional, triggered with ENTER

```html
<form method="post" actions="register">
</form>
```

+ Using 'name' and 'value' tags are essential to crafting query strings.

```html
<input type="hidden" name="search_p_val" value="en">
```

+ The query string would be passed like "domain.com/?search_p_val=en"