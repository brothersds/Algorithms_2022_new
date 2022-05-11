"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
матрицу.
"""

# постановка задачи

# решение задачи
row = 5
col = 4
matrix = []
for i in range(row):
    rows = []
    sum_ = 0

    for j in range(col - 1):
        num = int(input(f'{i}-я строка, {j}-й элемент : '))
        sum_ += num
        rows.append(num)

    rows.append(sum_)
    matrix.append(rows)

for line in matrix:
    for item in line:
        print(f'{item:>10_}', end='')
    print()
