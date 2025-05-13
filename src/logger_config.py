import logging
import os


def setup_logger(module_name: str) -> logging.Logger:
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # Удаление предыдущих обработчиков, чтобы избежать дублирования
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(f"logs/{module_name}.log", mode="w", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
