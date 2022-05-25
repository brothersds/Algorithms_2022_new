"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""


def func_string_hash(user_str):
    user_str = str(user_str).lower()
    hash_set = set()
    for i in range(len(user_str) + 1):
        for j in range(i + 1, len(user_str) + 1):
            h = hash(user_str[i:j].encode('utf-8'))
            hash_set.add(h)
    return len(hash_set)


# постановка задачи
user_string = 'sova'

# решение задачи
print(f'Количество различных подстрок в строке {user_string}: {func_string_hash(user_string) - 1}')
