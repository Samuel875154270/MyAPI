import urllib.request

class myRequest():

    headers = ''

    def __init__(self,headers):
        self.headers = headers

    def call(self,url,params=None,isPost=False):
        request = urllib.request.Request(url, headers=self.headers)

        if not isPost:
            response = urllib.request.urlopen(request)

        else:
            response = urllib.request.urlopen(request, data=params)

        # response = bytes(response.read()).decode(encoding='utf-8')
        response = response.read()

        return response