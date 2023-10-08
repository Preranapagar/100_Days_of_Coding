import pandas as pd

print("Empty data frame")
df = pd.DataFrame()
print(df)

print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

print("Dataframe with list")
data = [['PPA',4],['LB',3]]