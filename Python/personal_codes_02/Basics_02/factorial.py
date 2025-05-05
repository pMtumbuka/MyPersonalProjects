
import sys
sys.setrecursionlimit(1000000)  # Increases recursion limit

from dictionaries import print_name

import import_functions

def factorial(n) -> int:
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call


# Taking user input
num = int(input("Enter The Number You Would Like To Take The Factorial Of Here:\t"))


if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("The factorial of {} is {}".format(num, factorial(num)))

print_name()

print(f"External access: {import_functions.__name__}")
