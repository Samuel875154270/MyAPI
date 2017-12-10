import re


class MyRe(object):
    @staticmethod
    def get_data(pattern, data_source):
        pattern = re.compile(pattern)
        data = re.findall(pattern, data_source)
        return data
