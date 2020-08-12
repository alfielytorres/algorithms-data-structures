def fibonacci(n):
    list = [0, 1]
    even_list = []
    
    i = 1 # nth term 
    number = 1 # this is used to go through the list


    while len(even_list) < n:
        next = list[number]+list[number-1]
        list.append(next)
        number+=1
        i+=1
        if next %2 ==0: # only add if it is even
            even_list.append(next)

    return even_list


print(fibonacci(8))
