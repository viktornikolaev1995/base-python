#1 task
# import sys
# digit_string = sys.argv[1]
# if not digit_string:
#     raise ValueError("Переданный параметр не должен быть пустым")
# s = 0
# if digit_string.isdigit():
#     for i in digit_string:
#         s += int(i)
#     print(s)
# else:
#     raise ValueError("Переданный параметр должен содержать только числовые символы")

#2 task
# import sys
# quantity = sys.argv[1]
# if not quantity:
#     raise ValueError("Переданный параметр не должен быть пустым")
# if not (isinstance(int(quantity), int) and int(quantity) > 0):
#     raise ValueError("Переданный параметр должен содержать только числовые символы и равен больше нуля")
#
# quan = int(quantity)
# symb1 = "#"
# symb2 = " "
# n = 1
# for i in range(quan):
#     print((quan-1)*symb2+n*symb1)
#     quan -= 1
#     n += 1

#3 task
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b**2-4*a*c
if d > 0:
    x1 = int( ( -b + d**0.5) / (2*a) )
    print(x1)
    x2 = int( ( -b - d**0.5) / (2*a) )
    print(x2)
elif d == 0:
    x = int( -b / (2*a) )
    print(x)
else:
    print("Корней квадратного уравнения не существует")
