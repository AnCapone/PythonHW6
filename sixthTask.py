# Завдання 6. Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як
# параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.
import listGeneration


def exponentiation_elements(input_list: list, pow):
    output_list = []
    for num in input_list:

        output_list.append(num ** pow)

    return output_list


inputList = listGeneration.generate_list()
print(f"Вхідний список: {inputList}")
while True:
    try:
        pow = int(input("Введіть число до степені якого треба піднести елементи списку: "))
        if pow < 0:
            print("Введіть ціле позитивне число!")
            continue
        break
    except ValueError as error:
        print("Введіть ціле число!")
        continue

print(f"Список, підведений до степені: {exponentiation_elements(inputList, pow)}")