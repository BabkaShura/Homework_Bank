from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.

    :param data: Строка, содержащая тип и номер (например, "Visa Platinum 7000792289606361").
    :return: Замаскированная строка.
    """
    parts = data.rsplit(" ", 1)  # Разделяем строку, отделяя номер от названия
    if len(parts) != 2:
        raise ValueError("Некорректный формат данных")

    name, number = parts[0], parts[1]

    if number.isdigit():
        if len(number) == 16:
            return f"{name} {get_mask_card_number(number)}"
        elif len(number) == 20:
            return f"{name} {get_mask_account(number)}"

    raise ValueError("Некорректный номер карты или счета")


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "ДД/ММ/ГГГГ".

    :param date_str: Исходная строка с датой.
    :return: Дата в формате "ДД/ММ/ГГГГ".
    """
    year, month, day = date_str.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


# def main() -> None:
# while True:
# print("\nВыберите действие:")
# print("1. Маскировать номер карты/счета")
# print("2. Форматировать дату")
# print("3. Выйти")

# choice = input("Введите номер действия: ")

# if choice == "1":
# data = input(
#    "Введите данные (например, 'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305'): "
# )
# try:
#  masked_data = mask_account_card(data)
# print(f"Результат: {masked_data}")
# except ValueError as e:
#  print(f"Ошибка: {e}")

#  elif choice == "2":
#   date_str = input("Введите дату в формате '2024-03-11T02:26:18.671407': ")
#  formatted_date = get_date(date_str)
#  print(f"Результат: {formatted_date}")

# elif choice == "3":
#  print("Выход из программы.")
#  break

#  else:
# print("Некорректный ввод, попробуйте снова.")


# if __name__ == "__main__":
# main()
