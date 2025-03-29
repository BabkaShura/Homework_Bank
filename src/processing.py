from datetime import datetime
from typing import List


def filter_by_state(data: List[dict], state: str = "EXECUTED") -> List[dict]:
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
