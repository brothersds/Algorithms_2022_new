"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1xpdjGb4dnycOuNAA8Te81iUPAOYEXlcV/view?usp=sharing
"""
print("Поиск суммы и произведения чисел трехзначного числа")
num_user = int(input("Введите трехзначное число: "))
num_one = num_user % 10
num_two = (num_user % 100) // 10
num_three = (num_user // 100)
sum_num = (num_one + num_two + num_three)
mul_num = (num_one * num_two * num_three)
print(f'Сумма чисел равна: {sum_num}')
print(f'Произведение чисел равно: {mul_num}')
