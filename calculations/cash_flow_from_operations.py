from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class CashFlowFromOperations(InvestmentProjectCalculator):
    """Рассчитывает "Cash Flow From Operations" (CFFO)."""

    def __init__(
        self,
        depreciation: list[float],
        net_profit_data: list[float],
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """Денежные потоки от операций (CFFO) — это мера денежных средств,
        которые компания генерирует в результате своей обычной деятельности.
        Сюда входят деньги от таких вещей, как продажи, а также деньги,
        которые тратятся на такие вещи, как заработная плата, аренда и
        другие расходы.
        :param depreciation: Амортизационные отчисления.
        :param net_profit_data: Чистая прибыль.
        :param round_value: Количество знаков после запятой при расчете."""
        self.depreciation = depreciation
        self.net_profit_data = net_profit_data
        self.__round = round_value

    def __is_same_length(self) -> bool:
        return len(self.depreciation) == len(self.net_profit_data)

    def calc(self) -> list[float]:
        """Рассчитывает "Cash Flow From Operations".
        :return: Cash Flow From Operations."""
        if not self.__is_same_length():
            raise ValueError(
                "Количество элементов в 'Амортизационные отчисления' "
                "и 'Чистая прибыль' различаются"
            )

        return [
            round(self.depreciation[i] + self.net_profit_data[i], self.__round)
            for i in range(len(self.depreciation))
        ]
