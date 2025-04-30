import os
from typing import Any
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict[str, str]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.

    :param transaction: словарь с ключами 'amount' и 'currency'
    :return: сумма в рублях (float)
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency")

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        response: requests.Response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            params={"base": currency, "symbols": "RUB"},
            headers={"apikey": API_KEY},
        )
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        rate: float = data["rates"]["RUB"]
        return round(amount * rate, 2)

    return amount
