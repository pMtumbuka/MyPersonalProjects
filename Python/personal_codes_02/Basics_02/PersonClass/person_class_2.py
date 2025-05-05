class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):
        print("Hello, {}! Great to hear that you are {} years old.".format(self.name, self.age))

print("Hello there.")

p1 = Person(input("What is your name?\n"), int(input("How old are you?\n")))

p1.greet()

siblings = input("Do you have any siblings? (yes/no)\n").strip().lower()

if siblings == "yes":
    p2 = Person(input("What is your sibling's name?\n"), int(input("How old are they?\n")))
    print("Oh, {} is a great name. So they are {} years old, great to know. Thank you very much for sharing this with me.".format(p2.name, p2.age))
    p2.greet()  # This allows the sibling to greet too
else:
    response = input("How does it feel to be an only child?\n")
    print("Okay, that's a normal feeling.")
