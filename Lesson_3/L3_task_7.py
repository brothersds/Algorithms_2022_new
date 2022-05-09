"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

# решение задачи
if ls[0] < ls[1]:
    min_one = 0
    min_two = 1
else:
    min_one = 1
    min_two = 0

for item in range(2, len(ls)):
    if ls[item] < ls[min_one]:
        var_num = min_one
        min_one = item
        if ls[var_num] < ls[min_two]:
            min_two = var_num
    elif ls[item] < ls[min_two]:
        min_two = item

print(f'Число {ls[min_one]} в ячейке {min_one}\nЧисло {ls[min_two]} в ячейке {min_two}')
