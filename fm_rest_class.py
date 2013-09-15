import hashlib
import json
import urllib
import urllib2


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
            post_data = json.dumps(params)
        else:
            post_data = urllib.urlencode(params)

        sign = hashlib.sha1(
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

        req = urllib2.Request(address)
        req.add_header('X-Rest-ApiKey', self.api_key)
        req.add_header('X-Rest-ApiSign', sign)
        req.add_header('Content-Type', self.content_type)
        if post_data != '':
            req.add_data(post_data)

        response = urllib2.urlopen(req)

        self.raw_response = response.read()
        self.http_code = response.getcode()

        if(raw_response):
            return self.raw_response
        self.response = json.loads(self.raw_response)

        if self.http_code != 200:
            self.errors = self.response['errors']
            raise RestMultiError(self.errors)

        return self.response


class RestMultiError(Exception):

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return "; ".join(["Error: message:%s code:%s" % (error['message'], error['code']) for error in self.errors])
