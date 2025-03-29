def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item.get('state') == state]

from datetime import datetime

def sort_by_date(data, reverse=True):
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
