"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(n):
    e = 1
    s = 0
    for i in range(n):
        s += e
        e /= -2
    return f'Сумма элементов ряда: {s}'


num_user = int(input("Введите кол-во элементов ряда: "))
sum_elem = calc(num_user)
print(sum_elem)
