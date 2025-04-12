# Homework_Bank

## Описание проекта
Homework_Bank — это учебный проект, включающий обработку транзакций, маскировку номеров карт и счетов, а также сортировку и фильтрацию данных.

## Функциональность
Проект включает следующие функции:

### Маскировка данных
- **`get_mask_card_number(card_number: str) -> str`**  
  Маскирует номер банковской карты, оставляя только последние 4 цифры.  
  **Пример:** `"1234567891234678"` → `"************4678"`

- **`get_mask_account(account_number: str) -> str`**  
  Маскирует номер банковского счёта, оставляя первые 2 и последние 4 цифры.  
  **Пример:** `"12345678901234567890"` → `"12****************7890"`

# Функциональность

### Маскирование номера карты или счёта
- **`mask_account_card(data: str) -> str`**  
  Маскирует номер карты (оставляя только первые 6 и последние 4 цифры) или счёта (оставляя только последние 4 цифры).  
  **Пример:** `mask_account_card("Visa Platinum 7000792289606361")` → `Visa Platinum 7000 79** **** 6361`.

### Преобразование даты
- **`get_date(date_str: str) -> str`**  
  Преобразует строку с датой из формата `"2024-03-11T02:26:18.671407"` в `"11.03.2024"`.


### Обработка транзакций
- **`filter_by_state(data: list, state: str = 'EXECUTED') -> list`**  
  Фильтрует список транзакций по заданному статусу.  
  **Пример:** Вернёт только транзакции со статусом `'EXECUTED'`.

- **`sort_by_date(data: list, reverse: bool = True) -> list`**  
  Сортирует список транзакций по дате в порядке убывания (по умолчанию) или возрастания.  
  **Пример:** Последние операции будут в начале списка.

### Фильтрация по валюте
- **`filter_by_currency(data: list, currency_code: str) -> Iterator[dict]`**  
  Возвращает итератор транзакций, в которых валюта соответствует заданному коду.  
  **Пример:** `filter_by_currency(data, "USD")` вернёт только транзакции в долларах США.

### Функция-декоратор
- **`@log(file_path: str)`**
  Декоратор, записывающий информацию о вызове функции в указанный лог-файл.
  Точкой входа является файл `main.py`. Он позволяет запустить все функции с использованием классических примеров входных данных.

## Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/BabkaShura/Homework_Bank.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd homework_bank
   ```
3. Установите зависимости (если есть):
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите `main.py`:
   ```bash
   python main.py
   ```
## Использование

Примеры использования функций:

~~~
from datetime import datetime
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date
from typing import List

Маскировка номера карты
card_number = "1234567890123456"
masked_number = get_mask_card_number(card_number)
print(f"Информация о карте: {masked_number}") # Output: 1234 56** **** 3456

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Информация о счете: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
input_information = "Visa Classic 1234567890123456"
masked_information = mask_account_card(input_information)
print(f"Информация о карте/счете: {masked_information}") # Output: Visa Classic 1234 56** **** 3456

Преобразование даты
input_date = "2023-03-06T00:00:00"
formated_date = get_date(input_date)
print(f"Дата операции: {formated_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
operations = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
list_of_operation = filter_by_state(operations, state="EXECUTED")
print(f"Успешные операции: \n{list_of_operation}")

# Output:
[{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},]

Сортировка по дате
sort_by_date_list = sort_by_date(operations)
print(f"Список операций: \n{sort_by_date_list}")

# Output:
[{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},]


Фильтрация по валюте

Пример входных данных:
transaction_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]

result = filter_by_currency(transaction_list, currency="USD")
print(f"Список транзакций в валюте {currecy}:")
for transaction in result:
    print(transaction)
    
# Output:
{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    
    
Описание типов транзакций

Пример входных данных: аналогично функции "Фильтрация по валюте"
item = transaction_descriptions(transaction_list)
print("Типы транзакций:")
for transaction in item:
    print(transaction)   
# Output:
Перевод организации
Перевод со счета на счет
    
Генератор номеров карт

Пример входных данных:
  start = 1
  stop = 3
  generator = card_number_generator(start, stop)
    for card in generator:
        print(card)  
        
# Output:
0000 0000 0000 0001
0000 0000 0000 0002        
~~~

## Тестирование

Для тестирования работы каждой функции в условиях получения различных входных данных (в том числе, ошибочных и неполных) существует группа тестов в пакете `tests`.
В модуле `conftest.py` содержатся вспомогательные функции (фикстуры), используемые при проведении тестов.


## Зависимости

Проект использует следующие зависимости:

*   Python 3.13
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
