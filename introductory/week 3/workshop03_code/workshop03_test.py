#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False



#############################################################################

#Import statements
from workshop03 import *
import workshop03
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

def evaluate_module(module, tests, mark=2.5, marking=False):
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

    if res/max>=0.95 and f_passed > 1: scaled = 2.5
    elif res/max>=0.7 and f_passed > 1: scaled = 2
    elif res/max>=0.5 and f_passed > 1: scaled = 1.5
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

PARTIAL_SUM = \
  [('partial_sum', (3, 13, 2), 48),
   ('partial_sum', (8, 290, 5), 8436),
   ('partial_sum', (-5, 30, 3), 138),
   ('partial_sum', (-10, -100, -5), -1045) ]

#Task 2
REVERSE_STRINGS = \
  [('reverse_strings', [], ''),
   ('reverse_strings', ['my','little','pony'], 'ponylittlemy'),
   ('reverse_strings', ['00','11','22','33'], '33221100')]

COMPLETE = \
  [('complete', [12,15,19], [12,13,14,15,16,17,18,19]),
   ('complete', [2,3], [2,3]),
   ('complete', [1], [1]),
   ('complete', [-5,0,5], [-5,-4,-3,-2,-1,0,1,2,3,4,5])]

#Task 3
ADD_TABLE = \
  [('addition_table', [2,5,-3,7], [[3,6,-2,8],[4,7,-1,9],[5,8,0,10]]),
   ('addition_table', [1], [[2],[3],[4]]),
   ('addition_table', [-2,-5,-9,-12,-23], [[-1,-4,-8,-11,-22],[0,-3,-7,-10,-21],[1,-2,-6,-9,-20]])]

#Task 4
OUTLIERS = \
  [('remove_outliers', [[0,4],[2,4],[-1,3]], [[0,1.5],[2,1.5],[1.5,3]])]

#Task 5
SIEVE = \
  [('primes_in_range', (35,100), [37,41,43,47,53,59,61,67,71,73,79,83,89,97]),
   ('primes_in_range', (211,263), [211,223,227,229,233,239,241,251,257,263]),
   ('primes_in_range', (35400,35500), [35401,35407,35419,35423,35437,35447,35449,35461,35491]),
   ('primes_in_range', (51854787,51854830), [51854801, 51854807, 51854809, 51854821, 51854827]) ]


#Challenge
#Given examples
board1 = [['x',None,'o'],
          [None,'x','o'],
          [None,None,None]]
board2 = [['x',None,'o',None],
          [None,'x','o','o'],
          ['x','x','o','o'],
          [None,'o','x','x']]
#Empty
board3 = [[None]]
#Finds rows
board4 = [[None,None,None,None,None],
          [None,'x','x','x','x'],
          [None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None]]
board5 = [[None,None,None,None,None],
          [None,None,None,None,None],
          ['o','o','o','o',None],
          [None,None,None,None,None],
          [None,None,None,None,None]]
board6 = [[None,None,None,None,None],
          [None,None,None,None,None],
          ['o','o','o','o','o'],
          [None,None,None,None,None],
          [None,None,None,None,None]]
#Finds col
board7 = [[None,'x',None,None,None],
          [None,'x',None,None,None],
          [None,'x',None,None,None],
          [None,'x',None,None,None],
          [None,None,None,None,None]]
board8 = [[None,None,None,None,None],
          [None,None,None,'o',None],
          [None,None,None,'o',None],
          [None,None,None,'o',None],
          [None,None,None,'o',None]]
board9 = [[None,None,None,'o',None],
          [None,None,None,'o',None],
          [None,None,None,'o',None],
          [None,None,None,'o',None],
          [None,None,None,'o',None]]
#Finds diagonals
board10 = [['x','o',None,None],
         [None,'x',None,None],
         ['o',None,None,None],
         [None,None,None,'x']]
board11 = [[None,None,None,None],
         [None,None,'o',None],
         [None,'o',None,None],
         ['o',None,None,None]]
#No duplicates
board12 = [['o','o','o',None],
         [None,'x','o',None],
         [None,'o','o',None],
         ['o',None,None,None]]

TTT_WIN = \
  [('ttt_winning_move', board1, ['o','x']),
   ('ttt_winning_move', board2, []),
   ('ttt_winning_move', board3, ['o','x']),
   ('ttt_winning_move', board4, ['x']),
   ('ttt_winning_move', board5, ['o']),
   ('ttt_winning_move', board6, []),
   ('ttt_winning_move', board7, ['x']),
   ('ttt_winning_move', board8, ['o']),
   ('ttt_winning_move', board9, []),
   ('ttt_winning_move', board10, ['x']),
   ('ttt_winning_move', board11, ['o']),
   ('ttt_winning_move', board12, ['o'])]


evaluate = \
  [(PARTIAL_SUM, 1, None),
   (REVERSE_STRINGS, 0.5, None),
   (COMPLETE, 0.5, None),
   (ADD_TABLE, 1, None),
   (OUTLIERS, 1, None),
   (SIEVE, 1, None)
   ]

evaluate += [] if FIT1045 else [(SIEVE, 2, sorted)]
################################################################################

def main():
    evaluate_module(workshop03, evaluate, marking=False)

    if getattr(workshop03, 'ttt_winning_move', None):
        if ttt_winning_move([[None]]) != None:
            evaluate_module(workshop03, [(TTT_WIN, 1, sorted)], 1, marking=False)

def mark():            
    num,email,name = details()
    score = evaluate_module(workshop03, evaluate, marking=True)
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
