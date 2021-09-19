# def caller(func, params):
#     return func(*params)
# def printer(name, origin):
#     print("I'm {} of {}".format(name,origin))
#
# caller(printer, ['Moana', 'Motunui'])
#
# a = ['Moana', 'Motunui']
#
# print(*a)
#
# def get_multiplier(number):
#     def inner(a):
#         return a*number
#     return inner
#
# multiplier_by_2 = get_multiplier(3)
# print(multiplier_by_2(20))

def squarify(a):
    return a**3

a = list(map(squarify, range(50)))
print(a,"\n",len(a))

def is_positive(a):
    return a > 0
a1 = list(filter(is_positive, range(-5,9)))
print(a1)

a2 = list(map(lambda v: v**3, range(6)))
print(a2)
a3 = list(filter(lambda v: v > 0, range(-20, 6)))
print(a3)

print(list(map(lambda v: float(v), range(10))))

from functools import reduce, partial

print(reduce(lambda v, v1: v * v1, range(1,7)))

def greeter(person, greeting):
    return "{}, {}!".format(greeting, person)

hier = partial(greeter, person="Mike")
helloer = partial(greeter, person="Mikel")

print(hier(greeting="Hi"))
print(helloer(greeting="Hello"))
