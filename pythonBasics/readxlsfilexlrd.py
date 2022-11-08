
import xlrd

path = "D:\Projects\pythonBasics\TestData.xls"

workbook = xlrd.open_workbook(path)

sheet = workbook.sheet_by_name('Sheet1')

# Getting the sheet by index

sheet1 = workbook.sheet_by_index(0)

for sh in workbook.sheets():
    print(sh.name)

row_count = sheet.nrows

column_count = sheet.ncols

print(row_count)

print(column_count)

for cur_row in range(0, row_count):
    for cur_col in range(0, column_count):
        cell = sheet.cell(cur_row, cur_col)
        print(cell.value, cell.ctype)

