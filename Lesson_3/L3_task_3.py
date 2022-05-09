"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

# решение задачи
min_num = max_num = ls[0]
index_min = 0
index_max = 0
en_ls = enumerate(ls)
for index, item in en_ls:
    if item < min_num:
        index_min = index
        min_num = item
    elif item > max_num:
        index_max = index
        max_num = item
ls[index_min], ls[index_max] = ls[index_max], ls[index_min]
print(ls)
