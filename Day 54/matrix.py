"""Create Python Program that computes following actions :
1. Read Matrix from MS Excel
2. Prints Matrix to MS Excel
3. Give user ability to multiply them, add them, obtain the inverse, the transpose, Eigen vectors and Eigen Values.
It is capable of computing individual row/operations as used in the Gauss-Jordan method for a specific pivot with matrix."""

#Libraries
import pandas as pd
import numpy as np

#Functions
def Read_Excel():
    filename = input("Enter Filename :")
    df = pd.read_excel(f'{filename}.xlsx')
    matrix_1 = df.iloc[0:3,0:3].values
    matrix_2 = df.iloc[0:3,3:6].values
    print(matrix_1)
    print(matrix_2)

def main():
    print("Matrix Operations")
    print("1.Read File")
    option = int(input("Select Operation :"))

    if option == 1:
        print("Reading data......")
        Read_Excel()
    else:
        print("Wrong option selection")

if __name__=="__main__":
    main()