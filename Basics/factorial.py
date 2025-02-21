import sys
sys.setrecursionlimit(30000)  # Increase the recursion limit

import math


# Solution 1: Use Iteration Instead of Recursion

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input_num = factorial_iterative(int(input("Which Number Would You Like To Find The Factorial Of? \n")))
print(f"The Factorial is: {user_input_num}")


'''

# Solution 2: Increase the Recursion Limit

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

user_input_num = int(input("Which Number Would You Like To Find The Factorial Of? \n"))
print(f"The Factorial is: {math.factorial(user_input_num)}")
'''