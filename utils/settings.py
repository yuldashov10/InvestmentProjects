import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FILENAME = "source.xlsx"  # название исходного Excel файла
INPUT_FILE_PATH = os.path.join(BASE_DIR, "src", FILENAME)

# Названия листов в исходном файле
SHEET_1_NAME = "main"
SHEET_2_NAME = "source_1"
SHEET_3_NAME = "source_2"

# Названия листов в результирующем файле
RESULT_SHEET_1_NAME = "Основной"
RESULT_SHEET_2_NAME = "С учетом инфляции"
RESULT_SHEET_3_NAME = "Оптимистический"
RESULT_SHEET_4_NAME = "Пессимистический"
RESULT_SHEET_5_NAME = "Итоговые потоки"
RESULT_SHEET_6_NAME = "Пороговое значение цены"

# Номер столбца с данными для диаграммы
DATA_COLUMN_NUM = 12  # столбец L

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

LABELS_FOR_CHARTS: list[tuple[str, str, str]] = [
    ("CASH FLOW при реализации", "Период времени", "Млн.руб."),
    ("CASH FLOW при отказе", "Период времени", "Млн.руб."),
]

FIRST_STEP_SUBTITLES: dict[int, str] = {
    1: "При реализации проекта",
    2: "При отказе от реализации"
}

if __name__ == "__main__":
    print(BASE_DIR)
    print(INPUT_FILE_PATH)
