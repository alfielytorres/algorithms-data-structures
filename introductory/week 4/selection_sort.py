items= [14,13,12,11,10]
def min_index(list):
    '''
    accepts: list of length n > 0 of comparable elements 
    returns: index k in range(n) such that 
    for all j in range(n), lst[k] <= lst[j]
    '''
    return list.index(min(list))

def selection_sort(list):
    """
    accepts : list list of length n of comp. elements 
    post-cond: list has same elements as on call but 
    for all i in range (1,n), list[i-1] <= list[i]
    """
    for i in range(len(list)):
        j= min_index(list[i:])+i
        print(j)
        list[i], list[j] = list[j], list[i]
    return list 
print (selection_sort(items))