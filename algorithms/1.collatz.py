def next(n):
    '''
    Input: any number n that is greater than 0
    Output: returns the next collatz number
    '''
    num = n 
    if num%2==0:  
        num = num/2
          
    else:   
        num = num*3+1
    
    return num

def collatz(n):
    '''
    Input: any number greater than 0 
    Output: returns a list of numbers that num was evaluated to before it reached 1
    '''
    list = []
    num = n
    if num <1:
        print('Number must be greater than 0')
        return

    while(num!=1):
        num = next(num)
        list.append(num)
    
    print(list)
    return


collatz(20)