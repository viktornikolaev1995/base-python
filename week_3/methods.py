# class Human:
#     def __init__(self, name, age=None):
#         self.name = name
#         self.age = age
# class Planet:
#     def __init__(self, name, population=None):
#         self.name = name
#         self.population = population or []
#     def add_human(self, human):
#         print(f"Welcome to {self.name}, {human.name}!")
#         self.population.append(human)
# mars = Planet("Mars")
# bob = Human("Bob")
# mars.add_human(bob)
# mark = Human("Mark")
# mars.add_human(mark)
# print([i.name for i in mars.population])

# class Human:
#     def __init__(self, name, age=None):
#         self._name = name
#         self._age = age
#     def _say(self, text):
#         print(text)
#     def say_name(self):
#         self._say(f"Hello, I am {self._name}")
#     def say_how_old(self):
#         self._say(f"I am {self._age} years old")
# bob = Human("Bob", 25)
# bob.say_name()
# bob.say_how_old()

# from datetime import date
# def extract_description(user_string):
#     return "Открытие чемпионата мира по футболу"
# def extract_date(user_string):
#     return date(2018, 6, 14)
# class Event:
#     def __init__(self, description, event_date):
#         self.description = description
#         self.date = event_date
#     def __str__(self):
#         return f"Event \"{self.description}\" at {self.date}"
#
#     @classmethod
#     def from_string(cls, user_input):
#         description = extract_description(user_input)
#         date = extract_date(user_input)
#         return cls(description, date)

# from datetime import date
# even_description = "Рассказать, что такое @classmethod"
# even_date = date.today()
# event = Event(even_description, even_date)
# print(event)
# event = Event.from_string("Добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
# print(event)
# print(dict.fromkeys("victor"))

# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#     @staticmethod
#     def is_age_valid(age):
#         return 0 < age < 27
#
# human = Human("Viktor", 25)
# print(human.is_age_valid(21))

class Robot:
    def __init__(self, power):
        self.power = power
    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = self.power
        return self.power

r = Robot(100)
print(r.set_power(-200))

