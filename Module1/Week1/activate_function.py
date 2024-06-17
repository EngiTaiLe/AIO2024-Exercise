import math

# Function sigmoid 
def sigmoid(x):
    return 1/(1+math.exp(-x))

# Function relu 
def relu(x):
    y = 0
    if x > 0:
        y = x
    return y 

# Function elu 
def elu(x,alpha=0.01):
    y = x
    if x <= 0:
        y = alpha*(math.exp(x)-1)
    return y 

# Function check number 
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Combined Functions
def fx(x):
    if not is_number(x):
        print('x must be a number')
        return
    act_fun = input("Input activation function (sigmoid|relu|elu):")
    if not act_fun in ('sigmoid','relu','elu'):
        print(f'{act_fun} is not supported')
        return
    x = float(x)
    if act_fun == 'sigmoid':
        result = sigmoid(x)
    elif act_fun == 'relu':
        result = relu(x)
    else:
        result = elu(x)
    return result

print(fx(-2))