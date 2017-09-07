import urllib.request

class getPictures():

    headers = []

    def __init__(self, headers):
        self.headers = headers
        return

    def download(self, imgurl, downloadPath):
        # http://www.bubuko.com/infodetail-1871264.html  解决下载文件被403
        request = urllib.request
        opener = request.build_opener()
        opener.addheaders = self.headers
        request.install_opener(opener)
        request.urlretrieve(imgurl, downloadPath)

        print('download success')

