# empty_dict = {}
# empty_dict1 = dict()
# collections_map = {
#     'mutable': ['list', 'set', 'dict'],
#     'immutable': ['tuple', 'frozenset']
# }
# print(collections_map['mutable'])
# print(collections_map.get('irresistible', 'Not found'))
# print('mutable' in collections_map)
# print('irresistible' in collections_map)
#
# beatles_map = {
#     'Paul': 'Bass',
#     'Jonh': 'Guitar',
#     'George': 'Guitar',
# }
# print(beatles_map)
# beatles_map['Ringo'] = 'Drums'
# print(beatles_map)
# del beatles_map['Paul']
# print(beatles_map)
# beatles_map.update({
#     'Paul': 'Bass'
# })
# print(beatles_map)
# print(beatles_map.pop('Paul'))

# unknown_dict = {}
# print(unknown_dict.setdefault('key', 'default'))
# print(unknown_dict)

# for key in collections_map:
#     print(key)
# for key, value in collections_map.items():
#     print("{}-{}".format(key,value))
# from collections import OrderedDict
# name = OrderedDict()
# print(type(name))
# for number in range(10):
#     name[number] = str(number)
# for key, value in name.items():
#     print("{}-{}".format(key,value))
# print(type(name))
# import this
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
zen_map = dict()

for word in zen.split():
    cleaned_word = word.strip('.,!-').lower()
    if cleaned_word not in zen_map:
        zen_map[cleaned_word] = 0
    zen_map[cleaned_word] += 1
# print(zen_map)
import operator
zen_items = zen_map.items()
word_count_items = sorted(
    zen_items, key=operator.itemgetter(1), reverse=True
)
print(word_count_items[:9])

from collections import Counter

cleaned_list = []
for word in zen.split():
    cleaned_list.append(word.strip('.,!-').lower())
print(Counter(cleaned_list).most_common(7))
