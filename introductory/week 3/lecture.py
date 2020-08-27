def quantity_eaten(food, eaten_foods, eaten_quantities):
    res = 0
    for i in range(0,len(eaten_foods)):
        if eaten_foods[i]==food:
            res += eaten_quantities[i]
    return res

eaten = ['beef','potato', 'broccoli', 'apple', 'potato', 'apple']
quantities = [300, 300, 200, 100, 250, 100]

print(quantity_eaten('potato',eaten,quantities))