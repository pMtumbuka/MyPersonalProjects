class Descriptor:
    def __get__(self, instance, owner):
        print("Getting attribute")
        return instance.__dict__.get("_value", None)

    def __set__(self, instance, value):
        print(f"Setting attribute to {value}")
        instance.__dict__["_value"] = value

    def __delete__(self, instance):
        print("Deleting attribute")
        del instance.__dict__["_value"]



class MyClass:
    attr = Descriptor()  # attr is managed by Descriptor

obj = MyClass()
obj.attr = 10   # Calls __set__
print(obj.attr) # Calls __get__
del obj.attr    # Calls __delete__




class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("_age", None)

    def __set__(self, instance, value):
        if not (0 <= value <= 120):
            raise ValueError("Age must be between 0 and 120")
        instance.__dict__["_age"] = value

    def __delete__(self, instance):
        print("Deleting age attribute")
        del instance.__dict__["_age"]

class Person:
    age = AgeDescriptor()

p = Person()
p.age = 25  # Valid assignment
print(p.age)  # Works fine
del p.age  # Calls __delete__
