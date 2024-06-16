# Задание №9
# Выведите в консоль таблицу умножения от 2x2 до 9x10 как на школьной тетрадке

LOWER_LIMIT = 2
UPPER_LIMIT = 11
COLUMNS = 4
for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS):
    for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
        for num_1 in range(row, row + COLUMNS):
            print(f"{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}", end='\t')
        print()
    print()