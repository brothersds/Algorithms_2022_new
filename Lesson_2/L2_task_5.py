"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
https://drive.google.com/file/d/1dwhQvcBzeoUEK2onaSP5wYbwg6QopT7-/view?usp=sharing
"""


def calc(a, b):
    if a == b:
        return f'{a} is {chr(a)}'
    if a < b:
        return f'{a} is {chr(a)}, {calc(a + 1, b)}'


n = 32
step = 0
for i in range(32, 127):
    if i == n:
        if i == 122:
            step = 5
        else:
            step = 9
        res = calc(i, i + step)
        print(res)
        n += 10
