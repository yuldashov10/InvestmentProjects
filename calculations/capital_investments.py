from calculations.base import InvestmentProjectCalculator


class CapitalInvestments(InvestmentProjectCalculator):
    """Рассчитывает капитальные вложения."""

    def __init__(
        self,
        period: int,
        new_machine_price: int | float,
        old_liquidation: int | float,
        new_liquidation: int | float,
        tax_rate: float,
        is_implemented: bool = False,
    ) -> None:
        """Первый и последний элемент рассчитываются по следующим формулам:
        - При реализации:
            - Первый элемент списка:
            `new_machine_price - (old_liquidation * (1 - tax_rate))`
            - Последний элемент списка:
            `new_liquidation - (new_liquidation * tax_rate)`
        - При отказе от реализации:
            - Первый элемент списка: Равен 0
            - Последний элемент списка:
            `old_liquidation - (old_liquidation * tax_rate)`
        - Между этими элементами могут быть добавлены значение 0.

        :param period: Период времени (Срок службы нового оборудования).
        :param new_machine_price: Цена нового оборудования.
        :param old_liquidation: Ликвидационная стоимость старого оборудования.
        :param new_liquidation: Ликвидационная стоимость нового оборудования.
        :param tax_rate: Ставка налога на прибыль.
        :param is_implemented: При реализации или при отказе от реализации.
        По умолчанию False.
        """
        self.period = period
        self.new_machine_price = new_machine_price
        self.old_liquidation = old_liquidation
        self.new_liquidation = new_liquidation
        self.tax_rate = tax_rate
        self.is_implemented = is_implemented

    def calc(self) -> list[float]:
        """Рассчитывает капитальные вложения.
        :return: Капитальные вложения."""
        coefficient: int = 1
        zeros: list[int | float] = [0] * self.period

        if not self.is_implemented:
            last_item: float = self.old_liquidation - (
                self.old_liquidation * self.tax_rate
            )
            zeros.append(last_item)
            return zeros

        first_item: float = abs(
            self.new_machine_price
            - (self.old_liquidation * (coefficient - self.tax_rate))
        )
        last_item: float = self.new_liquidation - (
            self.new_liquidation * self.tax_rate
        )
        zeros[0] = first_item  # заменить первый элемент
        zeros.append(last_item)
        return zeros
