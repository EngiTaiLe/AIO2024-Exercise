# Function factorial 
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result 

# Function sin
def approx_sin(x,n=10):
    result = 0
    for i in range(0,n):
        result += (pow(-1,i))*(pow(x,2*i+1))/factorial(2*i+1)
    return result 

# Function cos 
def approx_cos(x,n=10):
    result = 0
    for i in range(0,n):
        result += (pow(-1,i))*(pow(x,2*i))/factorial(2*i)
    return result 

# Function sinh 
def approx_sinh(x,n=10):
    result = 0
    for i in range(0,n):
        result += (pow(x,2*i+1))/factorial(2*i+1)
    return result 

# Function cosh 
def approx_cosh(x,n=10):
    result = 0
    for i in range(0,n):
        result += (pow(x,2*i))/factorial(2*i)
    return result 

