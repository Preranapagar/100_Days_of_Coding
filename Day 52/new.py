import pandas as pd
import numpy as np

df = pd.read_excel('matrix.xlsx')
print('Data :\n',df)

matrix_1 = df.iloc[0:3].values
print("Matrix 1 :\n",matrix_1)

matrix_2 = df.iloc[3:6].values
print("Matrix 2 :\n",matrix_2)

mult = np.multiply(matrix_1,matrix_2)
print("Multiplication :\n",mult)
