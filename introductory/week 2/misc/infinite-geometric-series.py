
# general 
def infinite_geometric(a, r):
    return a*(1/(1-r))

# print(infinite_geometric(1,1/2))


# more definite 
def infinite_geometric_definite(a, r):
    sum =0
    exp = 0
    term = r
    while term > 1e-10:
        term = r**(exp) # r^0 + r^1 ... + r^n-1 + r^n
        sum += a*term# ar^0 + ar^1 + ... + ar^n-1 + ar^n 
        exp +=1 # increment exponent
    return sum

print(infinite_geometric_definite(2,1/4))
