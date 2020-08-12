def collatz(n):
    list = []
    num = n 
    while(num!=1): # assuming that it will eventually become 1
        if num%2==0:
            num = num/2
            list.append(num)
        else:
            num = num*3+1
            list.append(num)
    print(num) # print num
    return list


print(collatz(71293791)) # print list