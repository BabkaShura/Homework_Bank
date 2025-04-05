import re
from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX."""
    if len(card_number) not in {16, 0, 4}:
        raise ValueError("Некорректный номер карты. Должно быть 16 цифр.")
    if len(card_number) in {0, 4}:
        return card_number

    if not re.fullmatch(r"\d{16}", card_number):
        raise ValueError("Некорректный номер карты. Должно быть 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета в формате **XXXX."""
    if not account_number:
        raise ValueError("Номер счета не может быть пустым.")
    if not re.fullmatch(r"\d{20}", account_number):
        raise ValueError("Некорректный номер счета. Должно быть 20 цифр.")

    return f"****{account_number[-4:]}"
