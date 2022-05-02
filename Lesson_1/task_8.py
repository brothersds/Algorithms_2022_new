"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
year_user = int(input("Введите год: "))

if year_user % 400 == 0 or (year_user % 100 != 0 and year_user % 4 == 0):
    print(f'Год {year_user} високосный')
else:
    print(f'Год {year_user} не високосный')
