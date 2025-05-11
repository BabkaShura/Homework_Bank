from collections import Counter
from typing import List, Dict


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой из указанных категорий по полю 'description'.

    :param transactions: Список словарей с банковскими операциями.
    :param categories: Список названий категорий для подсчета.
    :return: Словарь с количеством операций по категориям.
    """
    category_counter = Counter()

    for tx in transactions:
        description = tx.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counter[category] += 1

    return dict(category_counter)


transactions = [
    {"id": 1, "description": "Оплата товаров в магазине"},
    {"id": 2, "description": "Перевод от друга"},
    {"id": 3, "description": "Покупка билетов"},
    {"id": 4, "description": "Оплата коммунальных услуг"},
]

categories = ["оплата", "перевод", "покупка"]

result = count_transactions_by_category(transactions, categories)
print(result)