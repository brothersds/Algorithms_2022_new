"""
Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число,
● случайное вещественное число, ● случайный символ. Для каждого из трех случаев пользователь задает свои границы
диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
вывести на экран любой символ алфавита от 'a' до 'f' включительно.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
from random import randint
from random import uniform

print("Введите диапазоны для поиска случайного значения")
a_r1 = int(input("Введите первое целое число: "))
a_r2 = int(input("Введите второе целое число: "))
b_r1 = float(input("Введите первое вещественное число: "))
b_r2 = float(input("Введите второе вещественное число: "))
sim_r1 = str(input("Введите первый символ: "))
sim_r2 = str(input("Введите второй символ: "))

if a_r1 < a_r2:
    a = randint(a_r1, a_r2)
else:
    a = randint(a_r2, a_r1)

if b_r1 < b_r2:
    b = uniform(b_r1, b_r2)
else:
    b = uniform(b_r2, b_r1)

sim_r1_ord = ord(sim_r1)
sim_r2_ord = ord(sim_r2)

if sim_r1_ord < sim_r2_ord:
    simbol = chr(randint(sim_r1_ord, sim_r2_ord))
else:
    simbol = chr(randint(sim_r2_ord, sim_r1_ord))

print(f'Случайное целое число: {a}')
print(f'Случайное вещественное число: {b}')
print(f'Случайный символ: {simbol}')
