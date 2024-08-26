import numpy as np

def compute_cosine(v1,v2):
    if len(v1) != len(v2):
        return "The length of vector1 is not equal to the length of vector2"
    result = (v1@v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return result 
