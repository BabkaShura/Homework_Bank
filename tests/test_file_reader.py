from unittest.mock import MagicMock
from unittest.mock import patch

import pandas as pd

from src.file_reader import read_transactions_csv
from src.file_reader import read_transactions_excel


@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv: MagicMock) -> None:
    mock_df = pd.DataFrame(
        [
            {"date": "2025-01-01", "amount": 1000, "category": "Salary"},
            {"date": "2025-01-02", "amount": -150, "category": "Groceries"},
        ]
    )
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv()

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["category"] == "Salary"
    mock_read_csv.assert_called_once_with("transactions.csv")


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel: MagicMock) -> None:
    mock_df = pd.DataFrame(
        [
            {"date": "2025-01-03", "amount": -200, "category": "Transport"},
            {"date": "2025-01-04", "amount": -300, "category": "Rent"},
        ]
    )
    mock_read_excel.return_value = mock_df

    result = read_transactions_excel()

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[1]["category"] == "Rent"
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
