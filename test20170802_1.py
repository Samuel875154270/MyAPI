from common.myRequest import myRequest
from common.myRe import myRe
from common.getPictures import getPictures
from common.myCSV import myCSV
import urllib.request
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

headers0 = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36')
headers1 = ('Cookie', 'UM_distinctid=15d344097194ac-046d3f1e31176c-62101875-100200-15d3440971a907; ASPSESSIONIDSACQDABA=AEAMKFJABMDFFMKMBFIKBKKB; CNZZDATA1254428444=768632678-1499816118-http%253A%252F%252Fc.pc.qq.com%252F%7C1501674083; Hm_lvt_731a53a94394c1764ce2ab6cc1a76d2d=1499820236,1499866510,1501679342; Hm_lpvt_731a53a94394c1764ce2ab6cc1a76d2d=1501679359')
headers2 = ('Host', 'zhaofuli.mobi')

csv = myCSV('./csvFile.csv').read()

j = 301
print('正在下载图片...')

request = urllib.request
opener = request.build_opener()
opener.addheaders = [headers0]
opener.addheaders = [headers1]
opener.addheaders = [headers2]
request.install_opener(opener)

for img in csv:
    print(img[0])
    request.urlretrieve(img[0], 'D:/0.整理/12.other/photo/2017/20170730_%s.jpg' % str(j))
    j = j + 1


print('The End!')

