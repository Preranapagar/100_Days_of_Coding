import pandas as pd

#demonstration of operations on Excel file using pandas

batches = pd.read_excel("Data.xlsx")
print(batches)

batches_sheet1 = pd.read_excel("Data.xlsx",sheet_name=0,index_col=0)
print(batches_sheet1.head())

xlsx = pd.ExcelFile("Data.xlsx")
batches_sheet = []

for sheet in xlsx.sheet_names:
    print(sheet)
    batches_sheet.append(xlsx.parse(sheet))

batches2 = pd.concat(batches_sheet)
print(batches2)