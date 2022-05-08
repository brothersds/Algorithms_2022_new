"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(a):
    k1 = k2 = 0
    while a > 0:
        if a % 2 == 0:
            k2 += 1
        else:
            k1 += 1
        a = a // 10
    return f'нечетных чисел: {k1} четных чисел: {k2}'


num_user = int(input("Введите целое натуральное число: "))
res = calc(num_user)
print(res)

