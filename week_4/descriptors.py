# class Descriptor:
#     def __get__(self, obj, obj_type):
#         print("get")
#     def __set__(self, obj, value):
#         print("set")
#     def __delete__(self, obj):
#         print("delete")
#
# class Class:
#     attr = Descriptor()
#
# obj1 = Class
# obj1.attr
# obj1.attr = 5
# del obj1.attr

# class Value:
#     def __init__(self):
#         self.value = None
#     @staticmethod
#     def _prepare_value(value):
#         return value * 10
#     def __get__(self, obj, obj_type):
#         return self.value
#     def __set__(self, obj, value):
#         self.value = self._prepare_value(value)
#
# class Class:
#     attr = Value()
#
# instance = Class()
# instance.attr = 20
# print(instance.attr)

class ImportantValue:
    def __init__(self, amount):
        self.amount = amount
    def __get__(self, obj, obj_type):
        return self.amount
    def __set__(self, obj, value):
        with open('text2.log', "w") as f:
            f.write(str(value))
        self.amount = value

class Account:
    amount = ImportantValue(200)

a = Account()
print(a.amount)
a.amount = 500
print(a.amount)