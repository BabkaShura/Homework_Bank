from pathlib import Path

from src.utils import load_transactions


def test_load_transactions_valid(tmp_path: Path) -> None:
    file = tmp_path / "valid.json"
    file.write_text('[{"amount": "100", "currency": "USD"}]')
    result = load_transactions(str(file))
    assert isinstance(result, list)
    assert result[0]["amount"] == "100"


def test_load_transactions_empty(tmp_path: Path) -> None:
    file = tmp_path / "empty.json"
    file.write_text("")
    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_not_list(tmp_path: Path) -> None:
    file = tmp_path / "invalid.json"
    file.write_text('{"amount": "100"}')
    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_file_not_found() -> None:
    result = load_transactions("nonexistent.json")
    assert result == []
