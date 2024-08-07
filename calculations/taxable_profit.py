from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class TaxableProfit(InvestmentProjectCalculator):
    """Рассчитывает налогооблагаемую прибыль."""

    def __init__(
        self,
        sales_vol: list[float | int],
        prod_costs: list[float],
        depreciation: list[float],
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        :param sales_vol: Объём реализации.
        :param prod_costs: Издержки производства.
        :param depreciation: Амортизационные отчисления
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.sales_vol = sales_vol
        self.prod_costs = prod_costs
        self.depreciation = depreciation
        self.__round = round_value

    def __is_same_length(self) -> bool:
        return (
            len(self.sales_vol)
            == len(self.prod_costs)
            == len(self.depreciation)
        )

    def calc(self) -> list[float]:
        """Рассчитывает налогооблагаемую прибыль.
        :return: Налогооблагаемая прибыль."""

        if not self.__is_same_length():
            raise ValueError(
                "Количество элементов в "
                "'Объём реализации', 'Издержки производства' и "
                "'Амортизационные отчисления' различаются"
            )

        return [
            round(
                self.sales_vol[i] - self.prod_costs[i] - self.depreciation[i],
                self.__round,
            )
            for i in range(len(self.sales_vol))
        ]
