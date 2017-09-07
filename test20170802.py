from common.myRequest import myRequest
from common.myRe import myRe
from common.getPictures import getPictures
from common.myCSV import myCSV
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection':'keep-alive',
    'Cookie': 'ASPSESSIONIDQCASBDBA=HDONIBGBHDIBIPNFBOJEOANJ; UM_distinctid=15da7f19a01369-0ac88b06b403b9-62101875-100200-15da7f19a028cc; CNZZDATA1254428444=1700717456-1501760490-%7C1501760490; Hm_lvt_731a53a94394c1764ce2ab6cc1a76d2d=1501761215; Hm_lpvt_731a53a94394c1764ce2ab6cc1a76d2d=1501761215',
    'Host': 'zhaifuli.xyz',
    # 'If-Modified-Since': 'Fri, 16 Jun 2017 12:40:16 GMT',
    # 'If-None-Match': '"dad84b49de6d21:0"',
    'Upgrade-Insecure-Requests':1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
ImgHeader = [
    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
    ('Accept-Encoding','gzip, deflate, sdch'),
    ('Accept-Language','zh-CN,zh;q=0.8'),
    ('Cache-Control','max-age=0'),
    ('Connection','keep-alive'),
    ('Host','images.zhaofulipic.com:8818'),
    # ('If-Modified-Since','Fri, 25 Nov 2016 12:53:00 GMT'),
    ('If-None-Match','"5838342c-19019"'),
    # ('Referer','http://zhaifuli.xyz/luyilu/2016/1125/2650.html'),
    ('Upgrade-Insecure-Requests',1),
    ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36')
]

# pattern = r'64P" src=.([\s\S]*?\.(?:png|jpg|bmp|gif))"'
pattern = r'<img src=.(http://[\s\S]*?\.(?:png|jpg|bmp|gif))" alt='


j = 301
print('正在下载图片...')

for i in range(1, 9):
    if i == 1:
        # url = 'http://www.xgyw.cc/Xiuren/Xiuren5425.html'
        # url = 'http://www.xgyw.cc/MTMeng/6052.html'
        # url = 'http://www.xgyw.cc/YouWu/YouWu5680.html'
        url = 'http://zhaifuli.xyz/luyilu/2016/1125/2650.html'
        # url = 'http://www.xgyw.cc/MFStar/MFStar4281.html'
        # url = 'http://www.xgyw.cc/BoLoli/BoLoli6772.html'
    else:
        url = 'http://zhaifuli.xyz/luyilu/2016/1125/2650_%s.html' % i
    # print(url)
    html = myRequest(headers).call(url)
    html = html.decode('gbk')
    # print(html)
    imgs = myRe().getReDatas(pattern, html)
    for img in imgs:
        # img = 'http://www.xgyw.cc/' + img
        # print(img)
        # myCSV('./csvFile.csv').write([img])
        getPictures(ImgHeader).download(img, 'D:/0.整理/12.other/photo/2017/20170730_%s.jpg' % str(j))
        j = j + 1
        time.sleep(1)

print('The End!')




