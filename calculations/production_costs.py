from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class ProductionCosts(InvestmentProjectCalculator):
    """Рассчитывает производственные издержки.
    На единицу продукции с учетом инфляции и без нее.
    """

    def __init__(
        self,
        annual_sales: list[int],
        production_costs_per_unit: list[float],
        inflation: float = None,
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """Формула расчета с учетом инфляции:\n
        `annual_sales[time_period - 1]
        * (costs * (1 + inflation) ** time_period)`

        Формула расчета без учета инфляции:\n
        `annual_sales[time_period - 1] * costs`

        * time_period - момент времени (год);
        * annual_sales[time_period - 1] - объём
          продаж в `time_period` момент времени;
        * costs - производственные издержки в `time_period` момент времени;
        * inflation - годовой темп инфляции;

        :param annual_sales: Годовой объем продаж(шт.)
        :param production_costs_per_unit: Производственные издержки.
        :param inflation: Годовой темп инфляции. По умолчанию None.
        :param round_value: Количество знаков после запятой при расчете.
        """

        self.annual_sales = annual_sales
        self.production_costs_per_unit = production_costs_per_unit
        self.inflation = inflation
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает производственные издержки.
        На единицу продукции с учетом инфляции и без нее.
        :return: Издержки производства.
        """
        if len(self.annual_sales) != len(self.production_costs_per_unit):
            raise ValueError(
                "Данные о годовых продажах и производственных "
                "издержках не совпадают по количеству элементов"
            )
        if self.inflation is not None:
            return [
                round(
                    self.annual_sales[time_period - 1]
                    * (costs * (1 + self.inflation) ** time_period),
                    self.__round,
                )
                for time_period, costs in enumerate(
                    self.production_costs_per_unit, start=1
                )
            ]

        return [
            round(
                self.annual_sales[time_period - 1] * costs,
                self.__round,
            )
            for time_period, costs in enumerate(
                self.production_costs_per_unit, start=1
            )
        ]
