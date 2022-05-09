"""
Определить, какое число в массиве встречается чаще всего.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# решение задачи
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
