
import pandas as pd
import numpy as np

def mult(a,b):
    multiplication = np.multiply(a,b)
    result = pd.DataFrame(multiplication)
    result.to_excel("Multiplication_result.xlsx")
    print("Multiplication Result Generated")

def add(a,b):
    addition = a + b
    result = pd.DataFrame(addition)
    result.to_excel("Addition_result.xlsx")
    print("Addition Result Generated")

def main():
    df = pd.read_excel('matrix.xlsx', header=None)
    print(df)

    matrix_a = df.iloc[0:3].values
    matrix_b = df.iloc[3:6].values

    mult(matrix_a, matrix_b)
    add(matrix_a, matrix_b)

if __name__=="__main__":
    main()