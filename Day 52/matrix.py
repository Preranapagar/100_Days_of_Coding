import pandas as pd
import numpy as np

def read_matrics():
    df = pd.read_excel('matrix.xlsx')
    matrix_data = df.values
    print(matrix_data)

def create_matrics(nums,rows,cols):
    
    result = np.array(nums).reshape(rows,cols)
    df = pd.DataFrame(result)

    file_name = 'matrix.xlsx'
    df.to_excel(file_name, index=False, header=False)

    print("Excel file is created")

def main():
    
    list1 = [1,2,3,4,5,6,7,8,9]
    r = 3
    c = 3

    # create_matrics(list1,r,c)
    read_matrics()


if __name__=='__main__':
    main()