# response = None
# if response == None:
#     response = "45"
#     print(response)
#
# res = None
# if not isinstance(res, str):
#     res = "ht"
#     print(res)

response = 'ok\n'
key = "nntest"
values = [(10, 120200.6)]
for i in values:
    response += ' '.join([key, str(i[1]), str(i[0])+'\n'])

#     print(ascii('{0}\n'.format(response)))
# AssertionError: Тест 16.2. На сервер отправлено несколько запросов на сохранение данных по ключу
# test_same_timestamp. Среди данных есть результаты измерений с одинаковым значением
# timestamp. Ожидается сохранение на сервере данных двух измерений: (0.0, 1503319740) и (100.99, 1503319743).
# На запрос получения данных по ключу: 'get test_same_timestamp\n' сервер вернул не верный ответ:
# 'ok\ntest_same_timestamp 12.0 1503319740\ntest_same_timestamp 0.0 1503319740\ntest_same_timestamp 12.5 1503319743\ntest_same_timestamp 100.99 1503319743\n\n'.


'ok\ntest_same_timestamp 12.0 1503319740\ntest_same_timestamp 0.0 1503319740\ntest_same_timestamp 12.5 1503319743\ntest_same_timestamp 100.99 1503319743\n\n'

key_ = 'test_same_timestamp'
tup_list = (100.99, 1503319743)
d = {'test_same_timestamp': [(12.0, 1503319740), (12.5, 1503319743)], 'test_same_timestamp1': [(12.0, 1503319740), (12.5, 1503319743)]}
# print(d)
# [print(i[0][1]) for i in d.values()]

def func(key_,tup_list,d):
    if key_ in d.keys():
        if tup_list[1] in [j for i,j in d[key_]]:
            for idx,data in enumerate(d[key_]):
                if tup_list[1] == data[1]:
                    d[key_][idx] = tup_list
        else:
            d[key_].append(tup_list)
func(key_,tup_list,d)
print(d)
tup_list1 = (0.0, 1503319740)
func(key_,tup_list1,d)
print(d)
tup_list2 = (100.99, 1503319743)
key1_ = 'test_same_timestamp1'
func(key1_,tup_list2,d)
print(d)