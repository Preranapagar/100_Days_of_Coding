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

# Example usage:
A = [[1, 2],
     [3, 4]]

A_inv = inverse_matrix(A)

print("Original matrix A:")
for row in A:
    print(row)

print("\nInverse of matrix A:")
for row in A_inv:
    print(row)
