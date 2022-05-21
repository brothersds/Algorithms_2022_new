"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

from collections import deque


def func_hex_sum(x, y):
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
    return list(res_sum)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print('Сумма чисел равна: ', f'{func_hex_sum(a, b)}')
