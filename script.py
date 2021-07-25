# coding: UTF-8

#モジュール読み込み
import openpyxl

#デスクトップ上の既存Exelファイルの取得
wb = openpyxl.load_workbook('/Users/kicks-t73/Desktop/test.xlsx')

ws = wb.active

#b1 = ws['B1'].value
#b2 = ws['B2'].value
#b3 = ws['B3'].value
#「row = 行数」、「column = 列数」、「value = 値」
#ws.cell(row = 1, column = 3).value = b1*10 
#ws.cell(row = 2, column = 3).value = b2*10
#ws.cell(row = 3, column = 3).value = b3#*10

#B列を取得
col = ws['B']

#B列の全値を出力
for col_data in col:
    print(col_data.value)

#保存
wb.save('/Users/kicks-t73/Desktop/test.xlsx')
wb.close()

