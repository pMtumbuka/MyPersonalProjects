# Demostration Of A Class In Py

class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):
        print("Hello, {} Great To Here That You Are {} Years Old.".format(self.name, self.age))

print("Hello There.")

p1 = Person(input("What Is Your Name?\n"), int(input("How Old Are You?\n")))

p1.greet()

# p2.greet()

# print(("Do You Have Any Siblings?\n"))

siblings = input("Do You Have Any Siblings?\n")

if siblings.lower() == "yes":
    p2 = Person(input("What Is Your Sibling's Name?\n"), int(input("How Old Are They?\n")))
    print("Oh, {} Is a Great Name. So They Are {} Years Old, Great To Know. Thank You Very Much For Sharing This With Me".format(p2.name, p2.age))
else:
    print(input("How Does It Feel To Be An Only Child?\n"))
    print("Okay, That's a Normal Feeling.")
