#Manipulate matrix by reversing its rows and columns
#Input : [[1,2,3],[4,5,6],[7,8,9]]  Output: [[1,4,7],[2,5,8],[3,6,9]]
import numpy as np

def transpose(matrix):
    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])

    transposed = [[0 for j in range(no_of_rows)] for i in range(no_of_columns)]

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            transposed[j][i] = matrix[i][j]

    transposed = np.array(transposed)

    return transposed


def main():

    n = int(input("Enter the number of rows :"))
    m = int(input("Enter the number of columns :"))

    matrix =[]

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(int(input("Enter the Number :")))

    matrix = np.array(matrix)

    transposed_matrix = transpose(matrix)

    print("Original Matrix :\n", matrix)

    print("Transposed Matrix :\n", transposed_matrix)

if __name__=="__main__":
    main()