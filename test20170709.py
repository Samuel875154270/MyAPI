from common.myCSV import myCSV

list = ['list', '列表', 123]
tup = ('tup', '元组',  456)
dict = {
    'Chinese': '字典',
    'string': 'dict',
    'digit': 789
}
str = 'abc'
num = 123.01

listData1 = [list,tup,dict,str,num]
listData2 = [num,str,tup,list,dict]

csv = myCSV('./csvFile.csv')
# 写入csv
csv.write(listData1)
csv.write(listData2)
# 读取csv
reader = csv.read()
for data in reader:
    print(data)