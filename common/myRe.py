import re

class myRe():

    def __init__(self):
        return

    def getReDatas(self,pattern,dataSource):
        pattern = re.compile(pattern)
        ReDatas = re.findall(pattern,dataSource)

        return ReDatas