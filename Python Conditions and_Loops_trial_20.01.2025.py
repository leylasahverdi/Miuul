# All questions asked by ChatGPT, and the answers were answered by me
#1. Write a function:
# check_divisibility(num, divisors), which checks if a number is divisible by all the numbers in a given list.
#
# If divisible by all, return True; otherwise, return False.

def check_divisibility(num, divisors): #all results (for all items) will be printed
    for i in divisors:
        if num % i != 0:
            print('False')
        else:
            print('True')

check_divisibility(10, [1,5])
def check_divisibility1(num, divisors): # there will be just one result
    if any(num % i != 0 for i in divisors): #!!!! #the expression if all() is also used, and applicable here
        print('False')
    else:
        print('True')
check_divisibility1(10, [1,7])

# 2.

