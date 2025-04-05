from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import filter_by_state
from src.processing import sort_by_date

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
