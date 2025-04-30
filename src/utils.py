import json
from typing import List, Dict


def load_transactions(filepath: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.

    :param filepath: путь к JSON-файлу
    :return: список транзакций или пустой список
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []