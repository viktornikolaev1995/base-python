# def decorator(func):
#     def new_func():
#         return 5
#     return new_func
#
# @decorator
# def decorated():
#     print("Hello!")
#
# print(decorated())
# print(decorated.__name__)

# def stringify(func):
#    print("def stringify")
#    return func
#
#
# @stringify
# def multiply():
#    print("def multiply")
#    return 6

# print(multiply())
import functools
#
# def logger(func):
#     @functools.wraps(func)
#     def wrapped(num_list):
#         result = func(num_list)
#         with open("C:\\Users\\vikto\\text.txt", "w") as f:
#             f.write(str(result))
#         return result
#     return wrapped
# @logger
# def simulator(num_list):
#     return sum(num_list)
#

# print(simulator(a))
# with open("C:\\Users\\vikto\\text.txt", "r") as f:
#     print(f"text.txt: {f.read()}")
# print(simulator.__name__)

# def logger(filename):
#     def decorator(func):
#         def wrapped(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(filename, "w") as f:
#                 f.write(str(result))
#             return result
#         return wrapped
#     return decorator
# a = list(range(1,66,3))
# @logger("C:\\Users\\vikto\\text.txt")
# def summator(a):
#     return sum(a)
# print(summator(a))
# with open("C:\\Users\\vikto\\text.txt", "r") as f:
#     print(f.read())
# summator = logger("log.txt")(summator)

# def first_decorator(func):
#     def wrapped():
#         print("Inside first_decorator product")
#         return func()
#     return wrapped
#
# def second_decorator(func):
#     def wrapped():
#         print("Inside second_decorator product")
#         return func()
#     return wrapped
#
# @first_decorator
# @second_decorator
# def decorated():
#     print("Finally called...")
#
# decorated()

def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@bold
@italic
def hello():
    return "hello world"

print(hello())


