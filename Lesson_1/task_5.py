"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
sim_r1 = str(input("Введите первый символ: "))
sim_r2 = str(input("Введите второй символ: "))

sim_r1_ord = ord(sim_r1.lower())
sim_r2_ord = ord(sim_r2.lower())

num1 = sim_r1_ord - ord('a')
num2 = sim_r2_ord - ord('a')
if num1 < num2:
    num3 = num2 - num1
else:
    num3 = num1 - num2
print(f'Первое число находится на {num1 + 1} месте алфавита')
print(f'Второе число находится на {num2 + 1} месте алфавита')
print(f'Между первым и вторым числом {num2 + 1} букв алфавита')
