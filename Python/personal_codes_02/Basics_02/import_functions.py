def greet():
    print("Hello from the module!")

print(type(greet))

if __name__ == "__main__":
    greet()  # This will only run if the script is executed directly
else:
    print("Imported as", __name__)

# print(__name__)

# The following block will never run because __name__ is never equal to "__factorial__"
# So it's either a mistake or intended for another purpose, like testing or modifying later.

if __name__ == "__import_functons__":
    print("the if block is now in your script executing as we speak!")
