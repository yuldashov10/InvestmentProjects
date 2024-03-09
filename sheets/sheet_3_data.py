import sys

import pandas as pd

from sheets.sheet_utils import open_excel_file
from utils.settings import INPUT_FILE_PATH, SHEET_3_NAME

data: pd.DataFrame = open_excel_file(INPUT_FILE_PATH,
                                     sheet_name=SHEET_3_NAME,
                                     header=[0, 1])

try:
    VARIANT = int(data.iloc[1, 0])

    PESSIMISTIC_PRICE_PERCENT = float(data.iloc[0, 1])
    OPTIMISTIC_PRICE_PERCENT = float(data.iloc[0, 2])

    PESSIMISTIC_PROD_COSTS_PERCENT = float(data.iloc[0, 3])
    OPTIMISTIC_PROD_COSTS_PERCENT = float(data.iloc[0, 4])

    PESSIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT = float(data.iloc[0, 5])
    OPTIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT = float(data.iloc[0, 6])

    PESSIMISTIC_PROBABILITY = float(data.iloc[0, 7])
    MOST_PROBABILITY = float(data.iloc[0, 8])
    OPTIMISTIC_PROBABILITY = float(data.iloc[0, 9])
except Exception as err:
    sys.stdout.write(f"При чтении данных из листа "
                     f"\"{SHEET_3_NAME}\"\nпроизошла ошибка, "
                     f"пожалуйста убедитесь, что все ячейки заполнены ")
    sys.stdout.write(f"Тип ошибки: {err}")
    sys.exit(-1)

if __name__ == "__main__":
    print(type(VARIANT), VARIANT)
