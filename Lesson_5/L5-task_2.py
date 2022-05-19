"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def func_hex_sum(hex_dec, dec_hex, x, y):
    result_sum = deque()
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
        if res > 16:
            result_sum.appendleft(dec_hex[str(res - 16)])
            transfer_number = 1
        else:
            result_sum.appendleft(dec_hex[str(res)])
    if transfer_number == 1:
        result_sum.appendleft('1')
    return list(result_sum)


# a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
# b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
# print(a, b)
task_dec = list([str(i) for i in range(0, 16, 1)])
task_hex = list('ABCDEF')
hexdec = dict(zip((task_dec[:10] + task_hex), task_dec))
dechex = dict(zip(task_dec, (task_dec[:10] + task_hex)))
# a = list('12FD')
# b = list('234')
a = list('12FD')
b= list('234')

result_sum = func_hex_sum(hexdec, dechex, a, b)
print('Сумма чисел равна', f'{result_sum}')

# print(*a, '+', *b, '=', *sum_hex(a, b))

