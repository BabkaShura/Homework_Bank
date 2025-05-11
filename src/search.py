import re
from typing import List, Dict

def search_transactions_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет операции, в описании которых присутствует заданная строка (поиск с учетом регистра и шаблонов).

    :param transactions: Список словарей с банковскими операциями. Описание операции должно находиться по ключу 'description'.
    :param search_str: Строка или регулярное выражение для поиска в описании операций.
    :return: Список словарей, содержащих заданную строку в описании.
    """
    pattern = re.compile(search_str, re.IGNORECASE)  # Игнорируем регистр
    result = [tx for tx in transactions if pattern.search(tx.get('description', ''))]
    return result


transactions = [
    {"id": 1, "description": "Оплата товаров в магазине", "amount": -500},
    {"id": 2, "description": "Перевод от друга", "amount": 1000},
    {"id": 3, "description": "Покупка билетов", "amount": -200}
]

result = search_transactions_by_description(transactions, "оплата")
print(result)