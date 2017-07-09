# http://member.cfa-fx.com/index.php?r=admin/login/login
# 用户名：106  密码：Qwer@1234

from handlerCSV import handlerCSV
from handlerRe import handlerRe
import urllib.request

url = 'http://member.cfa-fx.com/index.php?r=admin/account/account'

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

pattern = r'<div class="leibie">([\s\S]*?)</div>'
datas = []
i = 1
x = 1

for x in range(1,19):
    if x == 1:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        response = bytes(response.read()).decode(encoding='utf-8')
        re = handlerRe()
        reData = re.getData(pattern, response)

        for data in reData:
            if i % 8 != 0:
                datas.append(data)
            else:
                datas.append(data)
                csv = handlerCSV('./MT4.csv')
                csv.write(datas)
                datas = []
            i += 1
    else:
        formData = 'datetype=day&UserID=&uusername=&AncestorNodeLogin=&pageNo=' + str(x) + '&currentPage=' + str(x - 1)
        formData = formData.encode(encoding="utf-8")
        request = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(request,data=formData)
        response = bytes(response.read()).decode(encoding='utf-8')
        re = handlerRe()
        reData = re.getData(pattern,response)

        for data in reData:
            if i%8 != 0:
                datas.append(data)
            else:
                datas.append(data)
                csv = handlerCSV('./MT4.csv')
                csv.write(datas)
                datas = []
            i += 1

print('The End!')