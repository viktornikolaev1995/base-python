# def dummy_factory():
#     class Class:
#         pass
#     return Class
#
#
# Dummy = dummy_factory()
# print(type(Dummy))
# print(type(Dummy()))
# print(Dummy() is Dummy())
#
# NewClass = type("NewClass", (), {})
# print(NewClass)
# print(NewClass())
# class B:
#     def __init__(self, number):
#         self.number = number ** 2
# class C:
#     B = 10
# class Meta(type):
#     def __new__(cls, name, parents, attrs):
#         print("Creating {}".format(name))
#         if "class_id" not in attrs:
#             attrs["class_id"] = name.lower()
#             print(attrs)
#         return super().__new__(cls, name, parents, attrs)
#
# class A(metaclass=Meta):
#     pass

# Student = type('Student2', (), {'name': None, 'age': None, 'grade': None })
# print(Student.__name__)
# a = Student()
# print(type(a))
# print(type(Student))

# def init(self, name, age, aver_mark):
#     self.name = name
#     self.age = age
#     self.aver_mark = aver_mark
#
# Student = type('Student', (), {'__init__': init})
# Mark = Student('Mark', 23, 4.4)
# print(Mark.)
# print(Mark.__dict__)
# print(type(Student))


import re
import requests, time
def main(site_url, substring):
    start_time = time.strftime('%X')
    # import pdb
    # pdb.set_trace()
    site_code = get_site_code(site_url)
    matching_substrings = get_matching_substrings(site_code, substring)
    end_time = time.strftime('%X')
    print("Starting time at: {} ; {} found {} "
          "times in {}; Wasted time "
          "for finishing programm {}".format(start_time, substring, len(matching_substrings), site_url, end_time))
def get_site_code(site_url):
    if not site_url.startswith('http'):
        site_url = 'http://' + site_url
    return requests.get(site_url).text
def get_matching_substrings(source, substring):
    return re.findall(substring, source)

main("mail.ru", "script")


