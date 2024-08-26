import numpy as np

def compute_dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return "The length of vector1 is not equal to the length of vector2"
    result = np.sum(np.multiply(vector1,vector2))
    return result 

