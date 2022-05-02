"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
num_user = int(input("Введите номер буквы в алфавите: "))
if 0 < num_user < 27:
    sim_user = chr(ord('a') + num_user - 1)
    print(f'Введенный символ: {sim_user}')
else:
    print("Нет решений")
