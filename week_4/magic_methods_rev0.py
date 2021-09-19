import os, tempfile

class Iteration:
    def __init__(self, other):
        self.len, self.lines = other.count()
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.len:
            raise StopIteration
        self.start += 1
        return self.lines[self.start - 1]


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            self.path = path
            self.write("")
        self.path = path
    def read(self):
        with open(self.path, "r") as f:
            return f.read()
    def write(self, text):
        with open(self.path, "w") as f:
            return f.write(text)

    def count(self):
        with open(self.path, "r") as f:
            count = 0
            list_ = f.readlines()
            for _ in list_:
                count += 1
            return count, list_

    def __str__(self):
        return self.path
    @staticmethod
    def temp():
        temp = tempfile.TemporaryFile()
        path = os.path.join(tempfile.gettempdir(), temp.name)
        return path

    def __add__(self, other):
        path = self.temp()
        new_instance = File(path)
        data = self.read() + other.read()
        new_instance.write(data)
        return new_instance

    def __iter__(self):
        return Iteration(self)