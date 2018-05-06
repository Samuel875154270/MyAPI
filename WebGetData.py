import csv
import json
import os
import time
import urllib3
from lxml import etree


def my_formart(my_list):
    if my_list == []:
        return ""
    else:
        return my_list[0].strip()


def mk(mk_path):
    if not os.path.exists(mk_path):
        os.mkdir(mk_path)

def rg(el):
    try:
        return eval(el)
    except:
        return ""

# http = urllib3.PoolManager()
# headers = {
#     "Accept": "text/html,"
#               "text/javascript,"
#               "application/xhtml+xml,"
#               "application/json,"
#               "application/xml;q=0.9,"
#               "image/webp,"
#               "image/apng,"
#               "*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Cookie": "think_language=zh-cn; PHPSESSID=1dbea9djl45fq3rt47hjtk9ql7",
#     "Host": "user.oppfx.com",
#     "Upgrade-Insecure-Requests": 1,
#     "User-Agent": "Mozilla/5.0 "
#                   "(Windows NT 6.3; WOW64) "
#                   "AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) "
#                   "Chrome/66.0.3355.4 "
#                   "Safari/537.36"
# }
#
# for i in range(1, 2500):
#     url = "http://user.oppfx.com"
#     userinfo = "{}/Admin/Member/detail/id/{}".format(url, i)
#     underinfo = "{}/Datas/underinfo".format(url)
#     response_1 = http.request("POST", underinfo, fields={"id": i}, headers=headers).data.decode()
#     response_1 = json.loads(response_1)["info"]
#     response_2 = http.request("GET", userinfo, headers=headers).data.decode()
#     html = etree.HTML(response_2)
#
#     nick_name = rg('response_1["nickname"]')
#     chinese_name = rg('response_1["chineseName"]')
#     phone = rg('response_1["phone"]')
#     email = rg('response_1["email"]')
#     ID = "{}\t".format(my_formart(html.xpath('//*[@id="commentForm"]/div[15]/div/p/text()')))
#     photo_1 = "{}{}".format(url, my_formart(html.xpath('//*[@id="commentForm"]/div[16]/div/a/img/@src')))
#     photo_2 = "{}{}".format(url, my_formart(html.xpath('//*[@id="commentForm"]/div[17]/div/a/img/@src')))
#     bank_address = my_formart(html.xpath('//*[@id="commentForm"]/div[18]/div/p/text()'))
#     bank_id = "{}\t".format(my_formart(html.xpath('//*[@id="commentForm"]/div[20]/div/p/text()')))
#     photo_3 = "{}{}".format(url, my_formart(html.xpath('//*[@id="commentForm"]/div[21]/div/a/img/@src')))
#     photo_4 = "{}{}".format(url, my_formart(html.xpath('//*[@id="commentForm"]/div[22]/div/a/img/@src')))
#
#     file = open("login.csv", "a", newline="", encoding="UTF-8")
#     cf = csv.writer(file)
#     cf.writerow([i, nick_name, chinese_name, phone, email, ID, photo_1, photo_2, bank_address, bank_id, photo_3, photo_4])
#     file.close()
#     print("第{}条记录写入成功。".format(i))
#     time.sleep(0.01)
# print("end")

http = urllib3.PoolManager()

file = open("photo_e.csv", "r")
cf = csv.reader(file)
for li in cf:
    mk_path = "./photo/{}".format(li[0])
    if not os.path.exists(mk_path):
        os.mkdir(mk_path)
    url_1 = li[1]
    url_2 = li[2]
    url_3 = li[3]
    url_4 = li[4]
    if url_1:
        photo_1 = mk_path + "/01." + url_1.split(".")[-1]
        if os.path.exists(photo_1):
            photo_1 = mk_path + "/01(1)." + url_1.split(".")[-1]
        response_1 = http.request("GET", url_1).data
        with open(photo_1, "wb") as f1:
            f1.write(response_1)
    if url_2:
        photo_2 = mk_path + "/02." + url_2.split(".")[-1]
        if os.path.exists(photo_2):
            photo_2 = mk_path + "/02(1)." + url_2.split(".")[-1]
        response_2 = http.request("GET", url_2).data
        with open(photo_2, "wb") as f1:
            f1.write(response_2)
    if url_3:
        photo_3 = mk_path + "/03." + url_3.split(".")[-1]
        if os.path.exists(photo_3):
            photo_3 = mk_path + "/03(1)." + url_3.split(".")[-1]
        response_3 = http.request("GET", url_3).data
        with open(photo_3, "wb") as f1:
            f1.write(response_3)
    if url_4:
        photo_4 = mk_path + "/04." + url_4.split(".")[-1]
        if os.path.exists(photo_4):
            photo_4 = mk_path + "/04(1)." + url_4.split(".")[-1]
        response_4 = http.request("GET", url_4).data
        with open(photo_4, "wb") as f1:
            f1.write(response_4)
    print(li[0], "下载完成")
print("end")
