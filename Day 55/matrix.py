import numpy as np
import pandas as pd

def Transpose_Matrix(m):
    rows = len(m)
    cols = len(m[0])

    trans_mat = [[0]* rows for i in range(cols)]
    
    for i  in range(rows):
        for j in range(cols):
            trans_mat[j][i] = m[i][j]

    return trans_mat

def Inverse_Matrix(m):
    m = m.tolist()
    n = len(m)
    if n != len(m[0]):
        raise ValueError("Input matrix must be square")
    
    augmented_matrix = [ row + [int(i==j)for j in range(n)] for i, row in enumerate(m)]
    
    #Gauss-jordan elimination

    for i in range(n):
        pivot_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        pivot_val = augmented_matrix[i][i]
        augmented_matrix[i] = [val / pivot_val for val in augmented_matrix[i]]

        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [val - factor * augmented_matrix[i][idx] for idx, val in enumerate(augmented_matrix[j])]
    inverted_matrix = [row[n:] for row in augmented_matrix]
    
    return inverted_matrix

def Read_Matrix(fname):
    df = pd.read_excel(f'{fname}.xlsx')
    matrix_1 = df.iloc[0:3,0:3].values
    return matrix_1

def main():
    filename = 'data'
    matrix = Read_Matrix(filename)
    
    print("Original Matrix:\n",matrix)
    print('-'*20)

    Inverted_matrix = Inverse_Matrix(matrix)
    print("Inverted Matrix :")
    for row in Inverted_matrix:
        print(row)

    print('-'*20)
    Transposed_matrix = Transpose_Matrix(matrix)
    print("Transposed Matrix :")
    for row in Transposed_matrix:
        print(row)


if __name__=='__main__':
    main()