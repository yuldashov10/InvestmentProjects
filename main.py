import os

import pandas as pd

from investments.base import InvestmentBasic
from investments.excel_utils import BuildChart
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
from sheets.sheet_3_data import (
    OPTIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT,
    OPTIMISTIC_PRICE_PERCENT,
    PESSIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT,
    PESSIMISTIC_PRICE_PERCENT,
)
from utils.settings import (
    BASE_DIR,
    DATA_COLUMN_NUM,
    DEPRECIATION_PERIOD_WHEN_PROJECT_NOT_IMPLEMENTED,
    FIRST_STEP_TITLES,
    LABELS_FOR_CHARTS,
    RESULT_SHEET_1_NAME,
    RESULT_SHEET_2_NAME,
    RESULT_SHEET_3_NAME,
    RESULT_SHEET_4_NAME,
)

RESULT_FILENAME = f"variant_{VARIANT}_data.xlsx"
RESULT_FILE_PATH = os.path.join(BASE_DIR, "result", RESULT_FILENAME)


class Basic:
    def __init__(self):
        self.__filename: str = RESULT_FILE_PATH

    def get_data_implemented_without_inflation(self) -> InvestmentBasic:
        """
        Возвращает данные без учета инфляции при реализации
        инвестиционного проекта.
        :return: InvestmentBasic
        """
        args = {
            "inflation": None,
            "implemented": True
        }
        return self.__init_implemented(*args.values())

    def get_data_not_implemented_without_inflation(self) -> InvestmentBasic:
        """
        Возвращает данные без учета инфляции при отказе от реализации
        инвестиционного проекта.
        :return: InvestmentBasic
        """
        args = {
            "inflation": None,
            "implemented": None
        }
        return self.__init_not_implemented(*args.values())

    def get_data_implemented_with_inflation(self) -> InvestmentBasic:
        """
        Возвращает данные с учетом инфляции при реализации
        инвестиционного проекта.
        :return: InvestmentBasic
        """
        args = {
            "inflation": INFLATION,
            "implemented": True
        }
        return self.__init_implemented(*args.values())

    def get_data_not_implemented_with_inflation(self) -> InvestmentBasic:
        """
        Возвращает данные с учетом инфляции при отказе от реализации
        инвестиционного проекта.
        :return: InvestmentBasic
        """
        args = {
            "inflation": INFLATION,
            "implemented": None
        }
        return self.__init_not_implemented(*args.values())

    def get_data_optimistic_scenario(
            self,
            is_implemented: bool = False
    ) -> InvestmentBasic:
        if is_implemented:
            return self.__init_implemented_optimistic(is_implemented)
        return self.__init_not_implemented_optimistic()

    def get_data_pessimistic_scenario(
            self,
            is_implemented: bool = False
    ) -> InvestmentBasic:
        if is_implemented:
            return self.__init_implemented_pessimistic(is_implemented)
        return self.__init_not_implemented_pessimistic()

    def get_filename(self):
        return self.__filename

    def __create_chart_bar_for_cash_flow(
            self,
            sheet_name: str,
            col_num: int,
            chart_lables: list[tuple[str, str, str]]):
        chart_obj = BuildChart(self.get_filename(),
                               sheet_name,
                               col_num)
        chart_obj.bar_chart(chart_lables)

    def __write_to_excel(self,
                         data: InvestmentBasic,
                         sheet_name: str,
                         index: bool = False,
                         truncate_sheet: bool = False) -> None:
        df = pd.DataFrame(data.get_data())  # pandas Dataframe
        self.__rename_df_cols(df)

        data.append_data_to_excel(
            self.__filename,
            df,
            sheet_name=sheet_name,
            index=index,
            is_truncate_sheet=truncate_sheet
        )

    @staticmethod
    def __init_implemented(
            inflation: None | float = None,
            is_implemented: None | bool = None) -> InvestmentBasic:
        return InvestmentBasic(
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
            inflation=inflation,
            is_implemented=is_implemented
        )

    @staticmethod
    def __init_not_implemented(
            inflation: None | float = None,
            is_implemented: None | bool = None) -> InvestmentBasic:
        return InvestmentBasic(
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
            inflation=inflation,
            is_implemented=is_implemented
        )

    @staticmethod
    def __calc_price_changes(
            original_price: float,
            percentage: float) -> float:
        return original_price + (original_price * percentage)

    def __init_implemented_optimistic(
            self,
            is_implemented: None | bool = None
    ) -> InvestmentBasic:
        OPTIMISTIC_PRICE_PER_UNIT = self.__calc_price_changes(
            PRICE_PER_UNIT,
            OPTIMISTIC_PRICE_PERCENT
        )
        OPTIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE = self.__calc_price_changes(
            NEW_MACHINE_LIQUIDATION_VALUE,
            OPTIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT
        )
        return InvestmentBasic(
            YEARS,
            SALES_VOL_YES,
            PRODUCTION_COSTS_YES,
            OPTIMISTIC_PRICE_PER_UNIT,
            NEW_MACHINE_PRICE,
            NEW_MACHINE_DEPRECIATION_PERIOD,
            NEW_MACHINE_PERIOD,
            CAPITAL_REQUIREMENT_YES,
            OPTIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            is_implemented=is_implemented
        )

    def __init_not_implemented_optimistic(
            self,
            is_implemented: None | bool = None
    ) -> InvestmentBasic:
        OPTIMISTIC_PRICE_PER_UNIT = self.__calc_price_changes(
            PRICE_PER_UNIT,
            OPTIMISTIC_PRICE_PERCENT
        )
        OPTIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE = self.__calc_price_changes(
            NEW_MACHINE_LIQUIDATION_VALUE,
            OPTIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT
        )
        return InvestmentBasic(
            YEARS,
            SALES_VOL_NO,
            PRODUCTION_COSTS_NO,
            OPTIMISTIC_PRICE_PER_UNIT,
            NEW_MACHINE_PRICE,
            NEW_MACHINE_DEPRECIATION_PERIOD,
            NEW_MACHINE_PERIOD,
            CAPITAL_REQUIREMENT_NO,
            OPTIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            is_implemented=is_implemented
        )

    def __init_implemented_pessimistic(
            self,
            is_implemented: None | bool = None
    ) -> InvestmentBasic:
        PESSIMISTIC_PRICE_PER_UNIT = self.__calc_price_changes(
            PRICE_PER_UNIT,
            PESSIMISTIC_PRICE_PERCENT
        )
        PESSIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE = self.__calc_price_changes(
            NEW_MACHINE_LIQUIDATION_VALUE,
            PESSIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT
        )
        return InvestmentBasic(
            YEARS,
            SALES_VOL_YES,
            PRODUCTION_COSTS_YES,
            PESSIMISTIC_PRICE_PER_UNIT,
            NEW_MACHINE_PRICE,
            NEW_MACHINE_DEPRECIATION_PERIOD,
            NEW_MACHINE_PERIOD,
            CAPITAL_REQUIREMENT_YES,
            PESSIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            is_implemented=is_implemented
        )

    def __init_not_implemented_pessimistic(
            self,
            is_implemented: None | bool = None
    ) -> InvestmentBasic:
        PESSIMISTIC_PRICE_PER_UNIT = self.__calc_price_changes(
            PRICE_PER_UNIT,
            PESSIMISTIC_PRICE_PERCENT
        )
        PESSIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE = self.__calc_price_changes(
            NEW_MACHINE_LIQUIDATION_VALUE,
            PESSIMISTIC_NEW_MACHINE_LIQUIDATION_PERCENT
        )
        return InvestmentBasic(
            YEARS,
            SALES_VOL_NO,
            PRODUCTION_COSTS_NO,
            PESSIMISTIC_PRICE_PER_UNIT,
            NEW_MACHINE_PRICE,
            NEW_MACHINE_DEPRECIATION_PERIOD,
            NEW_MACHINE_PERIOD,
            CAPITAL_REQUIREMENT_NO,
            PESSIMISTIC_NEW_MACHINE_LIQUIDATION_VALUE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            is_implemented=is_implemented
        )

    @staticmethod
    def __rename_df_cols(df: pd.DataFrame) -> None:
        df.rename(columns=FIRST_STEP_TITLES, inplace=True)

    def write_step_one_to_excel_file(self) -> None:
        """
        Записывает данные первого шага в Excel файл. Данные будут записаны
        в следующем порядке:
            1. Лист "Основной":
                - При реализации инвестиционного проекта
                - При отказе от реализации инвестиционного проекта
            2. Лист "С учетом инфляции":
                - При реализации инвестиционного проекта
                - При отказе от реализации инвестиционного проекта
            3. Лист "Оптимистический":
                - При реализации инвестиционного проекта
                - При отказе от реализации инвестиционного проекта
            4. Лист "Пессимистический":
                - При реализации инвестиционного проекта
                - При отказе от реализации инвестиционного проекта
        :return: None
        """
        self.__write_to_excel(
            self.get_data_implemented_without_inflation(),
            sheet_name=RESULT_SHEET_1_NAME)
        self.__write_to_excel(
            self.get_data_not_implemented_without_inflation(),
            sheet_name=RESULT_SHEET_1_NAME)

        self.__write_to_excel(
            self.get_data_implemented_with_inflation(),
            sheet_name=RESULT_SHEET_2_NAME)
        self.__write_to_excel(
            self.get_data_not_implemented_with_inflation(),
            sheet_name=RESULT_SHEET_2_NAME)

        self.__create_chart_bar_for_cash_flow(
            RESULT_SHEET_1_NAME, DATA_COLUMN_NUM, LABELS_FOR_CHARTS
        )
        self.__create_chart_bar_for_cash_flow(
            RESULT_SHEET_2_NAME, DATA_COLUMN_NUM, LABELS_FOR_CHARTS
        )
        self.__write_to_excel(
            self.get_data_optimistic_scenario(is_implemented=True),
            sheet_name=RESULT_SHEET_3_NAME
        )
        self.__write_to_excel(
            self.get_data_optimistic_scenario(),
            sheet_name=RESULT_SHEET_3_NAME
        )
        self.__write_to_excel(
            self.get_data_pessimistic_scenario(is_implemented=True),
            sheet_name=RESULT_SHEET_4_NAME
        )
        self.__write_to_excel(
            self.get_data_pessimistic_scenario(),
            sheet_name=RESULT_SHEET_4_NAME
        )


if __name__ == "__main__":
    step_1 = Basic()
    step_1.write_step_one_to_excel_file()
