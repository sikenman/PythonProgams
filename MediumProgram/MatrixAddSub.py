import numpy as np

# Matrix addition
def matrix_addition(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)


# Example matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Perform matrix addition
addition_result = matrix_addition(matrix1, matrix2)

# Perform matrix subtraction
subtraction_result = matrix_subtraction(matrix1, matrix2)

# Print the results
print("Matrix Addition:")
print(addition_result)
print()

print("Matrix Subtraction:")
print(subtraction_result)


