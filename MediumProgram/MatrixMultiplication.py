import numpy as np

# Matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Example matrices
matrix1 = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

matrix2 = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

# Perform matrix addition
result = matrix_multiplication(matrix1, matrix2)

# Print multiplication result
print("Matrix Multiplication:")
print(result)
print()

'''Source: ChatGPT
NumPy uses the highly optimized BLAS (Basic Linear Algebra Subprograms) and LAPACK (Linear Algebra Package) 
libraries to perform matrix multiplication efficiently. These libraries provide implementations of various algorithms 
for matrix multiplication, such as the classical matrix multiplication algorithm, Strassen's algorithm for large matrices, 
and other optimized algorithms for specific matrix sizes.

By default, NumPy uses the BLAS and LAPACK libraries provided by the system or the ones that were used during the NumPy 
installation. These libraries are often highly optimized and may utilize hardware-specific optimizations, such as 
multithreading or vectorization, to achieve faster matrix multiplication.

The specific algorithm used by NumPy for matrix multiplication depends on the underlying BLAS and LAPACK implementation 
and the characteristics of the matrices being multiplied, such as their sizes and the hardware on which NumPy is running. 
NumPy's goal is to provide efficient matrix operations, and the choice of the algorithm is made to achieve the best 
performance for a wide range of scenarios.'''