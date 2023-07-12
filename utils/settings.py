from pathlib import Path
import platform

VARIANT = 7

BASE_DIR = Path(__file__).resolve().parent.parent
FILENAME = "source.xlsx"  # название исходного Excel файла

SHEET_1_NAME = "main"  # название 1-го листа
SHEET_2_NAME = "source_1"  # название 2-го листа
SHEET_3_NAME = "source_2"  # название 3-го листа

# ставка дисконтирования округляется до указанных знаков
DISCOUNT_RATE_ROUND = 2

# Значение округления денежных единиц
CURRENCY_ROUNDING_VALUE = 2

# Амортизационный период в случае отказа от реализации проекта
DEPRECIATION_PERIOD_WHEN_PROJECT_NOT_IMPLEMENTED = 0

# Расстояние между данными
DATA_SPACING = 5

FIRST_STEP_TITLES_KEYS: tuple[str, ...] = (
    "years", "sales_volume",
    "production_costs", "depreciation_allowance",
    "taxable_profit", "profit_tax",
    "net_profit", "cash_flow_from_op",
    "working_capital", "working_capital_gain",
    "capital_investments", "cash_flow"
)

FIRST_STEP_TITLES: dict[int, str] = {
    1: 'Годы',
    2: 'ОР (Объем реализации)(₽)',
    3: 'ИП (Издержки производства)(₽)',
    4: 'А (Амортизационные отчисления)(₽)',
    5: 'НОП (Налогооблагаемая прибыль)(₽)',
    6: 'Н (Налог на прибыль)(₽)',
    7: 'ЧП (Чистая прибыль)(₽)',
    8: 'CFFO (Cash Flow From Operations)(₽)',
    9: 'ОК (Оборотный капитал)(₽)',
    10: 'ПОК (Прирост оборотного капитала)(₽)',
    11: 'КВ (Капитальные вложения)(₽)',
    12: 'CF (Cash Flow)(₽)',
}

FIRST_STEP_SUBTITLES: dict[int, str] = {
    1: "При реализации проекта",
    2: "При отказе от реализации"
}

if platform.system() == "Windows":
    INPUT_FILE_PATH = rf"{BASE_DIR}\src\{FILENAME}"
    RESULT_FILE_PATH = rf"{BASE_DIR}\result\variant_{VARIANT}_data.xlsx"
else:  # Linux, MacOS
    INPUT_FILE_PATH = rf"{BASE_DIR}/src/{FILENAME}"
    RESULT_FILE_PATH = rf"{BASE_DIR}/result/variant_{VARIANT}_data.xlsx"

if __name__ == "__main__":
    print(BASE_DIR)
    print(INPUT_FILE_PATH)
