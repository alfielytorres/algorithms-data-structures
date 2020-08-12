from random import random
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
def calculate(x,y,operator):
    ret = 0 
    if operator == '+':
        ret = x + y
    elif operator == '-':
        ret = x -y 
    elif operator == 'x':
        ret = x*y 
    elif operator == '/':
        ret = x/y
    else:
        ret = 'That operator is not supported'
    return ret
    
    """
    >>> calculate(3, 5, '+')
    8
    >>> calculate(3, 5, '-')
    -2
    >>> calculate(3, 5, 'x')
    15
    >>> calculate(3, 5, '/')
    0.6
    """       
    pass


###Task 2
def is_leap_year(year):
    if year % 4== 0 and (year % 100 != 0 or year % 400 == 0 ):
        return True
    return False

    """
    >>> is_leap_year(1)
    False
    >>> is_leap_year(100)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2040)
    True
    >>> is_leap_year(2100)
    False
    """
    pass


import datetime

def leap_year_answer(year):

    if year <= datetime.date.today().year:
        if is_leap_year(year):
            return  "Year {} was a leap year".format(year)
        else:
            return  "Year {} was not a leap year".format(year)
    else:
        if is_leap_year(year):
            return  "Year {} will be a leap year".format(year)
        else:
            return  "Year {} will not be a leap year".format(year)
    """
    >>> leap_year_answer(1)
    'Year 1 was not a leap year'
    >>> leap_year_answer(100)
    'Year 100 was not a leap year'
    >>> leap_year_answer(2000)
    'Year 2000 was a leap year'
    >>> leap_year_answer(2019)
    'Year 2019 was not a leap year'
    >>> leap_year_answer(2040)
    'Year 2040 will be a leap year'
    >>> leap_year_answer(2100)
    'Year 2100 will not be a leap year'
    """
    pass

###Task 3
def next_triangular_number(num):
    sum = 0 
    n = 1
    while(sum < num):
        sum+=n # off by one so if next trianglular number of 5 is 6 then we add before we hit it
        n+=1
    return sum
    """
    >>> next_triangular_number(5)
    6
    >>> next_triangular_number(25)
    28
    >>> next_triangular_number(40)
    45
    >>> next_triangular_number(2000)
    2016
    """
    pass

###Task 4
def add(numbers):
    if len(numbers) < 1:
        return 0
    else: 
        index = 1
        sum = 0 
        while(index < len(numbers)):
            sum+=numbers[index]
            index+=2
        return sum
    """
    >>> add([])
    0
    >>> add([25])
    0
    >>> add([92, 61, 97, 10, -39])
    71
    >>> add([-24, -25, -33, 32, -81, -58, 28, -4, -30, -69, 44, -41])
    -165
    """
    pass

def flip(binary_string):
    flipped_string = []
    for bit in binary_string:
        if bit == '1':
            flipped_string.append('0')
        else:
            flipped_string.append('1')
    return "".join(flipped_string)
    """
    >>> flip('')
    ''
    >>> flip('01')
    '10'
    >>> flip('101')
    '010'
    >>> flip('001011111111')
    '110100000000'
    """
    pass

###Task 5 - FIT1053 Only
def n_even_fibonacci(n):
    list = [0, 1]
    even_list = [0]
    
    i = 1 # nth term 
    number = 1 # this is used to go through the list
    
    if n == 0:
        return []

    while len(even_list) < n:
        next = list[number]+list[number-1]
        list.append(next)
        number+=1
        i+=1
        if next %2 ==0: # only add if it is even
            even_list.append(next)

    return even_list
    """
    >>> n_even_fibonacci(0)
    []
    >>> n_even_fibonacci(5)
    [0, 2, 8, 34, 144]
    >>> n_even_fibonacci(10)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]
    >>> n_even_fibonacci(12)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
    """
    pass


###Challenge - Optional
from math import e
def estimate_e(error):
    """
    <WRITE YOUR ANALYSIS HERE>
    >>> estimate_e(1)
    2.0
    >>> estimate_e(0.1)
    2.6666666666666665
    >>> estimate_e(0.01)
    2.708333333333333
    >>> estimate_e(0.005)
    2.7166666666666663
    >>> estimate_e(0.001)
    2.7180555555555554
    >>> estimate_e(0.0000000001)
    2.7182818284467594
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
