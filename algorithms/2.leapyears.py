def is_leap_year(number):
    response = 'not leap'
    if number % 4 == 0 and (number % 100 != 0 or number % 400 ==0): 
        response='leap'
    print(response)

is_leap_year(2000)
is_leap_year(1900)
is_leap_year(2016)