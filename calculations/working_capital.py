from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class WorkingCapital(InvestmentProjectCalculator):
    """Рассчитывает оборотный капитал."""

    def __init__(
        self,
        sales_volume: list[float | int],
        capital_requirement: float,
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        :param sales_volume: Объём реализации.
        :param capital_requirement: Потребность в оборотном капитале.
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.sales_volume = sales_volume
        self.capital_requirement = capital_requirement
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает оборотный капитал.
        :return: Оборотный капитал"""

        return [
            round(vol * self.capital_requirement, self.__round)
            for vol in self.sales_volume
        ]
