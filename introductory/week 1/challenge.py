# What does these expressions yield 
# int(False or True)*2**2**(14//5*2%3+2)+2

value = int(False or True)*2**2**(14//5*2%3+2)+2 # 258
print(value)

value = int(False) # 0
print(value)

value = int(True) # 1
print(value)

value = int(False or True) #1 
print(value) 