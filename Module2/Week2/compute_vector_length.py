import numpy as np

def compute_vector_length(vector):
    result = np.sqrt(np.sum(np.power(vector,2)))
    return result 
