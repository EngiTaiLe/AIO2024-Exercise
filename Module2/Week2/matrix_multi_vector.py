import numpy as np

def matrix_multi_vector(matrix, vector):
    if matrix.shape[1] != len(vector):
        return "The length of matrix's column is not equal to the length of vector!"
    result = matrix@vector 
    return result 

