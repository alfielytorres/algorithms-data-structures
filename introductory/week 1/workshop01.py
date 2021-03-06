# Task 1: Maths
# Replace the '' in each line with one of [+, -, *, //, %, /, **]
# to create a statement that evaluates to True. 
# For example, (a) can be changed to:
# 0 == (x + x) % x

# We start by assigning values to variables x and y
x = 3
y = 5

# a
a= 0 == (x + x) % x 
# b
b = 4 == x ** (y % x) -y 
# c
c = 7.5 == (x*y) / (y - x)

print("{} {} {}".format(a,b,c))

# Task 2: Booleans
# Replace the '' in each line with one of [==, !=, <=, >=, <, >]
# to create a statement that evaluates to True.
# For example, (a) can be changed to:
# 10 <= 10

#a
a= 10 == 10
#b
b = 10%4 > 12//7
#c
c = 3**2 > 10-3
print("{} {} {}".format(a,b,c))

# Task 3: Temperature Conversion
# Replace the '' with a numerical expression that converts the
# temperature in Fahrenheit (temp_f) to the temperature in Celsius.
# For instance, if Celsius were 3 degrees more than Fahrenheit (incorrect!),
# the implementation would be:
# temp_c = temp_f + 3

temp_f = 3
temp_c = (temp_f-32)*(5/9)
print("{}°F -> {}°C".format(temp_f,temp_c))

# Task 4: Name Factoids
# Replace the '' with an expression that evaluates to a string with
# the following pattern:
# factoids = '<name> has <number of letters>. It starts with <letter> and ends with <letter>.'
# For example, if you do not change the given name, factoids would
# evaluate to:
#     'Jane has 4 letters. It starts with J and ends with e.'
# NOTE: You must implement factoids so that it would work for any value
#       assigned to name.

name = 'Alfie'

factoids = "{} has {} letters. It starts with {} and ends with {}.".format(name, len(name),name[0],name[-1])

print(factoids)


# Task 5: Coin Flip
# THIS TASK IS ONLY FOR FIT1053 STUDENTS

# Replace the '' with any necessary import statements
import random

def flip(bias):
    chance = bias > random.random()
    return 'Coin has bias of' + str(bias) + "value of heads" + str(chance)
