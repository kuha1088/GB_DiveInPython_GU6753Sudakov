# Задание №2
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

UPPER_LIMIT = 100000
ZERO = 0
INPUT_ERROR_TEXT = "Число должно быть больше ноля и менее 100 тысяч"
INPUT_SUCCESSFULL_TEXT = ""
RESULT_MSG_PRIME_NUMBER = "Число является простым"
RESULT_MSG_NOT_PRIME_NUMBER = "Число НЕ является простым"

user_number = 0


# Цикл, который просит пользователя ввести значение, пока не будет введено значение, удовлетворяющее условию
while True:
    user_number = int(input("Введите число больше ноля и менее 100 тысяч: "))
    if user_number > 0 and user_number < 100000:
        print(INPUT_SUCCESSFULL_TEXT)
        break
    else:
        print(INPUT_ERROR_TEXT)

# Проверка числа простое / не простое
k = 0
for i in range(2, user_number // 2+1):
    if (user_number % i == 0):
        k = k+1
if (k <= 0):
    print(RESULT_MSG_PRIME_NUMBER)
else:
    print(RESULT_MSG_NOT_PRIME_NUMBER)
