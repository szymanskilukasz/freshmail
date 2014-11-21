#FreshMail
A python library which implements the functionality of FreshMail REST API.

[Freshmail](http://freshmail.pl/) - official freshmail site.

[Freshmail PHP library](https://github.com/FreshMail/REST-API) - PHP library which implements the functionality of FreshMail REST API.

## Instructions 

1. Import FmRestApi class and provide both: API_KEY and API_SECRET.

```python

from freshmail import FmRestApi
api_key = YOUR_API_KEY 
api_secret = YOUR_API_SECRET
freshmail = FmRestApi(api_key, api_secret)
```

2. Now you can connect with API by do_request method.

- check your connection with 'ping' action

```python

response = freshmail.do_request('ping')
```

For more information check official API documentation -[http://freshmail.pl/developer-api/autoryzacja/](http://freshmail.pl/developer-api/autoryzacja/)
