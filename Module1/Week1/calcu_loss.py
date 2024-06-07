import math
from activate_function import is_number

# Function MAE
def mae(pred,target):
    return sum(abs(pred-target))/len(pred) 

# Function MSE
def mse(pred,target):
    return sum(pow(pred-target,2))/len(pred) 

# Function RMSE 
def rmse(pred,target):
    return math.sqrt(sum(pow(pred-target,2))/len(pred)) 

# Combined Functions 
import numpy as np
def compute_loss(n_samples):
    loss_name = input("Enter the loss name (RMSE|MSE|MAE): ")
    if not is_number(n_samples):
        print("number of samples must be an integer number")
        return
    preds = np.arange(0,n_samples)
    targets = np.arange(0,n_samples)
    n_min = 0
    n_max = 10
    size = 1
    for i in range(n_samples):
        pred = np.random.uniform(n_min,n_max,size)
        target = np.random.uniform(n_min,n_max,size)
        preds[i] = pred
        targets[i] = target
        if loss_name == 'RMSE':
            loss = rmse(pred,target)
        elif loss_name == 'MSE':
            loss = mse(pred,target)
        else:
            loss = mae(pred,target)
        print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')
    if loss_name == 'RMSE':
        final_loss = rmse(preds,targets)
    elif loss_name == 'MSE':
        final_loss = mse(preds,targets)
    else:
        final_loss = mae(preds,targets)
    print(f"final {loss_name}: {final_loss}")