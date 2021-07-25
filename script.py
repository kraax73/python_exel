# coding: UTF-8

import openpyxl
#デスクトップ上の既存Exelファイルの取得
wb = openpyxl.load_workbook('/Users/kicks-t73/Desktop/test.xlsx')
#ファイル内のシートを名前で取得＆名前変更
ws = wb["Sheet1"]
ws.title = "new"

#保存
wb.save('/Users/kicks-t73/Desktop/test.xlsx')
wb.close()

