"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(a, b):
    k = 0
    while a > 0:
        elements = int(input("Введите число: "))
        for el in str(elements):
            if el == str(b):
                k += 1
        a -= 1
    return k


print("Введите кол-во вводимых чисел и цифру, которую необходимо подсчитать")
num_user = int(input("Введите кол-во вводимых чисел: "))
e = int(input("Введите цифру, которую необходимо подсчитать: "))
res = calc(num_user, e)
print(f'Цифра {e} встречается {res} раз')
