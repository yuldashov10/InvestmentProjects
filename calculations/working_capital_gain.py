from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class WorkingCapitalGain(InvestmentProjectCalculator):
    """Рассчитывает прирост оборотного капитала."""

    def __init__(
        self,
        working_capital_data: list[float],
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        Первый элемент списка `working_capital_data` добавляется в `gain`
        без изменений, затем в `gain` записывается значение по формуле:
        `текущее_значение - предыдущее`. Последним элементом добавляется
        в `gain` последнее значение из `working_capital_data`.
        :param working_capital_data: Оборотный капитал.
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.working_capital_data = working_capital_data
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает прирост оборотного капитала.
        :return: Прирост оборотного капитала."""
        gain: list[float] = [
            round(
                self.working_capital_data[i + 1]
                - self.working_capital_data[i],
                self.__round,
            )
            for i in range(len(self.working_capital_data) - 1)
        ]

        first_item = self.working_capital_data[0]
        last_item = -self.working_capital_data[-1]  # добавляется знак минус
        gain.insert(0, first_item)
        gain.append(last_item)

        return gain
