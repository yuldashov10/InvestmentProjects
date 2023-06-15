from pathlib import Path
import platform

BASE_DIR = Path(__file__).resolve().parent.parent
FILENAME = "source.xlsx"  # название исходного Excel файла

SHEET_1_NAME = "main"  # название 1-го листа
SHEET_2_NAME = "source_1"  # название 2-го листа
SHEET_3_NAME = "source_2"  # название 3-го листа

# ставка дисконтирования округляется до указанных знаков
DISCOUNT_RATE_ROUND = 2

# Значение округления денежных единиц
CURRENCY_ROUNDING_VALUE = 2

if platform.system() == "Windows":
    INPUT_FILE_PATH = rf"{BASE_DIR}\src\{FILENAME}"
else:  # Linux, MacOS
    INPUT_FILE_PATH = rf"{BASE_DIR}/src/{FILENAME}"

if __name__ == "__main__":
    print(BASE_DIR)
    print(INPUT_FILE_PATH)
