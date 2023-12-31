# Завдання 4. Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість
# видаленних елементів.
import listGeneration


def delete_current_item(input_list: list):
    amount = 0  # Оголошуємо лічильник
    while True:  # Блок введення значення для видалення з перехопленням помилки неправильного значення
        try:
            number_to_delete = int(input("Введіть значення для видалення: "))
            break
        except ValueError as error:
            print("Невірне введення! Введіть ціле число!")
            continue

    while number_to_delete in input_list:  # Блок видалення елементу або елементів. Цикл працює до тих пір доки в
                                           # списку присутнє введене значення
        input_list.remove(number_to_delete)
        amount += 1
    return amount


baseList = listGeneration.generate_list()
print(f"Список: {baseList}")
amountDeleted = delete_current_item(baseList)

if amountDeleted == 0:
    print("Введене значення відсутнє в списку. Нічого не видалено.")  # Перевірка кількості видалених. Якщо нуль
                                                                      # виводимо повідомлення.
else:
    print(f"Кількість видалених: {amountDeleted}")  #Якщо більше за нуль, виводимо кількість
