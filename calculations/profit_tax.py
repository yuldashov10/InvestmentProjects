from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class ProfitTax(InvestmentProjectCalculator):
    """Рассчитывает налог на прибыль."""

    def __init__(
        self,
        taxable_profit_data: list[float],
        tax_rate: float,
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        :param taxable_profit_data: Налогооблагаемая прибыль.
        :param tax_rate: Налоговая ставка.
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.taxable_profit_data = taxable_profit_data
        self.tax_rate = tax_rate
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает налог на прибыль.
        :return: Налог на прибыль. Если налогооблагаемая прибыль
        является отрицательным числом, то налог будет равен 0.
        """

        return [
            round(max(profit * self.tax_rate, 0), self.__round)
            for profit in self.taxable_profit_data
        ]
