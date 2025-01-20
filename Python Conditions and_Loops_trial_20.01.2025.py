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
# For each element in a list:
# If the index is even, double the element.
# If the index is odd, subtract 1 from the element.
def modify_list(lst):
    lst_mod=[]
    for i, k in enumerate(lst):
        if i % 2 ==0:
            lst_mod.append(k*2)
        else:
            lst_mod.append(k-1)
    print(lst_mod)

modify_list([1, 2, 3, 4, 5])
#3.
#

