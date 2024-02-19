def determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

def cofactor(matrix):
    return [[matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1],
             matrix[0][2]*matrix[2][1] - matrix[0][1]*matrix[2][2],
             matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]],
            [matrix[1][2]*matrix[2][0] - matrix[1][0]*matrix[2][2],
             matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0],
             matrix[0][2]*matrix[1][0] - matrix[0][0]*matrix[1][2]],
            [matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0],
             matrix[0][1]*matrix[2][0] - matrix[0][0]*matrix[2][1],
             matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]]]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def scalar_multiply(matrix, scalar):
    return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return "The matrix is not invertible."
    else:
        adjugate = transpose(cofactor(matrix))
        return scalar_multiply(adjugate, 1/det)

# Define the 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Calculate the inverse
inverse_matrix = inverse(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nInverse Matrix:")
if type(inverse_matrix) == str:
    print(inverse_matrix)
else:
    for row in inverse_matrix:
        print(row)