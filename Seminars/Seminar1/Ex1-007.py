# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двухзначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двухзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100


num = LOWER_LIMIT - ONE
while num > UPPER_LIMIT or num < LOWER_LIMIT:
    num = int(input(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))

if num < TEN:
    result = f"Число {num} - цифра. Её квадрат равен {num * num}"
elif num < HUNDRED:
    f_num = num // TEN
    s_num = num % TEN
    result = f"Число {num} - двухзначное. Произведение цифр равно {f_num * s_num}"
else:
    f_num = num // HUNDRED
    s_num = num // TEN % TEN
    t_num = num % TEN
    result = f"Число {num} - трёхзначное. Зеркальное отображение равно {t_num * HUNDRED + s_num * TEN + f_num}"

print(result)