def partial_sum(start, end, step):
    '''
    Input: partial sum(3, 13, 2)
    Process: 3 + 5 + 7 + 9 + 11 + 13 = 48
    Output: 48
    '''
    sum = 0 # candidate answer
    
    end =  end+1 if end > 0 else end-1
    
    for i in range(start, end,step):
        sum +=i
    return sum
answer= partial_sum(-10, -100, -5) #-1045
# print(answer)




def complete(my_list):
    
    '''
    Input: complete([12, 15, 19])
    Output: [12, 13, 14, 15, 16, 17, 18, 19]
    '''
    current = 0 
    while current !=len(my_list)-1:
        if my_list[current]+1 != my_list[current+1]:
            my_list.insert(current+1,my_list[current]+1)
        current +=1
    return my_list
answer= complete([12, 16, 50])
# print(answer)

import copy 
def addition_table(numbers):

    '''
    Input: addition_table([2, 5, -3, 7])
    Output: [[3, 6, -2, 8], [4, 7, -1, 9], [5, 8, 0, 10]]
    '''

    outer_list = [None,None,None]

    for i in range(0,len(outer_list)):
        outer_list[i] = copy.deepcopy(numbers)


    for i in range(0,len(outer_list)):
        for j in range(0, len(outer_list[i])):
            outer_list[i][j] = outer_list[i][j]+(i+1)
    return outer_list


# answer = addition_table([1])
# print(answer)


def remove_outliers(table):
    '''
    Input: remove_outliers([[0, 4], [2, 4], [-1, 3]])
    Output: [[0, 1.5], [2, 1.5], [1.5, 3]]
    '''
    min = 0
    max  = 0 

    min = table[0][0]
    max = table[0][0]

    # find min and max 

    for i in range(0,len(table)): 
        for j in range(0,len(table[i])):
            if table[i][j] > max: 
                max = table[i][j]
            if table[i][j] < min: 
                min = table[i][j]

    # calculate mid point 
    mid_point= (min+max)/2
    print(mid_point)

    # replace 
    for i in range(0,len(table)): 
        for j in range(0,len(table[i])):
            if table[i][j] == min or table[i][j]==max:
                table[i][j] = mid_point


    return table

# answer = remove_outliers([[0, 4], [2, 4], [-1, 3]])
# print(answer)

import math 

def primes_in_range(start, stop):
    '''
    Input: start number of the list and end number of the list
    Output: prime numbers in between
    '''
    # Tips - Miller Robbin Algorithm

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

