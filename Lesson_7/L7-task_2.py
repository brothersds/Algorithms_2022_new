"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def func_merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle_arr = len(arr) // 2
    left_arr = func_merge_sort(arr[:middle_arr])
    right_arr = func_merge_sort(arr[middle_arr:])
    return func_merge(left_arr, right_arr)


def func_merge(left_list, right_list):
    new_arr = []
    index_left = 0
    index_right = 0
    for _ in range(len(left_list) + len(right_list)):
        if index_left < len(left_list) and index_right < len(right_list):
            if left_list[index_left] <= right_list[index_right]:
                new_arr.append(left_list[index_left])
                index_left += 1
            else:
                new_arr.append(right_list[index_right])
                index_right += 1
        else:
            if index_left == len(left_list):
                new_arr.append(right_list[index_right])
                index_right += 1
            else:
                if index_right == len(right_list):
                    new_arr.append(left_list[index_left])
                    index_left += 1
    return new_arr


# постановка задачи
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]

# решение задачи
print(f'Исходный массив:\n{array}')
new_array = func_merge_sort(array)
print(f'Отсортированный массив:\n{new_array}')
