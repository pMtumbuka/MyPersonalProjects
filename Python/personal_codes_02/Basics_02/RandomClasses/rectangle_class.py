class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            # No parameters
            self.width = 0
            self.height = 0
        elif len(args) == 1:
            # One parameter (square)
            self.width = self.height = args[0]
        elif len(args) == 2:
            # Two parameters
            self.width, self.height = args
        else:
            raise ValueError("Too many arguments")

# Usage
r1 = Rectangle()      # 0x0 rectangle
r2 = Rectangle(5)     # 5x5 square
r3 = Rectangle(3, 4)  # 3x4 rectangle
