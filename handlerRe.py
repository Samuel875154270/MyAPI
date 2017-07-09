import re

class handlerRe():

    def __init__(self):
        return

    def getData(self,pattern,dataSource):
        pattern = re.compile(pattern)
        datas = re.findall(pattern,dataSource)

        return datas
