# empty_set = {}
# number_set = {1,2,3,3,4,5}
# print(number_set)
# print(10 in number_set)

# odd_set = set()
# even_set = set()
# for number in range(10):
#     if number % 2 == 0:
#         even_set.add(number)
#     else:
#         odd_set.add(number)
# print(odd_set)
# print(even_set)
# union_set = odd_set | even_set
# print(union_set)
# union_set = odd_set.union(even_set)
# print(union_set)
# odd_set.add(20)
# even_set.add(20)
# odd_set.add(21)
# even_set.add(21)
# even_set.add(55)
# even_set.add(43)
# odd_set.add(122)
# union_set = odd_set.intersection(even_set)
# print(union_set)
# union_set = odd_set & even_set
# print(union_set)
# print(odd_set)
# print(even_set)
# difference_set = odd_set - even_set
# print(difference_set)
# difference_set = odd_set.difference(even_set)
# print(difference_set)
# symmetric_difference_set = odd_set ^ even_set
# print(symmetric_difference_set)
# symmetric_difference_set = odd_set.symmetric_difference(even_set)
# print(symmetric_difference_set)
# symmetric_difference_set.remove(122)
# print(symmetric_difference_set)
import random

random_set = set()

while True:
    new_number = random.randint(1,20)
    if new_number in random_set:
        break
    random_set.add(new_number)
print(len(random_set)+1)
