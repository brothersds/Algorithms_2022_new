"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

- Второй — без использования «Решета Эратосфена».
АНАЛИЗ: Странно, но решение решетом тратит намного больше времени на решение, чем решение перебором. N = 256

"""
# постановка задачи
import math
import timeit
import cProfile

N = 256

# решение задачи перебор


def func_not_erotosfen(number_in):
    my_list = [2]
    number = 3
    while len(my_list) < number_in:
        right_on = True
        for just in my_list.copy():
            if number % just == 0:
                right_on = False
                break
        if right_on:
            my_list.append(number)
        number += 1
    return my_list[-1]


print(f'Без использования решета Эратосфена: {func_not_erotosfen(N)}')

print(timeit.timeit('func_not_erotosfen(4)', number=1000, globals=globals()))       # 0.002257266000015079
print(timeit.timeit('func_not_erotosfen(8)', number=1000, globals=globals()))       # 0.006280703999891557
print(timeit.timeit('func_not_erotosfen(16)', number=1000, globals=globals()))     # 0.015564842999992834
print(timeit.timeit('func_not_erotosfen(32)', number=1000, globals=globals()))     # 0.04269251899995652
print(timeit.timeit('func_not_erotosfen(64)', number=1000, globals=globals()))     # 0.13333684999997786
print(timeit.timeit('func_not_erotosfen(128)', number=1000, globals=globals()))   # 0.4415852829997675
print(timeit.timeit('func_not_erotosfen(256)', number=1000, globals=globals()))   # 1.5775621239999964
cProfile.run('func_not_erotosfen(256)')
"""         3494 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 L4-task_2.py:21(func_not_erotosfen)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1618    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      255    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1617    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""


# решение задачи Решето Эратосфена


def func_erotosfen(number_in):
    number_primes = 0
    upper_limit = 2
    while number_primes <= number_in:
        number_primes = upper_limit / math.log(upper_limit)
        upper_limit += 1
    list_primes = [value for value in range(2, upper_limit)]
    for value in list_primes:
        if list_primes.index(value) <= value - 1:
            for just in range(2, len(list_primes)):
                if value * just in list_primes[value:]:
                    list_primes.remove(value * just)
        else:
            break
    return list_primes[number_in - 1]


print(f'C использования решета Эратосфена: {func_erotosfen(N)}')

print(timeit.timeit('func_erotosfen(4)', number=1000, globals=globals()))       # 0.0037077359997965686
print(timeit.timeit('func_erotosfen(8)', number=1000, globals=globals()))       # 0.01604514200016638
print(timeit.timeit('func_erotosfen(16)', number=1000, globals=globals()))     # 0.07406962599998224
print(timeit.timeit('func_erotosfen(32)', number=1000, globals=globals()))     # 0.3612713869997606
print(timeit.timeit('func_erotosfen(64)', number=1000, globals=globals()))     # 1.7283106270001554
print(timeit.timeit('func_erotosfen(128)', number=1000, globals=globals()))   # 8.935592619999625
print(timeit.timeit('func_erotosfen(256)', number=1000, globals=globals()))   # 49.41953388100001
cProfile.run('func_erotosfen(256)')
"""         4174 function calls in 0.050 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.050    0.050 <string>:1(<module>)
        1    0.045    0.045    0.050    0.050 L4-task_2.py:50(func_erotosfen)
        1    0.000    0.000    0.000    0.000 L4-task_2.py:56(<listcomp>)
        1    0.000    0.000    0.050    0.050 {built-in method builtins.exec}
      295    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1937    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      295    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
     1642    0.005    0.000    0.005    0.000 {method 'remove' of 'list' objects}"""
