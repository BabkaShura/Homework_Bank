from unittest.mock import MagicMock
from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7450.0}

    result = convert_to_rub(transaction)
    assert result == 7450.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_rub(mock_get: MagicMock) -> None:
    transaction = {"operationAmount": {"amount": "1500", "currency": {"code": "RUB"}}}

    result = convert_to_rub(transaction)
    assert result == 1500.0
    mock_get.assert_not_called()


def test_convert_to_rub_invalid_transaction() -> None:
    transaction = {"operationAmount": {"amount": "not_a_number", "currency": {"code": "USD"}}}

    result = convert_to_rub(transaction)
    assert result == 0.0
