import urllib.request

class getPictures():

    headers = ''

    def __init__(self):
        return

    def download(self,imgurl,downloadPath):
        urllib.request.urlretrieve(imgurl,downloadPath)

        print('download success')