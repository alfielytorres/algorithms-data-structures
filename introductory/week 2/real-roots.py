import math 

def find_no_roots(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta == 0:
        return 1
    elif delta > 0:
        return 2 
    else: 
        return 0
    
def real_roots(a, b, c):
    no_of_roots = find_no_roots(a,b,c)
    list = []

    if no_of_roots == 1:
        root = (-b+math.sqrt((b**2-4*a*c)))/(2*a)
        list.append(root)
    elif no_of_roots == 2:
        root_one = (-b+math.sqrt((b**2-4*a*c)))/(2*a)
        root_two = (-b-math.sqrt((b**2-4*a*c)))/(2*a)
        list.append(root_one)
        list.append(root_two)
    return list

print(real_roots(2,-1.1,-3))