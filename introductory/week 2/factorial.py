# normal 

def factorial(x):
    product = 1
    if x == 0:
        return product
    elif x > 0: 
        for i in range(1, x+1):
            product*=i

    return product

print(factorial(5))


# recursively 

def recursive_factorial(x):
    product = 1
    # base case
    if x == 0:
        return product
    # recursive case
    else:
        return x*recursive_factorial(x-1)

print(recursive_factorial(5))


