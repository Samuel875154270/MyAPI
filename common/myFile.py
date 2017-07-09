import csv
import os

class myFile():

    path = ''

    def __init__(self,path):
        self.path = path

    def write(self,str):
        # 以UTF-8编码追加写入
        file = open(self.path, 'a', encoding='UTF-8')
        file.write(str + '\n')
        file.close()

        print('write success')

    def read(self):
        if os.path.exists(self.path):
            file = open(self.path, 'r', encoding='UTF-8')
            reader = file.read()
            file.close()

            return reader
        else:
            print(self.path + ' is not exists')