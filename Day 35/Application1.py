#application to demonstrate operations on excel file using xlsxwriter

import os
import fnmatch
from sys import *
import xlsxwriter

def ExcelCreate(name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    worksheet.write('A1','Name')
    worksheet.write('B1','College')
    worksheet.write('C1','Mail ID')
    worksheet.write('D1','Mobile')

    workbook.close()

def main():
    print("Application Name :"+argv[0])

    if len(argv)!=2:
        print("Invalid number of arguments")
        exit()
    else:
        if argv[1]=="-h" or argv[1]=="-H":
            print("This Script is use to create excel file and write data into it")
            exit()

        elif argv[1]=="-u" or argv[1]=="-U":
            print("Usage : Application_Name Name_of_file.xlsx ")
            exit()

        else:
            try:
                ExcelCreate(argv[1])

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()

        