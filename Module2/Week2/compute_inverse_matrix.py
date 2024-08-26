import numpy as np

def inverse_matrix(matrix):
    if matrix.shape[1] != matrix.shape[0]:
        return "The matrix is not square!"
    if np.linalg.det(matrix) == 0:
        return "The matrix is uninvertible!"
    result = np.linalg.inv(matrix)
    return result 
