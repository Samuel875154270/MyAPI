import csv
import os

class myCSV():

    path = ''

    def __init__(self,path):
        self.path = path

    def write(self,list):  # csv以list列表写入数据
        # 以UTF-8编码追加写入，newline='' 控制写入不换行
        csvFile = open(self.path, 'a', encoding='UTF-8', newline='')
        write = csv.writer(csvFile)
        write.writerow(list)

        print('write success')

    def read(self):
        if os.path.exists(self.path):
            csvFile = open(self.path, 'r', encoding='UTF-8')
            read = csv.reader(csvFile)

            return read
        else:
            print(self.path + ' is not exists')