# Виведемо функцію генерації списку випадкових чисел в окремий файл в проекті, щоб звертатись до нього в усіх завданнях
# Додамо запит на введення мінімального, максимального значення для генерації та кількість елементів списку
import random


def generate_list() -> list:
    while True:
        try:
            amount = int(input("Введіть кількість елементів списку: "))
            if amount < 1:
                print("Кількість елементів має бути більшою за 0!")
                continue
            break
        except ValueError as error:
            print("Невірне значення кількості! Введіть ціле число більше за 0!")
            continue

    while True:
        try:
            min_number = int(input("Введіть мінімально можливе ціле значення елементу списка: "))
            break
        except ValueError as error:
            print("Введіть ціле число!")
            continue

    while True:
        try:
            max_number = int(input("Введіть максимально можливе ціле значення елементу списка: "))
            break
        except ValueError as error:
            print("Введіть ціле число!")
            continue

    if min_number > max_number:
        min_number, max_number = max_number, min_number

    return [random.randint(min_number, max_number) for i in range(amount)]
