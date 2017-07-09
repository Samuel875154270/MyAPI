from handlerCSV import handlerCSV
import urllib.request
import urllib

csv = handlerCSV('./MT4Images.csv')
Imgdatas = csv.read()

for img in Imgdatas:
    imgStr = img[0]
    # print(imgStr)
    ImaName = imgStr.split('http://member.cfa-fx.com/upfile/files/')[1]
    try:
        urllib.request.urlretrieve(imgStr, './MT4Img/%s' % ImaName)
    except Exception as msg:
        print(msg)
print('end')