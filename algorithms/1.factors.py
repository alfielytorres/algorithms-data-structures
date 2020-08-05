# Implementation of GCD 


# is prime we check if the number is divisible by itself and 1
def is_prime(number):
    # Check (1,7) or [2, 6]
    i = 2
    while i < number:
        # check if remainder is 0
        if number%i==0: # if 0 then we do not have a prime
            return False # program ends (Not a Prime)
        i=i+1

    return True # passes all tests and returns True (Prime)

def factorize(number):
    factors = []
    divisor = 2
    while number > 1:
        if is_prime(divisor) and number%divisor==0:
            factors.append(divisor)
            # we want to keep this divisor 
            # to check if we can divide it 
             # again with the same divisor 
            number=number/divisor
        else:
            divisor += 1
    print(factors)

factorize(24)