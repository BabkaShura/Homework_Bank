import re
from typing import Union

from src.decorators import log

from src.logger_config import setup_logger

logger = setup_logger("masks")


@log("mylog.txt")
def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX."""
    logger.info("Функция get_mask_card_number вызвана")
    if len(card_number) not in {16, 0, 4}:
        logger.error("Некорректный номер карты. Должно быть 16 цифр.")
        raise ValueError("Некорректный номер карты. Должно быть 16 цифр.")
    if len(card_number) in {0, 4}:
        return card_number

    if not re.fullmatch(r"\d{16}", card_number):
        logger.error("Некорректный номер карты. Должно быть 16 цифр.")
        raise ValueError("Некорректный номер карты. Должно быть 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


@log("mylog.txt")
def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета в формате **XXXX."""
    logger.info("Функция get_mask_account вызвана")
    if not account_number:
        logger.error("Номер счета не может быть пустым.")
        raise ValueError("Номер счета не может быть пустым.")
    if not re.fullmatch(r"\d{20}", account_number):
        logger.error("Некорректный номер счета. Должно быть 20 цифр.")
        raise ValueError("Некорректный номер счета. Должно быть 20 цифр.")

    return f"****{account_number[-4:]}"


if __name__ == "__main__":
    get_mask_card_number("1234567812345678")
    get_mask_account("40817810099910004312")
