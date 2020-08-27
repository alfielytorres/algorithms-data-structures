'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '28880552' #write your student number as a string
    student_email = 'ator0002' + '@student.monash.edu' #write your student email
    name = 'Alfonso Luigi Torres' #write your name as it appears on Moodle
    return str(student_number), student_email, name


###Task 1
def partial_sum(start, end, step):
    '''
    Input: partial sum(3, 13, 2)
    Process: 3 + 5 + 7 + 9 + 11 + 13 = 48
    Output: 48
    '''
    end =  end+1 if end > 0 else end-1

    sum = 0 # candidate answer
    for i in range(start, end,step):
        sum +=i
    return sum
    """
    >>> partial_sum(3, 13, 2)
    48
    >>> partial_sum(8, 290, 5)
    8436
    >>> partial_sum(-5, 30, 3)
    138
    >>> partial_sum(-10, -100, -5)
    -1045
    """
    pass

###Task 2
def reverse_strings(my_list):
    reversed_string=""
    for word in my_list[::-1]:
        reversed_string+=word
    return reversed_string
    """
    >>> reverse_strings([])
    ''
    >>> reverse_strings(['my','little','pony'])
    'ponylittlemy'
    >>> reverse_strings(['00','11','22','33'])
    '33221100'
    """
    pass

def complete(my_list):
    '''
    Input: complete([12, 15, 19])
    Output: [12, 13, 14, 15, 16, 17, 18, 19]
    '''
    current = 0 # current position 
    while current !=len(my_list)-1:
        if my_list[current]+1 != my_list[current+1]: # check if current +1 == to next integer in existing array
            my_list.insert(current+1,my_list[current]+1) # if not then insert
        current +=1
    return my_list

    """
    >>> complete([12, 15, 19])
    [12, 13, 14, 15, 16, 17, 18, 19]
    >>> complete([2, 3])
    [2, 3]
    >>> complete([1])
    [1]
    >>> complete([-5, 0, 5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    """
    pass

###Task 3
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

    """
    >>> addition_table([2, 5, -3, 7])
    [[3, 6, -2, 8], [4, 7, -1, 9], [5, 8, 0, 10]]
    >>> addition_table([1])
    [[2], [3], [4]]
    >>> addition_table([-2, -5, -9, -12, -23])
    [[-1, -4, -8, -11, -22], [0, -3, -7, -10, -21], [1, -2, -6, -9, -20]]
    """
    pass

###Task 4
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
    """
    >>> remove_outliers([[0, 4], [2, 4], [-1, 3]])
    [[0, 1.5], [2, 1.5], [1.5, 3]]
    """
    pass


###Task 5 - FIT1053
import math 
def primes_in_range(start, stop):
    '''
    Input: start number of the list and end number of the list
    Output: prime numbers in between
    '''
    # Create list of True values  
    boolean_list = [True for index in range(0, stop+1)]
    boolean_list[0]=False
    boolean_list[1]=False
    # Remove elements that are composite 
    prime = 2
    while not math.pow(prime,2) > stop:
        print('Running...')
        if boolean_list[prime]==True:
            # check numbers between the current one and the end of the stop 
            for j in range(prime+1, stop+1):
                if j%prime==0:
                    boolean_list[j]=False
        prime+=1

    return [index for index in range(start,stop+1) if boolean_list[index]==True]  



    """
    >>> primes_in_range(35, 100)
    [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> primes_in_range(211, 263)
    [211, 223, 227, 229, 233, 239, 241, 251, 257, 263]
    >>> primes_in_range(35400, 35500)
    [35401, 35407, 35419, 35423, 35437, 35447, 35449, 35461, 35491]
    >>> primes_in_range(51854787, 51854830)
    [51854801, 51854807, 51854809, 51854821, 51854827]
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)