import os
import xlrd
import xlwt
from xlutils.copy import copy

class myExcel():

    path = ''

    def __init__(self, path):
        self.path = path

    def write(self, row, column, value):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            excel = copy(excel)
            sheet = excel.get_sheet(0)
        else:
            excel = xlwt.Workbook(encoding='UTF-8')
            sheet = excel.add_sheet('Sheet1')

        sheet.write(row, column, value)
        print('write success')
        excel.save(self.path)

    def read(self, row, column):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            read = sheet.cell(row, column).value
            return read
        else:
            print(self.path + ' is not exists')

    def getCols(self):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            columns = sheet.ncols
            return columns
        else:
            print(self.path + ' is not exists')

    def getRows(self):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            rows = sheet.nrows
            return rows
        else:
            print(self.path + ' is not exists')

    def getColValues(self, colx, start_rowx=None, end_rowx=None):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            if (start_rowx==None and end_rowx==None):
                colValues = sheet.col_values(colx)
            else:
                colValues = sheet.col_values(colx, start_rowx, end_rowx)

            return colValues
        else:
            print(self.path + ' is not exists')

    def getRowValues(self, rowx, start_colx=None, end_colx=None):
        if os.path.exists(self.path):
            excel = xlrd.open_workbook(self.path, formatting_info=True)
            sheet = excel.sheet_by_index(0)
            if (start_colx == None and end_colx == None):
                rowValues = sheet.col_values(rowx)
            else:
                rowValues = sheet.col_values(rowx, start_colx, end_colx)

            return rowValues
        else:
            print(self.path + ' is not exists')