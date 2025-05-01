import json
from typing import Dict
from typing import List

from src.logger_config import setup_logger

logger = setup_logger("utils")


def load_transactions(filepath: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.

    :param filepath: путь к JSON-файлу
    :return: список транзакций или пустой список
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Не удалось загрузить файл: {filepath}", exc_info=True)
        return []


if __name__ == "__main__":
    logger.info("Тестовая запись в лог")
    load_transactions("несущ.json")
