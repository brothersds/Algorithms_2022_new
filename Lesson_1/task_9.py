"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
print("Введите три разных числа")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 < num2 < num3 or num3 < num2 < num1:
    print(f'Среднее число: {num2}')
elif num2 < num1 < num3 or num3 < num1 < num2:
    print(f'Среднее число: {num1}')
else:
    print(f'Среднее число: {num3}')
