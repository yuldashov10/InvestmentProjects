import pandas as pd

from investments.base import InvestmentBasic

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
    DEPRECIATION_PERIOD_WHEN_PROJECT_NOT_IMPLEMENTED,
    FIRST_STEP_TITLES, RESULT_FILE_PATH,
)


class RunStep:
    def __init__(self,
                 sheet_name: str,
                 inflation: float = None,
                 is_implemented: bool = None,
                 is_truncate_sheet: bool = None):
        self.__sheet_name = sheet_name
        self.__is_inflation = inflation
        self.__is_implemented = is_implemented
        self.__is_truncate_sheet = is_truncate_sheet

        if is_implemented is None:
            self.__data = self.__init_not_implemented()
            self.__df = pd.DataFrame(self.__data.get_data())
        else:
            self.__data = self.__init_implemented()
            self.__df = pd.DataFrame(self.__data.get_data())

        self.__filename = RESULT_FILE_PATH
        self.__rename_df_cols()

    def __init_implemented(self):
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
            is_implemented=self.__is_implemented,
            inflation=self.__is_inflation
        )

    def __init_not_implemented(self):
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
            inflation=self.__is_inflation
        )

    def __rename_df_cols(self):
        self.__df.rename(columns=FIRST_STEP_TITLES, inplace=True)

    def __write_to_excel(self):
        self.__data.append_data_to_excel(
            self.__filename,
            self.__df,
            sheet_name=self.__sheet_name,
            index=False,
            is_truncate_sheet=self.__is_truncate_sheet
        )

    def run_step_1(self):
        self.__write_to_excel()


if __name__ == "__main__":
    sheet_names = [
        "Основной", "Основной", "С учетом инфляции", "С учетом инфляции"
    ]
    is_implemented = [True, None, True, None]
    inflation_data = [None, None, INFLATION, INFLATION]

    for sheet_name, implemented, inflation in zip(sheet_names,
                                                  is_implemented,
                                                  inflation_data):
        step_1 = RunStep(sheet_name,
                         inflation=inflation,
                         is_implemented=implemented)
        step_1.run_step_1()
