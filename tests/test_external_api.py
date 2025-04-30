from unittest.mock import MagicMock
from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    transaction = {"amount": "100", "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    result = convert_to_rub(transaction)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_rub(mock_get: MagicMock) -> None:
    transaction = {"amount": "100", "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 100.0
    mock_get.assert_not_called()
