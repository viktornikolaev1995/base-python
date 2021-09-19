# import json
# class Pet:
#     def __init__(self, name):
#         print("Вызов базового класса из дочернего с помощью метода super()")
#         self.name = name
# class Dog(Pet):
#     def __init__(self, name, breed=None):
#         super().__init__(name)
#         self.breed = breed
#     def say(self):
#         return "{}: waw".format(self.name)
#     def to_json(self):
#         return json.dumps(
#             {"breed": self.breed,
#              "name": self.name
#             }
#         )
#     def decoder_form_to_json(self):
#         return json.loads(self.to_json())
#
# dog = Dog("Шарик", "Доберман")
# print(dog.name)
# print(dog.say())
# print(dog.to_json())
# print(dog.decoder_form_to_json())
# print(issubclass(Dog,Pet))
# print(isinstance(dog,Dog))

import math
class Math:
    def __init__(self, a, b, c):
        print("Вызов базового класса Math из дочернего с помощью метода super()")
        self.a = a
        self.b = b ** 2
        self.c = c ** 1.5


    def calc(self):
        return math.sqrt(self.a) * math.sqrt(self.b) + math.pow(self.c, 1)



class Math3:
    pass
    # def __init__(self, b):
    #     print("Вызов базового класса Math3 из дочернего с помощью метода super()")
    #     self.b = b + 2

class Math2(Math):
    def __init__(self, a, b, c):
        self.a = a ** 2
        super().__init__(b)
        super().__init__(c)
        # super(Math,self).__init__(c)
        # super(Math,self).__init__(c)

calc = Math2(2, 5, 7)
# print(calc.__dict__)
# print(calc.calc())
