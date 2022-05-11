"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

# решение задачи
min_num = max_num = ls[0]
index_min = 0
index_max = 0
for index, item in enumerate(ls):
    if item < min_num:
        index_min = index
        min_num = item
    elif item > max_num:
        index_max = index
        max_num = item
s = 0
if index_min > index_max:
    ls[index_min], ls[index_max] = ls[index_max], ls[index_min]
    for index in range(index_max + 1, index_min):
        s += ls[index]
else:
    for index in range(index_min + 1, index_max):
        s += ls[index]
print(ls)
print(f'Мин. элемент: {min_num},Макс. элемент: {max_num}')
print(f'Сумма элементов: {s}')
