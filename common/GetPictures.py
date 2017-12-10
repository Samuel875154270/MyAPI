import urllib.request
import logging


class GetPictures(object):
    headers = []

    def __init__(self, headers):
        self.headers = headers

    def download(self, img_url, download_path):
        # http://www.bubuko.com/infodetail-1871264.html  解决下载文件被403
        request = urllib.request
        opener = request.build_opener()
        opener.addheaders = self.headers
        request.install_opener(opener)
        request.urlretrieve(img_url, download_path)
        logging.info('download success')
