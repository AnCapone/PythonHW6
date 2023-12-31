import random


def generate_list(amount: int, min_number: int, max_number: int) -> list:
    return [random.randint(min_number, max_number) for i in range(amount)]


def find_simple_numbers(input_list: list):  # не визначаємо тип значення, що повертається, щоб була можливість повернути
                                            # повідомлення про відсутність простих чисел в списку
    output_list = []
    input_list = set(input_list)  # приведемо вхідний список до множини, щоб прибрати дублі
    for number in input_list:
        if number < 2:
            continue
        is_simple = True
        for i in range(2, number):
            if number % i == 0:
                is_simple = False
        if is_simple:
            output_list.append(number)
    if len(output_list) == 0:  # перевіряємо кількість елементів в вихідному списку, якщо 0, то виводимо повідомлення,
                               # що прості числа відсутні
        return "No simple numbers in list!"
    return output_list


baseList = generate_list(min_number=1, max_number=50, amount=30)
print(f"List: {baseList}")
print(f"List with simple numbers: {find_simple_numbers(baseList)}")  # друкуємо список з простими числами
print(f"Amount of simple numbers: {len(find_simple_numbers(baseList))}")  # рахуємо кількість елементів списку з
                                                                          # простими числами
