import random
class Car:
    def __new__(cls, *args, **kwargs):
        coordX = random.randint(1, 100)
        coordY = random.randint(1, 100)
        new_args = [coordX, coordY]
        return cls(*new_args)

    def __init__(self, *args):
        ...


car1 = Car()
