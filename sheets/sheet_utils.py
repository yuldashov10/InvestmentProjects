import math
import sys

import pandas as pd

from utils.settings import DISCOUNT_RATE_ROUND


def open_excel_file(
        file_path: str,
        sheet_name: str,
        header=None) -> pd.DataFrame:
    """
    Загружает данные из Excel файла и возвращает датафрейм.

    :param file_path: Путь до Excel файла
    :param sheet_name: Название листа
    :param header: Заголовки столбцов. По умолчанию None
    :return:
    """

    try:
        if header is None:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)
    except Exception as err:
        sys.stdout.write(f"При открытии файла {file_path}"
                         f"произошла ошибка, пожалуйста убедитесь,"
                         f"что файл и лист \"{sheet_name}\" существует.")
        sys.stdout.write(f"Тип ошибки: {err}")
        sys.exit(-1)

    return df


def remove_first_item(nums: list) -> None:
    """
    Удаляет первый элемент списка, если он имеет тип nan.

    :param nums: Список чисел
    :return:
    """

    if math.isnan(nums[0]):
        nums.pop(0)


def calc_discount_date(
        i: float,
        h: float,
        dec: int = DISCOUNT_RATE_ROUND) -> float:
    """
    Рассчитывает ставка дисконтирования, по формуле
    i + h + (i * h).
    :param i: Требуемый уровень доходности
    :param h: Инфляция
    :param dec: Округление до dec знаков. По умолчанию DISCOUNT_RATE_ROUND
    :return:
    """

    return round(i + h + (i * h), dec)
