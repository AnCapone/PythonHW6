# Завдання 2: Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.
import listGeneration


# def generate_list(num_elements: int, min_number: int, max_number: int) -> list:
#     return [random.randint(min_number, max_number) for i in range(num_elements)]


def find_minimum(input_list: list):
    minimum = input_list[0]
    for i in input_list:
        if i < minimum:
            minimum = i
    return minimum


generatedList = listGeneration.generate_list()
print(f"List: {generatedList}")
print(f"Minimum in this list is: {find_minimum(generatedList)}")
