import urllib.request


class MyRequest(object):
    headers = ''

    def __init__(self, headers):
        self.headers = headers

    def call(self, url, method='POST', params={}):
        request = urllib.request.Request(url, headers=self.headers)
        if method.upper() == 'POST':
            response = urllib.request.urlopen(request, data=params)
        else:
            response = urllib.request.urlopen(request)
        response = response.read()

        return response
