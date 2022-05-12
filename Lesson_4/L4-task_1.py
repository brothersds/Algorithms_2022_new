"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Выбрана задача Lesson 3 task 4 ()

Определить, какое число в массиве встречается чаще всего.
"""

# постановка задачи
import random

SIZE = 500
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 2) for _ in range(SIZE)]
print(array)

# решение задачи рекурсивным методом


def dict_rec(arr, res={}, repeat=[1], item=[]):
    if not arr:
        return
    else:
        first_el = arr[0]
        if not type(first_el) == list:
            res[first_el] = res.get(first_el, 0) + 1
            if repeat[len(repeat) - 1] < res[first_el]:
                item.clear(), item.append(first_el)
                repeat.clear(), repeat.append(res[first_el])
        dict_rec(arr[1:])
    return item, repeat


result = dict_rec(array)
if result is None:
    print("Нет совпадений")
else:
    print(f'Число {result[0][0]} встречается {result[1][0]} раз(-a)')

# решение задачи циклом for
count = {}
repeat = 1
num = None
for item in array:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
    if count[item] > repeat:
        repeat = count[item]
        num = item
if num is None:
    print("Нет совпадений")
else:
    print(f'Число {num} встречается {repeat} раз(-a)')

# решение задачи циклом while
count = {}
repeat = 1
n = 0
num = 0
while n < len(array):
    i = array[n]
    n += 1
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    if count[i] > repeat:
        repeat = count[i]
        num = i
if num is None:
    print("Нет совпадений")
else:
    print(f'Число {num} встречается {repeat} раз(-a)')
