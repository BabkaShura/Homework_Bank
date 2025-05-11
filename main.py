from src.file_reader import read_transactions_csv, read_transactions_excel
from src.search import search_transactions_by_description

from src.widget import mask_account_card, get_date

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions

AVAILABLE_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input("Пользователь: ")
    transactions = []

    if file_type == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = load_transactions("data/operations.json")
    elif file_type == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_transactions_csv("src/transactions.csv")
    elif file_type == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_transactions_excel("src/transactions_excel.xlsx")
    else:
        print("Программа: Некорректный выбор. Завершение работы.")
        return

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ").upper()
        if status in AVAILABLE_STATUSES:
            print(f"Программа: Операции отфильтрованы по статусу \"{status}\"")
            transactions = filter_by_state(transactions, status)
            break
        else:
            print(f"Программа: Статус операции \"{status}\" недоступен.")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if sort_answer == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse=reverse)

    currency_answer = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if currency_answer == "да":
        transactions = filter_by_currency(transactions, "руб")

    desc_filter = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").lower()
    if desc_filter == "да":
        keyword = input("Введите слово для фильтрации по описанию: ")
        transactions = list(search_transactions_by_description(transactions, keyword))

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for tx in transactions:
        raw_date = tx.get("date", "")
        date = get_date(raw_date) if raw_date else ""
        desc = tx.get("description", "")
        from_raw = tx.get("from", "")
        to_raw = tx.get("to", "")
        from_acc = mask_account_card(from_raw) if from_raw else ""
        to_acc = mask_account_card(to_raw) if to_raw else ""
        amount = tx.get("amount", 0)
        currency = tx.get("currency", "")
        print(f"{date} {desc}\n{from_acc} -> {to_acc}\nСумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()
