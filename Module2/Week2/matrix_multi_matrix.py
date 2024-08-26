import numpy as np

def matrix_multi_matrix(matrix1,matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        return "The length of the matrix1's column is not equal to the length of the matrix2's row"
    result = matrix1@matrix2
    return result 

