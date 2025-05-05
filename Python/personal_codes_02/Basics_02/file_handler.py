class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"File {filename} opened.")

    def write(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("File closed.")

# Usage
handler = FileHandler('example.txt')
handler.write("Hello, World!")
del handler  # This will trigger the __del__ method


class FileHandler2:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def write(self, data):
        self.file.write(data)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("File closed.")

# Usage
with FileHandler2('example.txt') as handler:
    handler.write("Hello, World!")
# The file is automatically closed when exiting the with block
