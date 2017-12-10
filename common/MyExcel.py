import os
import logging
import xlrd
import xlwt
from xlutils.copy import copy


class MyExcel(object):
    path = ''

    def __init__(self, path):
        self.path = path

    def write(self, row, column, value):
        try:
            if os.path.exists(self.path):
                excel = xlrd.open_workbook(self.path, formatting_info=True)
                excel = copy(excel)
                sheet = excel.get_sheet(0)
            else:
                excel = xlwt.Workbook(encoding='UTF-8')
                sheet = excel.add_sheet('Sheet1')
            sheet.write(row, column, value)
            excel.save(self.path)
            logging.info('write success')
        except Exception as error:
            logging.warning(error)

    def read(self, row, column):
        try:
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            read = sheet.cell(row, column).value
            return read
        except Exception as error:
            logging.warning(error)

    def get_cols(self):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            columns = sheet.ncols
            return columns
        else:
            print(self.path + ' is not exists')

    def get_rows(self):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            rows = sheet.nrows
            return rows
        else:
            print(self.path + ' is not exists')
