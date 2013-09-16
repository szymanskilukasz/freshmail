from hashlib import sha1
from json import dumps, loads
from urllib import urlencode
from urllib2 import Request, urlopen


class FmRestApi:
    content_type = 'application/json'
    host = 'https://app.freshmail.pl/'
    prefix = 'rest/'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def do_request(self, url, params=None, raw_response=False):
        if params is None:
            post_data = ''
        elif self.content_type == 'application/json':
            post_data = dumps(params)
        else:
            post_data = urlencode(params)

        api_sign = sha1(
            ''.join([
                self.api_key,
                '/',
                self.prefix,
                url,
                post_data,
                self.api_secret
            ])
        ).hexdigest()

        address = ''.join([
            self.host, self.prefix, url
        ])

        request = Request(address)
        request.add_header('X-Rest-ApiKey', self.api_key)
        request.add_header('X-Rest-ApiSign', api_sign)
        request.add_header('Content-Type', self.content_type)
        if post_data != '':
            request.add_data(post_data)

        response = urlopen(request)

        self.raw_response = response.read()
        self.http_code = response.getcode()

        if raw_response:
            return self.raw_response
        self.response = loads(self.raw_response)

        if self.http_code != 200:
            self.errors = self.response['errors']
            raise RestMultiError(self.errors)

        return self.response


class RestMultiError(Exception):

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return "; ".join(["Error: message:%s code:%s" % (error['message'], error['code']) for error in self.errors])
