"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""
import random


def calc(a, b):
    if a == b:
        return f'Ты угадал'
    if a > b:
        return f'Меньше'
    return f'Больше'


print("Задано целое число от 0 до 100")
num_rand = random.randint(0, 100)
n = 10
while n > 0:
    num_user = int(input(f'Введите Ваш вариант числа, у Вас {n} попыток :'))
    res = calc(num_user, num_rand)
    print(res)
    if res in str('Ты угадал'):
        break
    n -= 1
if n > 0:
    pass
else:
    print(f'Попытки закончились, правильное число : {num_rand}')
