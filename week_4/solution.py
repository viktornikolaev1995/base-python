import os, tempfile, uuid

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
    def __init__(self, file):
        if not os.path.exists(file):
            self.file = file
            self.write("")
        self.file = file
    def read(self):
        with open(str(self.file), "r") as f:
            return f.read()
    def write(self, text):
        with open(str(self.file), "w") as f:
            return f.write(text)

    def count(self):
        with open(str(self.file), "r") as f:
            count = 0
            list_ = f.readlines()
            for _ in list_:
                count += 1
            return count, list_

    def __str__(self):
        return self.file

    def __add__(self, other):
        unique_filename = str(uuid.uuid4())
        filename = os.path.join(tempfile.gettempdir(), unique_filename)
        new_instance = File(filename)
        data = self.read() + other.read()
        new_instance.write(data)
        return new_instance

    def __iter__(self):
        return Iteration(self)



# with open('file1.txt', 'w') as file:
#     file.write('file 1\nline 1\nline 2\nline 3\n')
#
# file_obj_1 = File('file1.txt')
#
# with open('file2.txt', 'w') as file:
#     file.write('file 2\nline 4\nline 5\nline 6\n')
#
# file_obj_2 = File('file2.txt')
# new_file = file_obj_1 + file_obj_2
# print('content new_file:', ascii(new_file.read()))
# print(new_file)