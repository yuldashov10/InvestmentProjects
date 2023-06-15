from utils.settings import CURRENCY_ROUNDING_VALUE


class Index:

    @staticmethod
    def sales_volume(
            annual_sales: list[int],
            unit_price: float | int,
            inflation=None) -> list[float | int]:
        """
        Рассчитывает объем продаж с учетом инфляции и без нее.

        Формула расчета с учетом инфляции:
        t - момент времени (год)
        unit_price - цена за единицу продукции
        sale - объём продаж в t момент времени
        inflation - годовой темп инфляции

        sale * (unit_price * (1 + inflation) ** t)

        Формула расчета без учета инфляции:
        sale * unit_price


        :param annual_sales: Годовой объем продаж(шт.)
        :param unit_price: Цена за единицу продукции
        :param inflation: Годовой темп инфляции. По умолчанию None
        :return: Объём реализации, список чисел (int или float)
        """

        if inflation is not None:
            # t - период времени
            # start=1 - в нулевой году не может быть никакие продажи,
            # только после года появляется объём продаж.
            return [
                round(sale * (unit_price * (1 + inflation) ** t),
                      CURRENCY_ROUNDING_VALUE)
                for t, sale in enumerate(annual_sales, start=1)
            ]

        return [
            round(sale * unit_price, CURRENCY_ROUNDING_VALUE)
            for sale in annual_sales
        ]

    @staticmethod
    def production_costs(annual_sales: list[int],
                         production_costs_per_unit: list[float],
                         inflation=None) -> list[float]:
        """
        Рассчитывает производственные издержки на единицу продукции
        с учетом инфляции и без нее.

        Формула расчета с учетом инфляции:
        t - момент времени (год)
        annual_sales[t - 1] - объём продаж в t момент времени
        costs - производственные издержки в t момент времени
        inflation - годовой темп инфляции

        annual_sales[t - 1] * (costs * (1 + inflation) ** t)

        Формула расчета без учета инфляции:

        annual_sales[t - 1] * costs

        :param annual_sales: Годовой объем продаж(шт.)
        :param production_costs_per_unit: Производственные издержки
        :param inflation: Годовой темп инфляции. По умолчанию None
        :return: Издержки производства
        """

        if len(annual_sales) != len(production_costs_per_unit):
            raise ValueError(
                "Данные о годовых продажах и производственных "
                "издержках не совпадают по количеству элементов")

        if inflation is not None:
            return [
                round(annual_sales[t - 1] * (costs * (1 + inflation) ** t),
                      CURRENCY_ROUNDING_VALUE)
                for t, costs in enumerate(production_costs_per_unit, start=1)
            ]

        return [round(annual_sales[t - 1] * costs, CURRENCY_ROUNDING_VALUE)
                for t, costs in enumerate(production_costs_per_unit, start=1)]

    @staticmethod
    def depreciation_allowance():
        # А (Амортизационные отчисления)(₽)
        pass

    @staticmethod
    def taxable_profit():
        # НОП (Налогооблагаемая прибыль)(₽)
        pass

    @staticmethod
    def profit_tax():
        # Н (Налог на прибыль)(₽)
        pass

    @staticmethod
    def net_profit():
        # ЧП (Чистая прибыль)(₽)
        pass

    @staticmethod
    def cash_flow_from_op():
        # CFFO (Cash Flow From Operations)(₽)
        # Операционный денежный поток
        pass

    @staticmethod
    def working_capital():
        # ОК (Оборотный капитал)(₽)
        pass

    @staticmethod
    def working_capital_gain():
        # ПОК (Прирост оборотного капитала)(₽)
        pass

    @staticmethod
    def capital_investments():
        # КВ (Капитальные вложения)(₽)
        pass

    @staticmethod
    def cash_flow():
        # Денежный поток
        # CF (Cash Flow)(₽)
        pass


if __name__ == "__main__":
    pass
