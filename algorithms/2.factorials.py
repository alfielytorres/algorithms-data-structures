# Non-recursive
def factorial(x):
    '''
    Input: Any number
    Output: Returns the sum of the numbers less than the number given
    '''
    product = 1
    if x == 0:
        return product
    elif x > 0: 
        for i in range(1, x+1):
            product*=i

    return product

print(factorial(5))


# Recursive 
def recursive_factorial(x):
    '''
    Input: Any number
    Output: Returns the sum of the numbers less than the number given
    '''
    product = 1
    # base case
    if x == 0:
        return product
    # recursive step
    else:
        return x*recursive_factorial(x-1)

print(recursive_factorial(5))


