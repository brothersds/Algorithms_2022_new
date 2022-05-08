"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc_one(a):
    s = 0
    while a > 0:
        s += 1
        a -= 1
    return s


def calc_two(a):
    s = a * (a - 1) / 2
    return s


n = int(input("Введите любое натуральное число: "))
res_1 = calc_one(n)
res_2 = calc_two(n)
if res_1 == res_2:
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")
