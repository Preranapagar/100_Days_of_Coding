import pandas as pd

array = [['A','A','B','B'],[1,2,1,2]]

index = pd.MultiIndex.from_arrays(array,names = ('Letter','Number'))

data = {'Value':[10,20,30,40]}

df = pd.DataFrame(data, index=index)

print(df)