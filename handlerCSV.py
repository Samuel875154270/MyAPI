import csv

class handlerCSV():

    path = ''

    def __init__(self,path):
        self.path = path

    def write(self,list):
        csvFile = open(self.path, 'a', encoding='utf-8', newline='')
        csvWrite = csv.writer(csvFile)
        csvWrite.writerow(list)
        print('成功写入cvs')

    def read(self):
        csvFile = open(self.path, 'r', encoding='utf-8')
        csvRead = csv.reader(csvFile)

        return csvRead