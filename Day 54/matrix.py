"""Create Python Program that computes following actions :
1. Read Matrix from MS Excel
2. Prints Matrix to MS Excel
3. Give user ability to multiply them, add them, obtain the inverse, the transpose, Eigen vectors and Eigen Values.
It is capable of computing individual row/operations as used in the Gauss-Jordan method for a specific pivot with matrix."""

#Libraries
import pandas as pd
import numpy as np

#Functions
def Read_Excel(fname):
    # filename = input("Enter Filename :")
    filename = fname
    df = pd.read_excel(f'{filename}.xlsx')
    matrix_1 = df.iloc[0:3,0:3].values
    matrix_2 = df.iloc[0:3,3:6].values
    
    return matrix_1, matrix_2

def inverse_matrix(matrix):
    n = len(matrix)
    
    # Check if the matrix is square
    if n != len(matrix[0]):
        raise ValueError("Input matrix must be square")
    
    # Create an identity matrix
    identity = [[0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1
    
    # Augment the matrix with the identity matrix
    augmented_matrix = [row + identity_row for row, identity_row in zip(matrix, identity)]
    
    # Perform Gauss-Jordan elimination with loops
    for i in range(n):
        # Find pivot row
        pivot_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
        
        # Swap rows
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        
        # Scale pivot row to have a leading 1
        pivot_val = augmented_matrix[i][i]
        augmented_matrix[i] = [val / pivot_val for val in augmented_matrix[i]]
        
        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [val - factor * augmented_matrix[i][idx] for idx, val in enumerate(augmented_matrix[j])]
    
    # Extract the inverted matrix from the augmented matrix
    inverted_matrix = [row[n:] for row in augmented_matrix]
    
    return inverted_matrix



def main():
    # print("Matrix Operations")
    # print("1.Read File")
    # option = int(input("Select Operation :"))

    # if option == 1:
    #     print("Reading data......")
    #     Read_Excel()
    # else:
    #     print("Wrong option selection")

    filename = 'data'

    matrices = Read_Excel(filename)

    Inversed_matrix = inverse_matrix(matrices[0])

    print("Original Matrix :\n", matrices[0])
    print("Inversed Matrix :\n", Inversed_matrix)

if __name__=="__main__":
    main()