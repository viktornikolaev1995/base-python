# while True:
#     try:
#         raw = input("Enter a number: ")
#         number = int(raw)
#         break
#     except ValueError:
#         print("Incorrect value")
#     except KeyboardInterrupt:
#         print("Exit from programm")
#         break
print(issubclass(IndexError,LookupError))
print(issubclass(IndexError,LookupError))

database = {
    "red": ["fox", "flower"],
    "green": ["peace", "M", "python"]
}

try:
    color = input("Enter a color: ")
    number = input("Enter a number in order: ")
    label = database[color][int(number)]
    print("You choose", label)
except LookupError:
    print("Object is not found")