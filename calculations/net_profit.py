from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class NetProfit(InvestmentProjectCalculator):
    """Рассчитывает чистую прибыль."""

    def __init__(
        self,
        taxable_profit_data: list[float],
        profit_tax_data: list[float],
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        :param taxable_profit_data: Налогооблагаемая прибыль.
        :param profit_tax_data: Налог на прибыль.
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.taxable_profit_data = taxable_profit_data
        self.profit_tax_data = profit_tax_data
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает чистую прибыль.
        :return: Чистая прибыль."""
        if len(self.taxable_profit_data) != len(self.profit_tax_data):
            raise ValueError(
                "Количество элементов в 'Налогооблагаемая прибыль' "
                "и 'Налог на прибыль' различаются"
            )

        return [
            round(
                self.taxable_profit_data[i] - self.profit_tax_data[i],
                self.__round,
            )
            for i in range(len(self.taxable_profit_data))
        ]
