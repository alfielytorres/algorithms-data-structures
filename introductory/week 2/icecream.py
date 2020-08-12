# def icecreams(x, summer):
#     # during summer you need 10 icecreams
#     if summer:
#         return 10-x

#     # if it is not summer you need only 2 
#     if 10-x > 0:
#         return 0 # > 2 is too much 
#     elif 2-x > 0:
#         return 2-x # <2 is too little


# print(icecreams(3 ,False))

def rounding(n):
    remainder = n%10
    num = n-remainder
    if remainder < 5:
        return num
    elif remainder > 5:
        return num + 10
    else:
        if num//10%2 == 0:
            return num + 10
        else:
            return num

    
print(rounding(26))






rounding(21) # 20 

rounding(25) # 20 

rounding(27) #30


