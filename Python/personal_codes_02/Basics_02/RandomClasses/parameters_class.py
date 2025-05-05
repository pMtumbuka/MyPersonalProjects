class MyClass:
    def __init__(self, param1=None, param2=None):
        if param1 is None and param2 is None:
            # Default constructor
            self.value = "Default"
        elif param2 is None:
            # Constructor with one parameter
            self.value = param1
        else:
            # Constructor with two parameters
            self.value = f"{param1}-{param2}"

    # For end-users, simple and friendly
    def __str__(self):
        return f"MyClass with value: {self.value}"

    # For developers, precise and formal
    def __repr__(self):
        return f"MyClass('{self.value}')"

    # Calling destructor
    def __del__(self):
        print("Destructor called, Example deleted.")

# Usage
obj1 = MyClass()          # Default constructor
obj2 = MyClass("Hello")   # One parameter
obj3 = MyClass("Hi", "there")  # Two parameters

print(obj1)
print(obj2)
print(obj3)
