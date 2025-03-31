import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210987654", "9876 54** **** 7654"),
    ("1234", "1234"),  # Граничный случай
    ("", ""),  # Пустая строка
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "****7890"),  # Корректный номер (20 цифр)
    ("98765432109876543210", "****3210"),  # Еще один корректный случай
    ("1234567890123456", ValueError),  # Недостаточная длина (16 цифр)
    ("98765432", ValueError),  # Недостаточная длина (8 цифр)
    ("123", ValueError),  # Слишком короткий номер
    ("", ValueError),  # Пустая строка
])
def test_get_mask_account(account_number, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_mask_account(account_number)
    else:
        assert get_mask_account(account_number) == expected