# Завдання 1: Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

import random


def generate_list(num_elements: int, min_number: int, max_number: int) -> list:
    return [random.randint(min_number, max_number) for i in range(num_elements)]


def calculate_product(numbers_list: list):
    prod = 1
    for i in numbers_list:
        prod *= i

    return prod


generatedList = generate_list(5, 7, 50)
print(f"List: {generatedList}")
print(f"Product: {calculate_product(generatedList)}")
