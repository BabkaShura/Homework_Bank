from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import transaction_list
from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.widget import get_date
from src.widget import mask_account_card

# Проверка функции маскировки номера карты
print(get_mask_card_number("1234567891234678"))

# Проверка функции маскировки номера счета
print(get_mask_account("12345678901234567890"))

# Тестовые данные
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Проверка функции фильтрации по статусу
filtered_transactions = filter_by_state(transactions)
print("Отфильтрованные транзакции (EXECUTED):", filtered_transactions)

# Проверка функции сортировки по дате
sorted_transactions = sort_by_date(transactions)
print("Отсортированные транзакции (по убыванию):", sorted_transactions)

# Проверка функции маскировки карты или счета по строке
try:
    print(mask_account_card("Visa Platinum 7000792289606361"))  # номер карты
    print(mask_account_card("Счет 12345678901234567890"))  # номер счета
except ValueError as e:
    print("Ошибка:", e)

# Проверка функции преобразования даты
print(get_date("2024-03-11T02:26:18.671407"))

# Вызов filter_by_currency
print("=== Транзакции в валюте USD ===")
currency_result = filter_by_currency(transaction_list, currency="USD")
for tx in currency_result:
    print(tx)

# Вызов transaction_descriptions
print("\n=== Описания всех транзакций ===")
descriptions = transaction_descriptions(transaction_list)
for desc in descriptions:
    print(desc)

# Вызов card_number_generator
print("\n=== Генерация номеров карт от 1 до 5 ===")
try:
    for card in card_number_generator(1, 6):
        print(card)
except (TypeError, ValueError) as e:
    print(f"Ошибка при генерации номеров карт: {e}")
