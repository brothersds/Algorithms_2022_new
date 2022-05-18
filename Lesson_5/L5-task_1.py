"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple

NAME_1 = 'roga'
NAME_2 = 'kopyta'
INCOME_Q1_1 = 1000
INCOME_Q2_1 = 1000
INCOME_Q3_1 = 1000
INCOME_Q4_1 = 1000
INCOME_Q1_2 = 2000
INCOME_Q2_2 = 2000
INCOME_Q3_2 = 2000
INCOME_Q4_2 = 2000

factory_calc = int(input("Введите кол-во предприятий: "))
Factory = namedtuple('Factory', 'name income_q1 income_q2 income_q3 income_q4 income_year')

array_data = []
total_income = 0

while True:
    if factory_calc == 0:
        break
    else:
        factory_name = input("Введите название предприятия: ")
        income_q1 = int(input("Введите прибыль за первый картал: "))
        income_q2 = int(input("Введите прибыль за второй картал: "))
        income_q3 = int(input("Введите прибыль за третий картал: "))
        income_q4 = int(input("Введите прибыль за четвертый картал: "))
        income_year = income_q1 + income_q2 + income_q3 + income_q1
        total_income += income_year
        array_data.append(Factory(factory_name, income_q1, income_q2, income_q3, income_q4, income_year))
        factory_calc -= 1


print(array_data)
