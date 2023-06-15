import sys

from utils.settings import INPUT_FILE_PATH, SHEET_1_NAME
from sheet_utils import remove_first_item, open_excel_file

data = open_excel_file(INPUT_FILE_PATH, SHEET_1_NAME)

try:
    YEARS = data.iloc[2:, 0].astype(int).tolist()

    SALES_VOL_YES = data.iloc[2:, 1].replace(
        ",", "", regex=True).astype(int).tolist()
    SALES_VOL_NO = data.iloc[2:, 2].replace(
        ",", "", regex=True).astype(int).tolist()

    PRODUCTION_COSTS_YES = data.iloc[2:, 3].replace(
        ",", "", regex=True).astype(int).tolist()
    PRODUCTION_COSTS_NO = data.iloc[2:, 4].replace(
        ",", "", regex=True).astype(int).tolist()
except Exception as err:
    sys.stdout.write(f"При чтении данных из листа "
                     f"\"{SHEET_1_NAME}\"\nпроизошла ошибка, "
                     f"пожалуйста убедитесь, что все ячейки заполнены ")
    sys.stdout.write(f"Тип ошибки: {err}")
    sys.exit(-1)

# очищаются все списки от значения nan
remove_first_item(SALES_VOL_YES)
remove_first_item(SALES_VOL_NO)
remove_first_item(PRODUCTION_COSTS_YES)
remove_first_item(PRODUCTION_COSTS_NO)

if __name__ == "__main__":
    print(SALES_VOL_YES)
    print(SALES_VOL_NO)
    print(PRODUCTION_COSTS_YES)
    print(PRODUCTION_COSTS_NO)
    