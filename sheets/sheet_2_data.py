import sys

from sheet_utils import calc_discount_date, open_excel_file
from utils.settings import INPUT_FILE_PATH, SHEET_2_NAME

data = open_excel_file(INPUT_FILE_PATH, SHEET_2_NAME)

try:
    VARIANT = int(data.iloc[0, 0])
    NEW_MACHINE_PERIOD = int(data.iloc[0, 1])
    PRICE_PER_UNIT = int(data.iloc[0, 2])
    NEW_MACHINE_PRICE = float(str(data.iloc[0, 3]).replace(",", ""))
    NEW_MACHINE_DEPRECIATION_PERIOD = int(data.iloc[0, 4])
    CAPITAL_REQUIREMENT_YES = float(str(data.iloc[0, 5]).replace(",", ""))
    CAPITAL_REQUIREMENT_NO = float(str(data.iloc[0, 6]).replace(",", ""))
    NEW_MACHINE_LIQUIDATION_VALUE = float(str(data.iloc[0, 7]).replace(",", ""))
    OLD_MACHINE_LIQUIDATION_VALUE = float(str(data.iloc[0, 8]).replace(",", ""))
    REQUIRED_PROFITABILITY = float(data.iloc[0, 9])
    TAX_RATE = float(data.iloc[0, 10])
    INFLATION = float(data.iloc[0, 11])
    DISCOUNT_RATE = calc_discount_date(REQUIRED_PROFITABILITY, INFLATION)
except Exception as err:
    sys.stdout.write(f"При чтении данных из листа "
                     f"\"{SHEET_2_NAME}\"\nпроизошла ошибка, "
                     f"пожалуйста убедитесь, что все ячейки заполнены ")
    sys.stdout.write(f"Тип ошибки: {err}")
    sys.exit(-1)

if __name__ == "__main__":
    print(VARIANT)
    print(DISCOUNT_RATE)
