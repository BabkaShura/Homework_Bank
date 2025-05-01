import os
from typing import Any
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли по данным ключам:
    'operationAmount.amount' и 'operationAmount.currency.code'.

    :param transaction: словарь с данными о транзакции
    :return: сумма в рублях (float)
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, TypeError, ValueError):
        return 0.0

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={"from": currency, "to": "RUB", "amount": amount},
            headers={"apikey": API_KEY},
        )
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        return float(data.get("result", 0.0))

    return amount
