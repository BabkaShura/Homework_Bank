import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "active", "date": "2024-01-01"},
        {"id": 2, "state": "inactive", "date": "2023-12-01"},
        {"id": 3, "state": "active", "date": "2024-02-15"},
    ]

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, "active")
    assert len(result) == 2
    assert all(item["state"] == "active" for item in result)

@pytest.mark.parametrize("order, expected_first_id", [
    ("asc", 2),
    ("desc", 3),
])
def test_sort_by_date(sample_data, order, expected_first_id):
    result = sort_by_date(sample_data, order)
    assert result[0]["id"] == expected_first_id
