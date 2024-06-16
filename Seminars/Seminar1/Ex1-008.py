# Задание №8
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Приме результата:
#      *
#     ***
#    *****
#   *******

SPACE = " "
STAR = "*"
ONE = 1

rows = int(input("Сколько рядов у ёлки?: "))
spaces = rows - ONE
stars = ONE

for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    stars += 2
    spaces -= 1