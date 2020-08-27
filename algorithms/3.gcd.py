import time

# Linear Case 
def gcd_linear(x,y):
    """
    input: such that integers not n==m==0
    ourput: GCD of m and n
    """
    start_time = time.time()

    n= min(x,y)
    m = max(x,y)
    
    if n == 0:  
        return m

    while x%n !=0 or y%n!=0:
        n=n-1
        print(n)
    print("Runtime -  %s seconds" % (time.time() - start_time))
    return n

# Euclid
'''
Better for larger worse case scenarios
'''
def gcd_euclid(m,n):
    start_time = time.time()
    """
    input: such that integers not n==m==0
    ourput: GCD of m and n
    """


    while n!=0:
        r = m%n
        m= n
        n = r 

        '''
         Given: m=4 n=12 

         r = 4 mod 12 = 4 
         m = 12 
         n = 4 

         r = 12 mod 4 = 0
         m = 4
         n = 0 

         return m=4 
       
         Given: m=12 n=4 

         r = 12 mod 4= 0
         m = 4
         n = 0

         return m=4 
         '''

       

        print(r)
    print("Runtime -  %s seconds" % (time.time() - start_time))
    return m

x = 2020931092301930210320190319023
y=4123121
print("Linear case =========")
print("gcd_linear({},{}) => {} ".format(x, y, gcd_linear(x,y)))
print('\n')



print("Euclid case =========")
print("gcd_euclid({},{}) => {} ".format(x, y, gcd_euclid(x,y)))
