"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict.
"""

while True:
    month = input('Введите номер месяца (число от 1 до 12): ')
    if month.isdigit():
        month = int(month)
        break

    print('Произошла ошибка. Пожалуйста, попробуйте еще раз.')

# Решение с использованием list

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print(f'{month}-й месяц года - это зима.')
elif month in spring:
    print(f'{month}-й месяц года - это весна.')
elif month in summer:
    print(f'{month}-й месяц года - это лето.')
elif month in autumn:
    print(f'{month}-й месяц года - это осень.')
else:
    print('Месяца с таким номером не существует в природе!')

# Решение с использованием dict

season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if month in season_dict.keys():
    print(f'{month}-й месяц года - это {season_dict.get(month)}.')
else:
    print('Месяца с таким номером не существует в природе!')

"""Решение преподавателя

season_list = ('зима', 'весна', 'лето', 'осень')  # Самое оптимальное решение
season_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}

season_dict2 = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

user_month_num = 12
season_idx = user_month_num // 3 % 4  # 3 - число месяцев в сезоне, 4 - число сезонов, % 4 используется исключительно
# для того, чтобы 12 сезон отнести к зиме, для остальных месяцев целочисленное деление на 3 дает номер сезона,
# который является индексом сезона в season_list

for key, value in season_dict.items():
    if user_month_num in value:
        print(key)
        break

print(season_idx)
print(season_list[season_idx])
"""
