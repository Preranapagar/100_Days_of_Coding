import pandas as pd
import numpy as np

s = pd.Series()
print(s)
print('-'*80)

data = np.array(['a','b','c','d'])
print(data)
s = pd.Series(data)
print(s)
print(s[0])
print('-'*80)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,200,300,400])
print(s)
print(s[100])
print('-'*80)

data = {'a':0.1,'b':0.2,'c':0.3}
s = pd.Series(data)
print(s)
print('-'*80)

s =pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
