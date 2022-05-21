"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def func_hex_sum(hex_dec, dec_hex, x, y):
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


def func_to_dec(hex_dec, x):
    decimal_number = 0
    length_hex = len(x) - 1
    for digit in x:
        decimal_number += int(hex_dec[digit])*16**length_hex
        length_hex -= 1
    return decimal_number


def func_to_hex(dec_hex, x):
    x_hex = x % 16
    rest = x // 16
    if rest == 0:
        return dec_hex[str(x_hex)]
    return func_to_hex(dec_hex, rest) + dec_hex[str(x_hex)]


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

task_dec = list([str(i) for i in range(0, 16, 1)])
task_hex = list('ABCDEF')
hexdec = dict(zip((task_dec[:10] + task_hex), task_dec))
dechex = dict(zip(task_dec, (task_dec[:10] + task_hex)))

result_sum = func_hex_sum(hexdec, dechex, a, b)
result_mul = func_to_hex(dechex, (func_to_dec(hexdec, a) * func_to_dec(hexdec, b)))
res_x = deque()
for i in result_mul:
    if len(result_mul) != 0:
        res_x.append(i)

print('Сумма чисел равна:           ', f'{result_sum}')
print('Произведение чисел равно:    ', f'{list(res_x)}')
