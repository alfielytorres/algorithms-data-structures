def binary_to_decimal(binary):
    decimal = 0
    for power, nth_term in enumerate(reversed(str(binary))):
        if nth_term == '1':
            decimal = decimal + 2**power

        # For visuals 
        print("{}; {} level; {}".format(nth_term, power, 2**power))
    return(decimal)

answer = binary_to_decimal(100101)
print(answer)