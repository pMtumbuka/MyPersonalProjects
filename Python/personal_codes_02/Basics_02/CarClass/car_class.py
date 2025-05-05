# Demostration Of A Class In Py

class Car:
    def __init__(self, brand="Toyota", model="Corolla", color="White"):
        self.brand = brand
        self.model = model
        self.color = color

c1 = Car()  # Uses default values
c2 = Car("Honda", "Civic", "Black")  # Uses given values

print(c1.brand, c1.model, c1.color)  # Output: Toyota Corolla White
print(c2.brand, c2.model, c2.color)  # Output: Honda Civic Black
