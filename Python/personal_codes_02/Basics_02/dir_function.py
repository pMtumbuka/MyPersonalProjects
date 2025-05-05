class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def __del__(self):
        print(f"Object {self.name} is being deleted")

print("==================================================================")

p = Person("Alice")
print(dir(p))

del p  # Explicitly deleting the object

print("==================================================================")

methods = [method for method in dir(str) if not method.startswith('__')]
print(methods)

print("==================================================================")

class MyClass:
    def __init__(self):
        print("This Is The __init__() Dunder Method")

    def __str__(self):
        return "This is MyClass"

    def __repr__(self):
        return "MyClass()"

    def __del__(self):
        print("Calling The Destructor Method")

obj = MyClass()
print(str(obj))  # Calls obj.__str__()

del obj  # Explicitly deleting the object

print("==================================================================")

obj2 = MyClass()
print(repr(obj2))  # Calls obj.__repr__()

del obj2  # Explicitly deleting the object

print("==================================================================")


class Example:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object is being destroyed")

def create_object():
    obj = Example()  # Local variable inside function

create_object()  # Function call
print("Function exited")
