from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class DepreciationAllowance(InvestmentProjectCalculator):
    """Рассчитывает амортизационные отчисления."""

    def __init__(
        self,
        new_machine_price: int | float,
        new_machine_depreciation_period: int,
        new_machine_lifespan: int,
        round_value: int = CURRENCY_ROUNDING_VALUE,
    ) -> None:
        """
        :param new_machine_price: Цена нового оборудования.
        :param new_machine_depreciation_period: Срок амортизации
        нового оборудования.
        :param new_machine_lifespan: Срок службы нового оборудования.
        :param round_value: Количество знаков после запятой при расчете.
        """
        self.new_machine_price = new_machine_price
        self.nmdp = new_machine_depreciation_period
        self.new_machine_lifespan = new_machine_lifespan
        self.__round = round_value

    def calc(self) -> list[float]:
        """Рассчитывает амортизационные отчисления.
        - Амортизационные отчисления за `new_machine_depreciation_period` период.
        - Если `new_machine_depreciation_period` равен нулю, возвращает
        список нулей, длина списка равна `new_machine_lifespan`.
        - Если new_machine_lifespan и `new_machine_depreciation_period` разные,
        то есть, `new_machine_depreciation_period` меньше, чем
        `new_machine_lifespan`, то список заполняется нулями."""

        if self.nmdp > self.new_machine_lifespan:
            raise ValueError(
                "Амортизационный период нового оборудования "
                "не может превышать срок службы оборудования"
            )

        # список из нулей
        zeros = [0] * (self.new_machine_lifespan - self.nmdp)

        if self.nmdp == 0:
            return zeros

        depreciation = [
            round(self.new_machine_price / self.nmdp, self.__round)
        ] * self.nmdp
        # depreciation.extend(zeros)
        return depreciation + zeros
