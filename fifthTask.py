# Завдання 5. Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
import listGeneration


def find_intersections(first_list: list, second_list: list) -> list:
    return list(set(first_list).intersection(set(second_list))) # Приводимо перший список до множини, використовуємо
                                                                 # метод множин intersection. Використовуєм як
                                                                 # параметр другий список, приведений до множини.
                                                                 # Результат приводимо до списка


firstList = listGeneration.generate_list()
print(f"Перший список: {firstList}")
secondList = listGeneration.generate_list()
print(f"Другий список: {secondList}")

outputList = find_intersections(firstList, secondList)
if len(outputList) == 0:
    print("Відсутні спільні елементи списків!")
else:
    print(f"Список спільних елементів: {outputList}")