"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

import sys
from collections import deque


def func_task_one():
    x = list(input('Введите 1-е шестнадцатиричное число: ').upper())
    y = list(input('Введите 2-е шестнадцатиричное число: ').upper())
    hex_dec = dict(
        zip((list([str(i) for i in range(0, 10, 1)]) + list('ABCDEF')), list([str(i) for i in range(0, 16, 1)])))
    dec_hex = dict(
        zip(list([str(i) for i in range(0, 16, 1)]), (list([str(i) for i in range(0, 10, 1)]) + list('ABCDEF'))))
    res_sum = deque()
    if len(x) > len(y):
        x, y = deque(x), deque(y)
    else:
        y, x = deque(x), deque(y)
    transfer_number = 0
    for i in range(len(x)):
        if not y:
            res = int(hex_dec[x.pop()]) + transfer_number
        else:
            res = int(hex_dec[x.pop()]) + int(hex_dec[y.pop()]) + transfer_number
        transfer_number = 0
        if res >= 16:
            res_sum.appendleft(dec_hex[str(res - 16)])
            transfer_number = 1
        else:
            res_sum.appendleft(dec_hex[str(res)])
    if transfer_number == 1:
        res_sum.appendleft('1')

    print('Сумма чисел равна: ', f'{list(res_sum)}')
    memory_size = func_calc_memory(locals())

    return memory_size


def func_calc_memory(data):
    sum_size = 0
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                sum_size += sys.getsizeof(key, default=0)
                sum_size += sys.getsizeof(value, default=0)
        elif not isinstance(data, str):
            for item in data:
                sum_size += sys.getsizeof(item, default=0)
    return sum_size


print('Суммарная выделенная память под переменные: ', func_task_one())
