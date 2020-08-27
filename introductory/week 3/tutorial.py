
# DEEP COPY =======
import copy 
def make_my_list(N):
    inner_list = [None]*N #create inner_list with room for N elements 
    outer_list = [None]*N #create outer_list with room for N elements
    for i in range(0, N):
        inner_list[i] = 0
    for i in range(0, N):
        outer_list[i] = copy.deepcopy(inner_list)
        # outer_list[i] = inner_list
    for i in range(0, N):
        for j in range(0, N):
            outer_list[i][j] = N*i + j
    print(outer_list)
# make_my_list(5)

'''
FIRST ====

Code: 
 for i in range(0, N):
        inner_list[i] = 0

Explanation:

Initialise each element in the list from None to 0 

SECOND ====

Code: 
for i in range(0, N):
        outer_list[i] = inner_list

Explanation:

Initialise the outer list with the inner loop for N 
amount of times in our case 4 times

THIRD ====

Code: 
for i in range(0, N):
        for j in range(0, N):
            outer_list[i][j] = N*i + j

OUTER =====

Explanation:
This just allows you to go through each 
array in the outer list 

INNER =====
Expectation:
outer_list[i][j] = N*i + j
outer_list[0][0] = 4*0 + 0 =0
outer_list[0][1] = 4*0 + 1 =1
outer_list[0][2] = 4*0 + 2 =2
outer_list[0][3] = 4*0 + 3 =3

outer_list[1][0] = 4*1 + 0 =4
outer_list[1][1] = 4*1 + 1 =5
outer_list[1][2] = 4*1 + 2 =6
outer_list[1][3] = 4*1 + 3 =7

outer_list[2][0] = 4*2 + 0 =8
outer_list[2][1] = 4*2 + 1 =9
outer_list[2][2] = 4*2 + 2 =10
outer_list[2][3] = 4*2 + 3 =11

outer_list[3][0] = 4*3 + 0 =12
outer_list[3][1] = 4*3 + 1 =13
outer_list[3][2] = 4*3 + 2 =14
outer_list[3][3] = 4*3 + 3 =15

Reality:
The contents of each array is all [12,13,14,15]
This may be due to a referencing issue
Using deepcopy should fix the issue

'''

# MULTIPLICATION TABLE ======

import copy

def maths_table(x,operator):
    outer_list = [None]*x
    inner_list = [None]*x
    for i in range(0,len(inner_list)):
        inner_list[i] = 0
    for i in range(0,len(outer_list)):
        outer_list[i] = copy.deepcopy(inner_list)
    
    for i in range(0,x):
        for o in range(0,x):
            outer_list[i][o]=eval("{}{}{}".format((o+1),operator,(i+1)))
            
    print(inner_list)
    print(outer_list)
maths_table(3,'*')

