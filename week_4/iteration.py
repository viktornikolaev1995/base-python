class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 3
        self.current += 1
        return result
for num in SquareIterator(1,6):
    print(num)