from common.myCSV import myCSV
from common.myRe import myRe
from common.myRequest import myRequest
from common.myFile import myFile

# list = ['list', '列表', 123]
# tup = ('tup', '元组',  456)
# dict = {
#     'Chinese': '字典',
#     'string': 'dict',
#     'digit': 789
# }
# str = 'abc'
# num = 123.01
#
# listData1 = [list,tup,dict,str,num]
# listData2 = [num,str,tup,list,dict]
#
# csv = myCSV('./csvFile.csv')
# # 写入csv
# csv.write(listData1)
# csv.write(listData2)
# # 读取csv
# reader = csv.read()
# for data in reader:
#     print(data)

# pattern = r'1[3|5|7|8][2-9][0-9]{8}'
# dataHtml = 'asdkhsfhkhdas13800138000asdkhk13000138000asdk123asdkh1571239782317412308123'
# reDatas = myRe().getReDatas(pattern,dataHtml)
# print(reDatas)
# for reData in reDatas:
#     print(reData)

# headers = {
#     'Host': 'member.cfa-fx.com',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': 1,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Referer': 'http://member.cfa-fx.com/index.php?r=admin/account/account',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cookie': 'PHPSESSID=imhp4tjqavi3ts3tj9er72qt83; rem_ausername=106'
# }
# url = 'http://member.cfa-fx.com/index.php?r=admin/account/account'
# params =  b'datetype=day&UserID=&uusername=&AncestorNodeLogin=&pageNo=5&currentPage=4'
# # params = params.encode(encoding="utf-8")
#
# request = myRequest(headers)
# get = request.call(url)
# # print(get)
# post = request.call(url,params,True)
# # print(post)

txt = myFile('./txt.txt')
txt.write('中文')
txt.write('一级')

read = txt.read()
print(read)