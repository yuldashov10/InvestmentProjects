from calculations.base import InvestmentProjectCalculator
from utils.settings import CURRENCY_ROUNDING_VALUE


class SalesVolume(InvestmentProjectCalculator):
    """Рассчитывает объем продаж с учетом инфляции и без нее."""

    def __init__(
        self,
        annual_sales: list[int],
        unit_price: float | int,
        inflation: float = None,
    ) -> None:
        """Формула расчета с учетом инфляции:\n
        `sale * (unit_price * (1 + inflation) ** time_period)`

        Формула расчета без учета инфляции:\n
        `sale * unit_price`

        - time_period - момент времени (год);
        - unit_price - цена за единицу продукции;
        - sale - объём продаж в `time_period` момент времени;
        - inflation - годовой темп инфляции.\n

        :param annual_sales: Годовой объем продаж(шт.).
        :param unit_price: Цена за единицу продукции.
        :param inflation: Годовой темп инфляции. По умолчанию None.
        """

        self.annual_sales = annual_sales
        self.unit_price = unit_price
        self.inflation = inflation

    def calc(self) -> list[float | int]:
        """Рассчитывает объем продаж с учетом инфляции и без нее.
        :return: Объём реализации, список чисел (int или float)
        """
        if self.inflation is not None:
            return [
                round(
                    sale
                    * (self.unit_price * (1 + self.inflation) ** time_period),
                    CURRENCY_ROUNDING_VALUE,
                )
                for time_period, sale in enumerate(self.annual_sales, start=1)
                # `start=1` - в нулевом году объём продаж отсутствует,
                # появится только после первого года.
            ]

        return [
            round(sale * self.unit_price, CURRENCY_ROUNDING_VALUE)
            for sale in self.annual_sales
        ]
