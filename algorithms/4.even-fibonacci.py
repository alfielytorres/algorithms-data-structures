def n_even_fibonacci(n):
    '''
    input: any number > 0 
    output: returns a n elements of list of even fibonacci numbers 
    '''
    list = [0, 1] # Normal fibonacci numbers
    even_list = [0] # Candidate solution 
    
    i = 1 # iteration varaible 
    number = 1 # this is used to go through the list
    
    if n == 0:
        return [] # if asked for 0 length return empty array 

    while len(even_list) < n: # Exists if desired length of even fibonacci numbers is reached

        # Get next fibonacci number next 
        next = list[number]+list[number-1]
        list.append(next)

        # increment pattern 
        number+=1
        i+=1

        # Add next to even fibonacci list if the number being added is even 
        if next %2 ==0: 
            even_list.append(next)

    return even_list
  
n_even_fibonacci(0)
#[]
n_even_fibonacci(5)
#[0, 2, 8, 34, 144]