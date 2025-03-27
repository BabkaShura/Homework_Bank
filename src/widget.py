from src.masks import get_mask_card_number, get_mask_account


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
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ".

    :param date_str: Исходная строка с датой.
    :return: Дата в формате "ДД.ММ.ГГГГ".
    """
    return date_str.split("T")[0].replace("-", ".")[::-1][:10][::-1]