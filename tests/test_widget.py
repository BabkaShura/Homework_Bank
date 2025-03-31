import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_value, expected", [
    ("Visa Platinum 1234567812345678", "Visa Platinum ****5678"),
    ("Visa 1234567890123456", "Visa ****3456"),
    ("MasterCard 9876543210987654", "MasterCard ****7654"),
    ("Счет 12345678901234567890", "Счет ****7890"),
    ("invalid", ValueError),
])
def test_mask_account_card(input_value, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            mask_account_card(input_value)
    else:
        assert mask_account_card(input_value) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-30", "30.03.2024"),
    ("01/01/2020", "01.01.2020"),
    ("31.12.2025", "31.12.2025"),
    ("2025/12/31", "31.12.2025"),
    ("invalid", None),
    ("", None),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected