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
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        return Iteration(self)
    def read(self):
        with open(self.filename, "r") as f:
            return f.read()
    def write(self, text):
        with open(self.filename, "w") as f:
            return f.write(text)

    def count(self):
        with open(self.filename, "r") as f:
            count = 0
            list = f.readlines()
            for _ in list:
                count += 1
            return count, list



m = File("text.log")

print(m.count())

for i in m:
    print(ascii(i))