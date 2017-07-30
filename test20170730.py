from common.myRequest import myRequest
from common.myRe import myRe
from common.getPictures import getPictures
from common.myCSV import myCSV
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'ASPSESSIONIDQATCSSCD=LHFIFKMCCLKNLPOAIIEBEKJC; __BAIDU_STATE_END__=yes; bdshare_firstime=1501423341475; JXM708517=1; JXD708517=1; __cfduid=d11f132b34fb61afa1c2e05a0a58963711501423364; uv_cookie_117675=1; a4031_pages=6; a4031_times=1; __mhcm_cpv_r_4085_cpv_plan_ids=%7C176%7C%7C186%7C%7C185%7C%7C202%7C%7C174%7C',
    'Host':'www.xgyw.cc',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}


pattern = r'55P" src=.([\s\S]*?\.(?:png|jpg|bmp|gif))"'

j = 101
print('正在下载图片...')

for i in range(0,19):
    if i == 0:
        url = 'http://www.xgyw.cc/Xiuren/Xiuren5425.html'
    else:
        url = 'http://www.xgyw.cc/Xiuren/Xiuren5425_%s.html' % i
    html = myRequest(headers).call(url)
    html = html.decode('gbk')
    # print(html)
    imgs = myRe().getReDatas(pattern, html)
    for img in imgs:
        img = 'http://www.xgyw.cc/' + img
        # print(img)
        # myCSV('./csvFile.csv').write([img])
        getPictures().download(img, 'D:/0.整理/12.other/photo/2017/20170730_%s.jpg' % str(j))
        j = j + 1
        time.sleep(1)

print('The End!')

