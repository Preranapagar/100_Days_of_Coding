import pandas as pd

data = [{'Name':'PPA','Duration':3,'Fees':18500},{'Name':'Angular','Duration':4,'Fees':20000},
        {'Name':'LB','Duration':3.2,'Fees':19500}]

df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name='Sheet1')

writer.save()