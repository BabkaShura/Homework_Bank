from datetime import datetime
from typing import List


def filter_by_state(data: List[dict], state: str = "EXECUTED") -> List[dict]:
    if not isinstance(data, list):
        raise TypeError("Ожидается список словарей")
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[dict], order: str = "desc") -> List[dict]:
    if not isinstance(data, list):
        raise TypeError("Ожидается список словарей")

    valid_items = []
    for item in data:
        if "date" in item and isinstance(item["date"], str):
            try:
                item["parsed_date"] = datetime.fromisoformat(item["date"])
                valid_items.append(item)
            except ValueError:
                continue  # Пропускаем некорректные даты

    return sorted(valid_items, key=lambda x: x["parsed_date"], reverse=(order == "desc"))
