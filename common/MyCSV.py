import csv
import logging


class MyCSV(object):
    @staticmethod
    def write(path, list_data):  # csv以list列表写入数据
        try:
            # 以UTF-8编码追加写入，newline='' 控制写入不换行
            csv_file = open(path, 'a', encoding='UTF-8', newline='')
            write = csv.writer(csv_file)
            write.writerow(list_data)
            logging.info('write success')
        except Exception as error:
            logging.warning(error)

    @staticmethod
    def read(path):
        try:
            csv_file = open(path, 'r', encoding='UTF-8')
            content = csv.reader(csv_file)
            return content
        except Exception as error:
            logging.warning(error)
