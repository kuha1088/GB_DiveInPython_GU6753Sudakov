# Задание №3
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS_NUMBER_IN_TEST = 10
INPUT_REQUEST_1 = "Угадайте число: "
INPUT_REQUEST_2 = "Попробуйте ещё раз. Введите число: "
INPUT_ERROR_TEXT = "Число должно быть больше ноля и менее 1000"
INPUT_SUCCESSFULL_TEXT = ""
RESULT_MSG_SUCCESS = "Ура! Вы отгадали!"
RESULT_MSG_DEFEAT = "Увы! Повезёт в другой раз!"

# Генерация "загаданного" числа
test_number = randint(LOWER_LIMIT, UPPER_LIMIT)
print(test_number)
user_number = int(input(INPUT_REQUEST_1))
user_attempts = ATTEMPTS_NUMBER_IN_TEST

while True:
    if user_number != test_number:
        if user_number > test_number:
            print("Меньше...")
        else:
            print("Больше...")
    else:
        print(RESULT_MSG_SUCCESS)
        break
    if user_attempts == 0:
        print(RESULT_MSG_DEFEAT)
    user_number = int(input(INPUT_REQUEST_2))
    user_attempts -= 1