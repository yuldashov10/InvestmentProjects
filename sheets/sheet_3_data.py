import sys

from sheets.sheet_utils import open_excel_file
from utils.settings import INPUT_FILE_PATH, SHEET_3_NAME

data = open_excel_file(INPUT_FILE_PATH, sheet_name=SHEET_3_NAME, header=[0, 1])

try:
    VARIANT = int(data.iloc[1, 0])
    PRICE_PER_UNIT_PESS = float(data.iloc[0, 1])
    PRICE_PER_UNIT_OPT = float(data.iloc[0, 2])
    PRODUCTION_COSTS_YES_PESS = float(data.iloc[0, 3])
    PRODUCTION_COSTS_YES_OPT = float(data.iloc[0, 4])
    NEW_MACHINE_LIQUIDATION_VALUE_PESS = float(data.iloc[0, 5])
    NEW_MACHINE_LIQUIDATION_VALUE_OPT = float(data.iloc[0, 6])
    PROBABILITY_PESS = float(data.iloc[0, 7])
    PROBABILITY_MOST = float(data.iloc[0, 8])
    PROBABILITY_OPT = float(data.iloc[0, 9])
except Exception as err:
    sys.stdout.write(f"При чтении данных из листа "
                     f"\"{SHEET_3_NAME}\"\nпроизошла ошибка, "
                     f"пожалуйста убедитесь, что все ячейки заполнены ")
    sys.stdout.write(f"Тип ошибки: {err}")
    sys.exit(-1)

if __name__ == "__main__":
    print(type(VARIANT), VARIANT)
    print(type(PROBABILITY_PESS), PROBABILITY_PESS)
    print(type(PROBABILITY_MOST), PROBABILITY_MOST)
    print(type(PROBABILITY_OPT), PROBABILITY_OPT)
