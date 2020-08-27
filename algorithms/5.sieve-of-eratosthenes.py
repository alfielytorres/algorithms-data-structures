import math 

def primes_in_range(start, stop):
    '''
    Input: start number of the list and end number of the list
    Output: prime numbers in between
    '''
    # Better Algorithms -  Miller-Rabin Primality Test

    # Create list of True values  
    boolean_list = [True for index in range(0, stop+1)]
    boolean_list[0]=False
    boolean_list[1]=False
    # Remove elements that are composite 
    prime = 2
    while not math.pow(prime,2) > stop:
        
        if boolean_list[prime]==True:
            # check numbers between the current one and the end of the stop 
            for j in range(prime+1, stop+1):
                if j%prime==0:
                    boolean_list[j]=False
        print('running..',prime)
        prime+=1

    return [index for index in range(start,stop+1) if boolean_list[index]==True] 

answer =  primes_in_range(35,100)
# [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print('primes_in_range( 100)',answer,'\n')

answer =  primes_in_range(211, 263)
# [211, 223, 227, 229, 233, 239, 241, 251, 257, 263]
print('primes_in_range(211, 263)',answer,'\n')

answer =  primes_in_range(35400, 35500)
# [35401, 35407, 35419, 35423, 35437, 35447, 35449, 35461, 35491]
print('primes_in_range(35400, 35500)',answer,'\n')

answer =  primes_in_range(51854787, 51854830)
# [51854801, 51854807, 51854809, 51854821, 51854827]
print('primes_in_range(51854787, 51854830)',answer,'\n')

