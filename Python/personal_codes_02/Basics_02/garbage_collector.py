import gc

class Example:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} is being destroyed")

obj = Example("Persistent")
other_ref = obj  # Another reference to the same object
del obj  # Does not delete the object immediately

gc.get_count()
gc.get_freeze_count()
gc.get_objects()
gc.get_referents()
gc.get_referrers()

print(dir(gc))

print("End of script")
gc.collect()  # Forcing garbage collection
