import logging


class MyFile(object):
    @staticmethod
    def write(path, contents):
        try:
            # 以UTF-8编码追加写入
            file = open(path, 'a', encoding='UTF-8')
            file.write(contents + '\n')
            file.close()
            logging.info('write success')
        except Exception as error:
            logging.warning(error)

    @staticmethod
    def read(path):
        try:
            file = open(path, 'r', encoding='UTF-8')
            reader = file.read()
            file.close()
            return reader
        except Exception as error:
            logging.warning(error)
