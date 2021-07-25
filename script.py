# coding: UTF-8

import openpyxl

wb = openpyxl.load_workbook('/Users/kicks-t73/Desktop/test.xlsx')

ws = wb["Sheet1"]
ws.title = "new"

wb.save('/Users/kicks-t73/Desktop/test.xlsx')
wb.close()

