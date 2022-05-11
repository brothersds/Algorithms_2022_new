"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
# постановка задачи
MIN_ITEM_1 = 2
MAX_ITEM_1 = 99
MIN_ITEM_2 = 2
MAX_ITEM_2 = 9

# решение задачи
dict_el = {key: 0 for key in range(MIN_ITEM_2, MAX_ITEM_2 + 1)}
for i in range(MIN_ITEM_1, MAX_ITEM_1):
    for el in range(MIN_ITEM_2, MAX_ITEM_2 + 1):
        if i % el == 0:
            dict_el[el] += 1
for key, item in dict_el.items():
    print(f'Цифре {key} кратно {item} чисел')
