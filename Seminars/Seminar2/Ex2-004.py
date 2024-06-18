# Задание №4
# Напишите проргамму, которая вычисляет площадь круга и длину окружности по введенному диаметру.
# Диаметр не превышает 1000 у.е.
# Точность высилений должна составить не менее 42 знаков после запятой

from math import pi
import decimal

decimal.getcontext().prec = 42
PI = decimal.Decimal(pi)
diameter = decimal.Decimal(input("Введите диаметр: "))
while diameter > 1000:
    print("Диаметр не должен быть больше 1000")
    diameter = decimal.Decimal(input("Введите диаметр: "))

square = PI * (diameter / 2) ** 2
length = PI * diameter
print(f"Площадь равна {square}\nДлина равна {length}")