import xlrd, xlwt, xlutils
import os

def write_excel (filename, data):
    book = xlwt.Workbook()
    sheet = book.add_sheet ('sheet1')
    c = 0
    for d in data:
        for index in range(len(d)):
            sheet.write(c, index, d[index])
            c = c + 1
            book.save (filename)
    return

def read_filename_in_folder (filepath, list):
    for root, dirs, files in os.walk(filepath):
        list.append(files)
    return

filename_list = []
source = input("输入读取的文件夹路径：")
dest = input("选择输出路径：")
read_filename_in_folder(source, filename_list)
write_excel(dest, filename_list)

