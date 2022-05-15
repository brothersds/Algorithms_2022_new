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

ЗАДАЧА: Выбрана задача Lesson 3 task 4 ()
Определить, какое число в массиве встречается чаще всего.
"""

# постановка задачи
import random
import timeit
import cProfile

SIZE = 10
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
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=100, globals=globals()))       # 0.00026350699954491574
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=100, globals=globals()))       # 0.0004565919998640311
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=100, globals=globals()))       # 0.0010487099998499616
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=100, globals=globals()))     # 0.0014971609998610802
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=100, globals=globals()))     # 0.0030309499998111278
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=100, globals=globals()))     # 0.006594675000087591
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=100, globals=globals()))   # 0.013830831000632315
print(timeit.timeit('func_one([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=100, globals=globals()))   # 0.04301830099939252
cProfile.run('func_one([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')

"""         3062 function calls (2806 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    257/1    0.000    0.000    0.000    0.000 L4-task_1.py:29(func_one)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1025    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        2    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      256    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      492    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""

if result_1 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_1[0][0]} встречается {result_1[1][0]} раз(-a)')

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
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=100, globals=globals()))       # 0.00016694599980837665
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=100, globals=globals()))       # 0.00028080399988539284
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=100, globals=globals()))       # 0.0005305389995555743
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=100, globals=globals()))     # 0.001022504000502522
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=100, globals=globals()))     # 0.0020479909999266965
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=100, globals=globals()))     # 0.0049278070000582375
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=100, globals=globals()))   # 0.008066028000030201
print(timeit.timeit('func_two([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=100, globals=globals()))   # 0.01657246299964754
cProfile.run('func_two([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')
"""         1542 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 L4-task_1.py:61(func_two)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      513    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""

if result_2 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_2[0]} встречается {result_2[1]} раз(-a)')

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
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 2 // 2) for _ in range(2)])', number=100, globals=globals())) # 0.00018386000010650605
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 4 // 2) for _ in range(4)])', number=100, globals=globals())) # 0.00031163600033323746
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 8 // 2) for _ in range(8)])', number=100, globals=globals())) # 0.0005824689997098176
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 16 // 2) for _ in range(16)])', number=100, globals=globals())) # 0.0011469270002635312
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 32 // 2) for _ in range(32)])', number=100, globals=globals())) # 0.0022144159993331414
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 64 // 2) for _ in range(64)])', number=100, globals=globals())) # 0.004459098000552331
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 128 // 2) for _ in range(128)])', number=100, globals=globals())) # 0.00893006099977356
print(timeit.timeit('func_three([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])', number=100, globals=globals())) # 0.021684649999770045
cProfile.run('func_three([random.randint(MIN_ITEM, 256 // 2) for _ in range(256)])')
"""         1786 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 L4-task_1.py:92(func_three)
      256    0.000    0.000    0.000    0.000 random.py:200(randrange)
      256    0.000    0.000    0.000    0.000 random.py:244(randint)
      256    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      257    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      256    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      500    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}"""

if result_3 is None:
    print("Нет совпадений")
else:
    print(f'Число {result_3[0]} встречается {result_3[1]} раз(-a)')
