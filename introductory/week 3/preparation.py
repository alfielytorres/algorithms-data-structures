def hours_to_legal_limit(bal):
    '''
    input: blood alcohol level (in decimals)
    process: decreases BAL by 15% for each hour elapsed
    output: hours it takes to reach BAL < 5% 
    '''
    h = 0 # candidate solution 
    while(bal>=.05): # exits if bal < 0.05
        h = h +1 
        bal=bal-0.15 # iteration variable
    return h 

answer = hours_to_legal_limit(2)
print(answer)


'''
In our case, BAL is not definite. As such, we can't have a set number of iterations 
(one that a for loop provides) to go through the loop. 
Using a while loop allows us go through the loop an unknown amount of times 
until the condition is reached -- in our case bal <0.05.'''