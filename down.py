import urllib3
import demjson

url1 = 'http://36.250.93.24/file3.data.weipan.cn/48752396/5bf2db37efaa0b3c228d0909fda7064df4bb3d99?ip=1513002361,58.251.168.33&ssig=C6lds89Nxp&Expires=1513002961&KID=sae,l30zoo1wmz&fn=%E8%B4%B9%E7%BF%94%20-%E3%80%8A%E6%95%85%E4%B9%A1%E7%9A%84%E4%BA%91%E3%80%8B.mp3&skiprd=2&se_ip_debug=58.251.168.33&corp=2&from=1221134&wsrid_tag=5a2e90ca_zhouwangtongxiazai13_25885-62549&wsiphost=local'
http = urllib3.PoolManager()
response = http.request('GET', url1)
print(response.info())
print(response.data)

# with open('费翔 -《故乡的云》.mp3', 'wb') as f:
#     f.write(response.data)
