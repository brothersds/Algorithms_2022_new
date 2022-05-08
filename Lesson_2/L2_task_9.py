"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
сумму его цифр.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(elements):
    s = 0
    for el in str(elements):
        s += int(el)
    return s


k = 0
n = 1
m = 0
print("Введите натуральное число или 0 для выхода и подсчета")
while n != 0:
    n = int(input("Введите натуральное число: "))
    res = calc(n)
    if k < int(res):
        k = int(res)
        m = n
    else:
        k = k
print(f'Максимальная сумма равна {k} для числа {m}')
