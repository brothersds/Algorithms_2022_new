"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

АНАЛИЗ: Решения с использованием циклов показали примерно одинаковые результаты, но по времени ручше цикл FOR, а по
вызову функции лучше цикл WHILE. Решение с использованием рекурсии затрачивает больше времени и, чем больше попыток, тем
существенее временной диапазон. Мой выбор цикл FOR, так как он удобен для чтения кода и быстрее выполняется.

ЗАДАЧА: Выбрана задача Lesson 3 task 4 (), N = 256, цикл повторов 10_000
Определить, какое число в массиве встречается чаще всего.
"""

# постановка задачи
import random
import timeit
import cProfile

SIZE = 256
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 2) for _ in range(SIZE)]
print(array)

# решение задачи 1


def func_one(arr, res={}, repeat=[1], item=[]):
    if len(arr) == 0:
        return
    else:
        first_el = arr[len(arr) - 1]
        if not type(first_el) == list:
            res[first_el] = res.get(first_el, 0) + 1
            if repeat[len(repeat) - 1] < res[first_el]:
                item.clear(), item.append(first_el)
                repeat.clear(), repeat.append(res[first_el])
            func_one(arr[:len(arr) - 1])
        return item, repeat


result_1 = func_one(array)
if result_1 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_1[0][0]} встречается {result_1[1][0]} раз(-a)')

print(timeit.timeit('func_one([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=10000, globals=globals()))       # 0.025712837999890326
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=10000, globals=globals()))       # 0.04376020300014716
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=10000, globals=globals()))       # 0.08201802300004601
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=10000, globals=globals()))     # 0.159077735999972
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=10000, globals=globals()))     # 0.3152050539999891
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=10000, globals=globals()))     # 0.6332070539999677
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=10000, globals=globals()))   # 1.2960195970001678
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=10000, globals=globals()))   # 2.8366463149998253
cProfile.run('func_one([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')

"""         3103 function calls (2847 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    257/1    0.000    0.000    0.000    0.000 L4-task_1.py:32(func_one)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1025    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        6    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      256    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      525    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""


# решение задачи 2


def func_two(arr, count = {}, repeat = 1, num = None):
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        if count[item] > repeat:
            repeat = count[item]
            num = item
    return num, repeat


result_2 = func_two(array)
if result_2 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_2[0]} встречается {result_2[1]} раз(-a)')

print(timeit.timeit('func_two([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=10000, globals=globals()))       # 0.015949405000128536
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=10000, globals=globals()))       # 0.02645604600002116
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=10000, globals=globals()))       # 0.05082072499999413
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=10000, globals=globals()))     # 0.09753058000001147
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=10000, globals=globals()))     # 0.2018325740000364
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=10000, globals=globals()))     # 0.38526937599999656
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=10000, globals=globals()))   # 0.7589551710000251
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=10000, globals=globals()))   # 1.5142625460000545
cProfile.run('func_two([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')
"""         1538 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 L4-task_1.py:86(func_two)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      509    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""

# решение задачи 3


def func_three(arr, count = {}, repeat = 1, n = 0, num = 0):
    while n < len(arr):
        i = arr[n]
        n += 1
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > repeat:
            repeat = count[i]
            num = i
    return num, repeat


result_3 = func_three(array)
if result_3 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_3[0]} встречается {result_3[1]} раз(-a)')

print(timeit.timeit('func_three([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=10000, globals=globals())) # 0.017393726000136667
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=10000, globals=globals())) # 0.02905826000005618
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=10000, globals=globals())) # 0.055166103999908955
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=10000, globals=globals())) # 0.10551767499987363
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=10000, globals=globals())) # 0.21629688200005148
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=10000, globals=globals())) # 0.41261344600002303
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=10000, globals=globals())) # 0.8170351680000749
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=10000, globals=globals())) # 1.6486714630000279
cProfile.run('func_three([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')
"""         1780 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 L4-task_1.py:132(func_three)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      257    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      494    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""
