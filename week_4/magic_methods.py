# class Singleton:
#     instance = None
#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# a = Singleton()
# b = Singleton()
# print(a.instance)
# print(b.instance)

# class Singleton_:
#     instance = None
#     count = 1
#     def __new__(cls):
#         if cls.count <= 4:
#            cls.instance = super().__new__(cls)
#            cls.count += 1
#         return cls.instance
#
# a1 = Singleton_()
# b1 = Singleton_()
# c1 = Singleton_()
# d1 = Singleton_()
# e1 = Singleton_()
# e2 = Singleton_()
# print(d1, e1, e2)
# print(d1 == e1 == e2)


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     def __str__(self):
#         return '{} <{}>'.format(self.name, self.email)
#
# jane = User('Jane Doe', 'janedoe@example.com')
# print(jane)


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     def __hash__(self):
#         return hash(self.email)
#     def __eq__(self, other):
#         return self.email == other.email
#
# jane = User('Jane Doe', 'jdoe@example.com')
# joe = User('Joe Doe', 'jdoe@example.com')
#
# print(jane == joe)
# print(hash(jane))
# print(hash(joe))
#
# user_email_map = {user: user.name for user in [jane, joe]}
# print(user_email_map)
#
# print(jane, joe)

# class Researcher:
#     def __getattr__(self, name):
#         return "Nothing found :("
#
#     def __getattribute__(self, name):
#         print(f"Looking for {name}")
#         return object.__getattribute__(self,name)
#
# obj = Researcher()
# print(obj.n)
# print(obj.meme)

class PascalList:
    def __init__(self, original_list = None):
        self.container = original_list or []
    def __getitem__(self, index):
        return self.container[index-1]
    def __setitem__(self, index, value):
        self.container[index-1] = value
    def __str__(self):
        return self.container.__str__()

numbers = PascalList([1,2,3,4,5])
print(numbers[1])
