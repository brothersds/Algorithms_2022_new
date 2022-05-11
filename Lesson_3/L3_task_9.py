"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
# постановка задачи

import random

ROW = 5
COL = 4
MIN_ITEM = 0
MAX_ITEM = 100

matrix = []
r = 0
for i in range(ROW):
    matrix.append([])
    for _ in range(COL):
        matrix[i].append(random.randint(MIN_ITEM, MAX_ITEM))
        r += 1

# решение задачи
for line in matrix:
    print(*line, sep='\t')

max_matrix = None
for j in range(len(matrix[0])):
    min_matrix = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] < min_matrix:
            min_matrix = matrix[i][j]
    if max_matrix is None or max_matrix < min_matrix:
        max_matrix = min_matrix

print(f'Макс. элемент среди мин. элементов столбцов = {max_matrix}')
