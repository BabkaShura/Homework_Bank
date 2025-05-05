from typing import Any
from typing import Dict
from typing import Hashable
from typing import List

import pandas as pd


def read_transactions_csv() -> List[Dict[Hashable, Any]]:
    """Считывает транзакции из файла transactions.csv с помощью pandas."""
    df = pd.read_csv("transactions.csv")
    return df.to_dict(orient="records")


def read_transactions_excel() -> List[Dict[Hashable, Any]]:
    """Считывает транзакции из файла transactions_excel.xlsx с помощью pandas."""
    df = pd.read_excel("transactions_excel.xlsx")
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
