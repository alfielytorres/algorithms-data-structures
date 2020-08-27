def gcd(x,y):

    if x> y:
        remainder = x%y  
        while remainder != 0:
            x = y
            y = remainder
            remainder = x%y  
        return y
    else:
        remainder = y%x  
        while remainder != 0:
            y = x
            x = remainder
            remainder = y%x 
        return x

print("gcd({},{}) => {} ".format(3, 29, gcd(3,29)))
print("gcd({},{}) => {} ".format(8, 4, gcd(8,4)))
print("gcd({},{}) => {} ".format(4, 8, gcd(4,8)))
print("gcd({},{}) => {} ".format(18, 6, gcd(18,6)))