"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

# решение задачи
num = float('-inf')
index_num = 0
for index, item in enumerate(ls):
    if num < item < 0:
        num = item
        index_num = index
if num == float('-inf'):
    print("Решения нет")
else:
    print(f'Макс. отрицательное число {num} под индексом {index_num}')
