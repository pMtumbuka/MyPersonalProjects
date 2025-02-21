
# Defining a Function

def greet(name):
    """This function prints a greeting message."""
    print(f"Hello, {name}!")
    
user_name = input("What Is Your Name? \n")

greet(user_name)  # Output: Hello, Patrick!


# Function with Return Value

def mult(a, b):
    return a * b

firstNum = float(input("Enter The First Number Here: \t"))
secondNum = float(input("Enter The Second Number Here: \t"))

multiplication = mult(firstNum, secondNum)
print("The Multiplication Of {} and {} is: ".format(firstNum, secondNum) + str(multiplication))  

'''
# Default Parameters

def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message) # Output: Hello, Alice!


# Using Default Parameters 

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Using default argument
describe_pet("Buddy")  # Output: I have a dog named Buddy.

# Overriding default argument
describe_pet("Whiskers", "cat")  # Output: I have a cat named Whiskers.


# Recursion


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Nested Functions

def outer():
    def inner():
        print("Hello from inner function")
    inner()

outer()  # Output: Hello from inner function
'''