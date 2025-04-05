import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.fixture
def card_data() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_data() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def date_str() -> str:
    return "2024-03-11T02:26:18.671407"


def test_mask_card_number(card_data: str) -> None:
    """Тест маскирования номера карты."""
    result = mask_account_card(card_data)
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account(account_data: str) -> None:
    """Тест маскирования номера счета."""
    result = mask_account_card(account_data)
    assert result == "Счет ****4305"


def test_get_date(date_str: str) -> None:
    """Тест преобразования даты из ISO формата в DD.MM.YYYY."""
    result = get_date(date_str)
    assert result == "11.03.2024"


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ],
)
def test_get_date_various_formats(date_str: str, expected: str) -> None:
    """Тест преобразования даты с разными входными значениями."""
    assert get_date(date_str) == expected
