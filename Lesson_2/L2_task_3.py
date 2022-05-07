"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(a):
    b = ''
    while a > 0:
        b += str(a % 10)
        a //= 10
    return b


num_user = int(input("Введите целое натуральное число: "))
inv_number = calc(num_user)
print(inv_number)
