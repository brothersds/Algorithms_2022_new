"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
print("Введите координаты двух точек для прямой вида Y = k*X +b")
X1 = int(input("Введите координаты X1: "))
Y1 = int(input("Введите координаты Y1: "))
X2 = int(input("Введите координаты X2: "))
Y2 = int(input("Введите координаты Y2: "))
if X1 != X2:
    k = (Y2 - Y1) / (X2 - X1)
    b = Y1 - (k * X1)
    if b > 0:
        print(f'Уравнение имеет вид Y = {k}*X+{b}')
    else:
        print(f'Уравнение имеет вид Y = {k}*X{b}')
else:
    print("Нет решений")
