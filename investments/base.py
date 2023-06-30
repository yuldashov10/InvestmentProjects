import os
import time
from pprint import pprint
from typing import Any

import pandas as pd

from calculations.index import Index
from sheets.sheet_1_data import (
    PRODUCTION_COSTS_NO,
    PRODUCTION_COSTS_YES,
    SALES_VOL_NO,
    SALES_VOL_YES,
    YEARS
)
from sheets.sheet_2_data import (
    CAPITAL_REQUIREMENT_NO,
    CAPITAL_REQUIREMENT_YES,
    DISCOUNT_RATE,
    INFLATION,
    NEW_MACHINE_DEPRECIATION_PERIOD,
    NEW_MACHINE_PERIOD,
    NEW_MACHINE_PRICE,
    NEW_MACHINE_LIQUIDATION_VALUE,
    OLD_MACHINE_LIQUIDATION_VALUE,
    PRICE_PER_UNIT,
    TAX_RATE,
    VARIANT
)
from utils.settings import (
    DATA_SPACING,
    DEPRECIATION_PERIOD_WHEN_PROJECT_NOT_IMPLEMENTED,
    FIRST_STEP_SUBTITLES,
    FIRST_STEP_TITLES,
)


class InvestmentBasic:
    """
    Реализует первый этап расчета эффективности инвестиционных проектов.

    :param year: Лет. На какой период рассчитан проект
    :param annual_sales: Годовой объем продаж(шт.)
    :param production_costs_per_unit: Производственные издержки на единицу
    :param unit_price: Цена за единицу продукции
    :param new_machine_price: Цена нового оборудования
    :param new_machine_depreciation_period: Срок амортизации
    нового оборудования
    :param new_machine_lifespan: Срок службы нового оборудования
    :param capital_requirement: Потребность в оборотном капитале
    :param old_machine_liquidation_value: Ликвидационная стоимость старого
    оборудования
    :param new_machine_liquidation_value: Ликвидационная стоимость нового
    оборудования
    :param tax_rate: Ставка налога на прибыль
    :param inflation: Годовой темп инфляции. По умолчанию None
    :param is_implemented: При реализации или при отказе от реализации.
    По умолчанию False
    """

    def __init__(self,
                 year,
                 annual_sales,
                 production_costs_per_unit,
                 unit_price,
                 new_machine_price,
                 new_machine_depreciation_period,
                 new_machine_lifespan,
                 capital_requirement,
                 new_machine_liquidation_value,
                 old_machine_liquidation_value,
                 tax_rate,
                 inflation=None,
                 is_implemented=False):
        self.__year = year
        self.__annual_sales = annual_sales
        self.__production_costs_per_unit = production_costs_per_unit
        self.__unit_price = unit_price
        self.__new_machine_price = new_machine_price
        self.__new_machine_depreciation_period = new_machine_depreciation_period
        self.__new_machine_lifespan = new_machine_lifespan
        self.__capital_requirement = capital_requirement
        self.__new_machine_liquidation = new_machine_liquidation_value
        self.__old_machine_liquidation = old_machine_liquidation_value
        self.__tax_rate = tax_rate
        self.__inflation = inflation
        self.__is_capital_invest_implemented = is_implemented

    def years(self):
        return self.__year

    def sales_volume(self):
        return Index.sales_volume(
            self.__annual_sales,
            self.__unit_price,
            inflation=self.__inflation
        )

    def production_costs(self):
        return Index.production_costs(
            self.__annual_sales,
            self.__production_costs_per_unit,
            inflation=self.__inflation
        )

    def depreciation_allowance(self):
        return Index.depreciation_allowance(
            self.__new_machine_price,
            self.__new_machine_depreciation_period,
            self.__new_machine_lifespan
        )

    def taxable_profit(self):
        return Index.taxable_profit(
            self.sales_volume(),
            self.production_costs(),
            self.depreciation_allowance()
        )

    def profit_tax(self):
        return Index.profit_tax(
            self.taxable_profit(),
            self.__tax_rate
        )

    def net_profit(self):
        return Index.net_profit(
            self.taxable_profit(),
            self.profit_tax()
        )

    def cash_flow_from_op(self):
        return Index.cash_flow_from_op(
            self.depreciation_allowance(),
            self.net_profit()
        )

    def working_capital(self):
        return Index.working_capital(
            self.sales_volume(),
            self.__capital_requirement
        )

    def working_capital_gain(self):
        return Index.working_capital_gain(
            self.working_capital()
        )

    def capital_investments(self):
        return Index.capital_investments(
            self.__new_machine_lifespan,
            self.__new_machine_price,
            self.__old_machine_liquidation,
            self.__new_machine_liquidation,
            self.__tax_rate,
            is_implemented=self.__is_capital_invest_implemented
        )

    def cash_flow(self):
        return Index.cash_flow(
            self.depreciation_allowance(),
            self.net_profit(),
            self.working_capital_gain(),
            self.capital_investments(),
            inflation=self.__inflation
        )

    def get_data(self) -> dict[int, list]:

        data: dict[int, list] = {
            1: self.years(),
            2: self.sales_volume(),
            3: self.production_costs(),
            4: self.depreciation_allowance(),
            5: self.taxable_profit(),
            6: self.profit_tax(),
            7: self.net_profit(),
            8: self.cash_flow_from_op(),
            9: self.working_capital(),
            10: self.working_capital_gain(),
            11: self.capital_investments(),
            12: self.cash_flow(),
        }

        self.__fill_na_first_pos(data)

        return data

    @staticmethod
    def __fill_na_first_pos(data: dict[Any, list]) -> None:
        """
        Заполняет списки меньшей длины значениями None.
        То есть добавляет значение None к первой позиции.

        :param data: Исходные данные
        :return: None
        """

        max_length: int = max(len(lst) for lst in data.values())

        for key, lst in data.items():
            len_item: int = len(lst)
            if len_item < max_length:
                nan: list[None] = [None] * (max_length - len_item)
                data[key] = nan + data[key]

    @staticmethod
    def check_file_exists(file_path: str) -> bool:
        """
        Проверяет существование файла по указанному пути.

        :param file_path: Путь к файлу
        :return: True, если файл существует, False в противном случае
        """
        return os.path.isfile(file_path)

    @staticmethod
    def __truncate_list(writer: pd.ExcelWriter, sheet_name: str) -> None:
        """
        Удаляет существующий лист из Эксель файла и
        создаст новый со старым индексом.

        :param writer: Excel файл
        :param sheet_name: Название листа, которого нужно пересоздать
        :return: None
        """

        idx = writer.book.sheetnames.index(sheet_name)
        writer.book.remove(writer.book.worksheets[idx])
        writer.book.create_sheet(sheet_name, idx)

    @staticmethod
    def __copy_already_exists_list(writer: pd.ExcelWriter) -> None:
        """
        Создает копию существующих листов файл, чтобы после создания
        новых листов обратно записать старые не удалились.

        :param writer: Excel файл
        :return: None
        """
        writer.sheets.update({ws.title: ws for ws in writer.book.worksheets})

    def append_data_to_excel(self,
                             file_path: str,
                             data: pd.DataFrame,
                             sheet_name: str,
                             start_col: int = 0,
                             start_row: int = None,
                             is_truncate_sheet: bool = False,
                             **kwargs) -> None:
        """
        Добавляет датафрейм в существующий файл Excel [filename] в лист
        [sheet_name].Если [filename] не существует, то функция создаст его.

        :param file_path: Путь к файлу или существующий ExcelWriter
        :param data: DataFrame для сохранения в Excel
        :param sheet_name: Имя листа, в котором будет содержаться DataFrame
        :param start_col: Начальный столбец для новых записей.
        По умолчанию: 0
        :param start_row: Начальная строка для новых записей.
        По умолчанию: None
        :param is_truncate_sheet: Очистить лист и создать заново перед
        записью новых данных
        :param kwargs: Именованные аргументы, которые будут переданы
        `data.to_excel()` могут быть в виде словаря
        :return: None
        """

        if not self.check_file_exists(file_path):
            data.to_excel(
                file_path, sheet_name=sheet_name, **kwargs
            )
            return None

        writer: pd.ExcelWriter = pd.ExcelWriter(
            file_path, mode="a", engine="openpyxl", if_sheet_exists="overlay"
        )

        wb_sheet_names = writer.book.sheetnames
        if is_truncate_sheet and sheet_name in wb_sheet_names:
            self.__truncate_list(writer, sheet_name)

        self.__copy_already_exists_list(writer)

        if (start_row is None and
                sheet_name in wb_sheet_names and
                not is_truncate_sheet):
            start_row = writer.book[sheet_name].max_row + DATA_SPACING
        else:
            start_row = 0

        data.to_excel(
            writer, sheet_name, startrow=start_row, **kwargs
        )
        writer.close()


if __name__ == "__main__":
    implemented = InvestmentBasic(
        YEARS,
        SALES_VOL_YES,
        PRODUCTION_COSTS_YES,
        PRICE_PER_UNIT,
        NEW_MACHINE_PRICE,
        NEW_MACHINE_DEPRECIATION_PERIOD,
        NEW_MACHINE_PERIOD,
        CAPITAL_REQUIREMENT_YES,
        NEW_MACHINE_LIQUIDATION_VALUE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
        is_implemented=True,
    )
    # print("implemented")
    # res_1 = implemented.get_data()
    # pprint(res_1)

    not_implemented = InvestmentBasic(
        YEARS,
        SALES_VOL_NO,
        PRODUCTION_COSTS_NO,
        PRICE_PER_UNIT,
        NEW_MACHINE_PRICE,
        DEPRECIATION_PERIOD_WHEN_PROJECT_NOT_IMPLEMENTED,
        NEW_MACHINE_PERIOD,
        CAPITAL_REQUIREMENT_NO,
        NEW_MACHINE_LIQUIDATION_VALUE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
        is_implemented=False,
    )
    # print("\nnot_implemented")
    # res_2 = not_implemented.get_data()
    # pprint(res_2)

    # write to file ---------------------------------------------

    df = pd.DataFrame(implemented.get_data())
    df2 = pd.DataFrame(not_implemented.get_data())

    df.rename(columns=FIRST_STEP_TITLES, inplace=True)
    df2.rename(columns=FIRST_STEP_TITLES, inplace=True)

    filename = f"variant_{VARIANT}_data.xlsx"

    implemented.append_data_to_excel(
        filename,
        df,
        sheet_name="main1",
        index=False,
        is_truncate_sheet=True
    )

    implemented.append_data_to_excel(
        filename,
        df,
        sheet_name="main1",
        index=False,
    )

    not_implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main2",
        index=False,
        is_truncate_sheet=True
    )
    not_implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main2",
        index=False,
    )
    not_implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main2",
        index=False
    )
    not_implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main3",
        index=False,
    )
    implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main4",
        index=False,
    )
    implemented.append_data_to_excel(
        filename,
        df2,
        sheet_name="main4",
        index=False,
        is_truncate_sheet=True
    )
