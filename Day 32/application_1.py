import pandas as pd

print("Empty data frame")
df = pd.DataFrame()
print(df)
print('-'*80)

print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print('-'*80)

print("Dataframe with list")
data = [['PPA',4],['LB',3],['Python',3],['Angular',3]]
df = pd.DataFrame(data,columns=['Name','Duration'])
print(df)
print('-'*80)

data = {'Name':['PPA','LB','Python','Angular'], 'Duration':[4,3,3,3]}
df = pd.DataFrame(data)
print(df)
print('-'*80)

data = [{'Name':'PPA','Duration':4,'Fees':10500},{'Name':'LB','Duration':3,'Fees':12500},{'Name':'Python','Duration':3.5,'Fees':18000}]
df = pd.DataFrame(data)
print(df)
print('-'*80)

d = {'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['x','y','z','w'])}
df = pd.DataFrame(d)
print(df)
