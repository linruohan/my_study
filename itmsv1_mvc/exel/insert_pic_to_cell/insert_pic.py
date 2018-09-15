#!/usr/bin/python
# -*- codding: cp936 -*-
import xlsxwriter
def insert_pic(path,sheetname,pic,location):
    book = xlsxwriter.Workbook(path)
    sheetnames=book.sheetnames
    print(sheetnames)
    print(type(sheetnames))
    if sheetname not in book.sheetnames.items():
        sheet = book.add_worksheet(sheetname)
    sheet=book.get_worksheet_by_name(sheetname)
    sheet.insert_image(location,pic)#('D4', 'VCFY6863.jpg')
    book.close()
if __name__ == '__main__':
    path='pict.xlsx'
    location='A1'
    pic= 'passwd.png'
    sheetname='picsheet'
    insert_pic(path, sheetname, pic, location)