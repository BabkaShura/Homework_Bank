from typing import Any
from typing import Dict
from typing import Hashable
from typing import List

import pandas as pd


def read_transactions_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Считывает транзакции из файла по указанному пути с помощью pandas."""
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def read_transactions_excel(path: str) -> List[Dict[Hashable, Any]]:
    """Считывает транзакции из файла по указанному пути с помощью pandas."""
    df = pd.read_excel(path)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    print("CSV:")
    df_csv = pd.read_csv("transactions.csv")
    print(df_csv.shape)
    print(df_csv.head())

    print("\nExcel:")
    df_excel = pd.read_excel("transactions_excel.xlsx")
    print(df_excel.shape)
    print(df_excel.head())
