# def even_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 3
#
# # for i in even_range(1,20):
# #     print(i, type(i))
#
# print(even_range(1,5))
#
# ranger = even_range(1,10)
# print(next(ranger))
# print(next(ranger))

# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print("After yeilding {}".format(item))
#
# generator = list_generator([1,2,6,9])
# print(next(generator))
# print(next(generator))
# print(next(generator))

# def fibonacci(number):
#     a = b = 1
#     for _ in range(number):
#         yield a
#         a, b = b, a + b
#
# a = fibonacci(20)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def accumulator():
    total = 0
    while True:
        value = yield total
        print("Got: {}".format(value))

        if not value: break
        total += value
        print(total)

generator = accumulator()

print(next(generator))
generator.send(5)
print("Accumulated: {}".format(generator.send(2)))
print("Accumulated: {}".format(generator.send(2)))
