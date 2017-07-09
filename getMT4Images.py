# http://member.cfa-fx.com/index.php?r=admin/login/login
# 用户名：106  密码：Qwer@1234

from handlerCSV import handlerCSV
from handlerRe import handlerRe
import urllib.request
import urllib

headers = {
    'Host': 'member.cfa-fx.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://member.cfa-fx.com/index.php?r=admin/account/account',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'PHPSESSID=imhp4tjqavi3ts3tj9er72qt83; rem_ausername=106'
}

pattern = r'<img src=".([\s\S]*?\.(?:png|jpg|bmp|gif))"'
datas = []
i = 1

csv = handlerCSV('./MT4Account.csv')
csvdatas = csv.read()
for data in csvdatas:
    url = 'http://member.cfa-fx.com/index.php?r=admin/account/modaccountinfo&userid=' + str(data[0])
    # print(url)

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    response = bytes(response.read()).decode(encoding='utf-8')
    re = handlerRe()
    reDatas = re.getData(pattern, response)
    # print(reDatas)

    for reData in reDatas:
        reData = 'http://member.cfa-fx.com' + str(reData)
        csv = handlerCSV('./MT4Images.csv')
        csv.write([reData])
        # print(reData)
        # print(ImaName)

csv = handlerCSV('./MT4Images.csv')
Imgdatas = csv.read()
print('正在下载图片...')
for img in Imgdatas:
    imgStr = img[0]
    # print(imgStr)
    ImaName = imgStr.split('http://member.cfa-fx.com/upfile/files/')[1]
    try:
        urllib.request.urlretrieve(imgStr, './MT4Img/%s' % ImaName)
    except Exception as msg:
        print(msg)


print('The End!')