"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
# Сортировка кучей


def func_heap_sort(arr):
    for i in range(len(arr), -1, -1):
        func_heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        func_heapify(arr, i, 0)
    return


def func_heapify(arr_heap, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and arr_heap[left_child] > arr_heap[largest]:
        largest = left_child
    if right_child < heap_size and arr_heap[right_child] > arr_heap[largest]:
        largest = right_child
    if largest != root_index:
        arr_heap[root_index], arr_heap[largest] = arr_heap[largest], arr_heap[root_index]
        func_heapify(arr_heap, heap_size, largest)
    return


# постановка задачи
M_ITEM = 5
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range((2 * M_ITEM) + 1)]

# решение задачи
print(f'Исходный массив:\n{array}')
func_heap_sort(array)
print(f'Отсортированный массив:\n{array}')
print(f'Медиана массива: {array[len(array) // 2]}')
