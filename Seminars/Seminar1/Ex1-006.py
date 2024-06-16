# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

BIG_LEAP_YEAR = 400
LARGE_NOT_BIG_YEAR = 100
SMALL_LEAP_YEAR = 4
MULTIPLE = 0
REFORM = 1582

year = int(input("Введите год: "))
if year < REFORM:
    result = f'Год  {year} до ввода Григорианского календаря'
elif year % BIG_LEAP_YEAR:
    result = f'Год {year} високосный'
elif year % LARGE_NOT_BIG_YEAR:
    result = f'Год {year} не високосный'
elif year % SMALL_LEAP_YEAR:
    result = f'Год {year} високосный'
else:
    result = f'Год {year} не високосный'

print(result)