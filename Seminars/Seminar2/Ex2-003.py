# Задание №3
# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам исчисления.
# Избегайте магических чисел.
# Добавьте аннотацию типов там, где это возможно.

DIV_BIN = 2
DIV_OCT = 8

user_number: int = int(input("Введите целое число: "))
for div in (DIV_BIN, DIV_OCT):
    num = user_number
    result: str = ''
    while num > 0:
        result = str(num % div) + result
        num //= div
    print(f"Для числа {user_number} в {div} системе результат: {result}")