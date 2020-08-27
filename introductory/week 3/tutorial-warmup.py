def adding(x):
    '''
    input: any number (e.g. 10) 
    output: sum of all even numbers <= x (e.g. 30)
    '''
    sum = 0 # candidate solution 
    for i in range(x+1)[::-2]: # step negative -2 
        sum+=i
    print(sum)
    return sum

# adding(10)


def double(x): 
    '''
    input: any integer x 
    output: number of times x must be doubled to reach an number > 100
    '''
    n = 0 # candidate solution

    while(x<100):
        x = 2*x
        n+=1
    print(n)
    return n

# double(5)

# Loop
'''
print(list(range(2,11,3)))
print(list(range(0,-3,-1)))
'''

# Loops (Continued)
'''

Problem: There is an isse with this code 

my_list = [3, 7, 4, 9, 12, 2]
for num in my_list:
    num = num//2

Explanation: we are trying to modify the list but 
that won't be possible if we are doing it like this

'''
def loop_one():
    my_list = [3, 7, 4, 9, 12, 2]
    for num in range(len(my_list)):
        my_list[num] = my_list[num]//2
    print(my_list)

# loop_one()

'''

Problem: There is an isse with this code 

my_string = `hare paws wall tuba draw'
for i in range(len(my_string)):
    if my_string[i] == `a':
        my_string[i] = `e'

Explanation: requires us to make it into a list 
'''
def loop_two():
    my_string = list("hare paws wall tuba draw")
    for i in range(len(my_string)):
        if my_string[i] == 'a':
            my_string[i] = 'e'
    my_string="".join(my_string)
    print(my_string)

# loop_two()

# List 
'''
What does x yield? 

my_list = [`1045', `1008', `2004', `2099']
x = my_list[1:3][-1]
'''
def list_one():
    my_list = ['1045', '1008', '2004', '2099']
    x = my_list[1:3][-1]
    print(x) # Expected: 
    return x 

# list_one()


'''
What does x yield? 

x = [`monkey', `tiger', `lion', `mouse']
animals = x
animals[3] = `meerkat'
'''
def list_two():
    x = ['monkey', 'tiger', 'lion', 'mouse']
    animals = x
    animals[3] = 'meerkat'
    print(x) # Expected: ['monkey', 'tiger', 'lion', 'meerkat']
    return x 

# list_two()

def nested_loop():
    table =[]
    for i in range(3):
        table+=[[1,2,3]]
    print(table)
    
# nested_loop()