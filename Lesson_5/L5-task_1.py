"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple


def factory_input(number, factory_array=[]):
    total_income = 0
    i = 0
    while True:
        if i == number:
            break
        else:
            factory_name = input(f'Введите название {i + 1}-го предприятия: ')
            income_q1 = int(input("Введите прибыль за первый картал: "))
            income_q2 = int(input("Введите прибыль за второй картал: "))
            income_q3 = int(input("Введите прибыль за третий картал: "))
            income_q4 = int(input("Введите прибыль за четвертый картал: "))
            income_year = income_q1 + income_q2 + income_q3 + income_q1
            total_income += income_year
            factory_array.append(Factory(factory_name=factory_name, income_q1=income_q1, income_q2=income_q2,\
                                         income_q3=income_q3, income_q4=income_q4, income_year=income_year))
            i += 1
    return total_income, factory_array


def total_average(total, quanity):
    total_avg = total // quanity
    return total_avg


def factory_income_upper_avg(arr, total_avg, array_up=[]):
    for Factory in arr:
        if Factory.income_year >= total_avg:
            array_up.append(Factory.factory_name)
    return array_up


def factory_income_lower_avg(arr, total_avg, array_low=[]):
    for Factory in arr:
        if Factory.income_year < total_avg:
            array_low.append(Factory.factory_name)
    return array_low


factory_calc = int(input("Введите кол-во предприятий: "))
Factory = namedtuple('Factory', 'factory_name income_q1 income_q2 income_q3 income_q4 income_year')
array = factory_input(factory_calc)
income_avg = total_average(array[0], factory_calc)
income_upper_avg = factory_income_upper_avg(array[1], income_avg)
income_lower_avg = factory_income_lower_avg(array[1], income_avg)
print(f'Компании с прибылью выше средней {income_avg}: {income_upper_avg}')
print(f'Компании с прибылью ниже средней {income_avg}: {income_lower_avg}')
