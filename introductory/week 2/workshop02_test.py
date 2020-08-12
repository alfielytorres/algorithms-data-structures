#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False



#############################################################################

#Import statements
from workshop02 import *
import workshop02
from math import ceil
from contextlib import redirect_stdout
import io
from collections.abc import Iterable

def fail_output(s):
    print("{}".format("="*60))
    print(s)
    print("{}".format("="*60))

def run_cases(module, cases, output_function=None, verbose=SHOW_ALL_INFO, marking=False):
    cases_failed = 0
    if marking == True: verbose = False
    for case in cases:
        if verbose:
            print("checking: {}({})=={}".format(case[0], case[1], case[2]))
        method = getattr(module, case[0], None)
        if not method:
            if not marking:
                print("...fail (method not found)")
            return 0,len(cases)
        try:
            f = io.StringIO()
            with redirect_stdout(f):
                #for when there is more than 1 arg
                if isinstance(case[1], tuple):
                    output = method(*case[1])
                else:
                    output = method(case[1])
        except Exception as e:
            if not marking:
                print(e)
                fail_output(f"...fail (exception thrown)")
            cases_failed += 1
            continue
        if output == case[2] or f.getvalue() == case[2]:
            if verbose:
                print("...passed")
        else:
            if output_function and output_function(output) == output_function(case[2]):
                    if verbose and not marking:
                        print("...passed after processing output")
            else:
                if not marking:
                    fail_output(f"...fail (incorrect output)\ngiven output:\t{output} \ncorrect output:\t{case[2]}")
                cases_failed += 1
    return (len(cases)-cases_failed, len(cases))

def evaluate_module(module, tests, mark=2, marking=False):
    if not marking:
        print(f"Evaluating module: {module.__name__}")
    res = 0
    max = 0 #max mark
    t_passed = 0 #percentage of tests passed
    total_tests = 0
    f_passed = 0 #number of functions with 0 errors
    for test in tests:
        max = max + test[1]
        if not marking:
            print("{}".format("#"*60))
            print()
            print(f"Testing function {test[0][0][0]}:")
        cases_passed, total_cases = run_cases(module, test[0], test[2], marking=marking)
        res += round((cases_passed/total_cases)*test[1],4) #scale res by marks function is worth
        t_passed += cases_passed
        total_tests += total_cases
        if cases_passed==total_cases: f_passed += 1
        if not marking:
            if cases_passed==total_cases:
                print("All cases passed")
            else:
                print("Some cases failed")
            print()
    if not marking:
        print("{}".format("#"*60))
        print()

    #Scale and print Results
    scaled = 0

    if res/max>=0.95 and f_passed > 1: scaled = 2
    elif res/max>=0.65 and f_passed > 1: scaled = 1.5
    elif f_passed >= 1: scaled = 1
    elif res/max>0: scaled = 0.5
    if not marking:
        print(f"Percentage of tests passed: {round(t_passed/total_tests*100,2)}%")
        print(f"Scaled percentage of tests passed: {round(res/max*100,2)}%")
        print(f"Total correct functions: {f_passed}/{len(tests)}")
        print()
        print(f"Total marks: {scaled}/{mark}")
    return scaled

#############################################################################


#Task 1

CALCULATE = \
  [('calculate', (3, 5, '+'), 8),
   ('calculate', (3, 5, '-'), -2),
   ('calculate', (3, 5, 'x'), 15),
   ('calculate', (3, 5, '/'), 0.6)]

#Task 2
IS_LEAP_YEAR = \
  [('is_leap_year', (1), False),
   ('is_leap_year', (100), False),
   ('is_leap_year', (2000), True),
   ('is_leap_year', (2019), False),
   ('is_leap_year', (2040), True),
   ('is_leap_year', (2100), False)]

LEAP_YEAR_ANSWER = \
  [('leap_year_answer', (1), 'Year 1 was not a leap year'),
   ('leap_year_answer', (100), 'Year 100 was not a leap year'),
   ('leap_year_answer', (2000), 'Year 2000 was a leap year'),
   ('leap_year_answer', (2019), 'Year 2019 was not a leap year'),
   ('leap_year_answer', (2040), 'Year 2040 will be a leap year'),
   ('leap_year_answer', (2100), 'Year 2100 will not be a leap year')]

#Task 3
TRIANGULAR_NUM = \
  [('next_triangular_number', (5), 6),
   ('next_triangular_number', (25), 28),
   ('next_triangular_number', (40), 45),
   ('next_triangular_number', (2000), 2016)]

#Task 5
ADD = \
  [('add', ([]), 0),
   ('add', ([25]), 0),
   ('add', ([92, 61, 97, 10, -39]), 71),
   ('add', ([-24, -25, -33, 32, -81, -58, 28, -4, -30, -69, 44, -41]), -165)]

FLIP = \
  [('flip', (''), ''),
   ('flip', ('01'), '10'),
   ('flip', ('101'), '010'),
   ('flip', ('001011111111'), '110100000000')]


#Task 6
EVEN_FIB = \
  [('n_even_fibonacci', (0), []),
   ('n_even_fibonacci', (5), [0, 2, 8, 34, 144]),
   ('n_even_fibonacci', (10), [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]),
   ('n_even_fibonacci', (12), [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578])]


#Challenge
ESTIMATE_E = \
  [('estimate_e', (1), 2.0),
   ('estimate_e', (0.1), 2.6666666666666665),
   ('estimate_e', (0.01), 2.708333333333333),
   ('estimate_e', (0.005), 2.7166666666666663),
   ('estimate_e', (0.001), 2.7180555555555554),
   ('estimate_e', (0.0000000001), 2.7182818284467594)]

evaluate = \
  [(CALCULATE, 1, None),
   (IS_LEAP_YEAR, 0.5, None),
   (LEAP_YEAR_ANSWER, 0.5, None),
   (TRIANGULAR_NUM, 1, None),
   (ADD, 0.5, None),
   (FLIP, 0.5, None),
   (EVEN_FIB, 0, None)
   ]

evaluate += [] if FIT1045 else [(EVEN_FIB, 2, None)]
################################################################################

def main():
    evaluate_module(workshop02, evaluate, marking=False)

    if getattr(workshop02, 'estimate_e', None):
        if estimate_e(0.1):
            evaluate_module(workshop02, [(ESTIMATE_E, 1, None)], 1, marking=False)

def mark():            
    num,email,name = details()
    score = evaluate_module(workshop02, evaluate, marking=True)
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
