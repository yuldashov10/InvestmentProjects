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
    def depreciation_allowance(new_machine_price: int | float,
                               new_machine_depreciation_period: int,
                               new_machine_lifespan: int) -> list[float]:
        """
        Рассчитывает амортизационные отчисления.

        :param new_machine_price: Цена нового оборудования
        :param new_machine_depreciation_period: Срок амортизации
        нового оборудования
        :param new_machine_lifespan: Срок службы нового оборудования
        :return: Амортизационные отчисления за new_machine_depreciation_period
        период. Если new_machine_depreciation_period равен нулю, возвращает
        список нулей, длина списка равна new_machine_lifespan.
        Если new_machine_lifespan и new_machine_depreciation_period
        разные, то есть, new_machine_depreciation_period меньше, чем
        new_machine_lifespan, то список заполняется нулями.
        """

        # сокращенное название переменной
        nmdp = new_machine_depreciation_period

        if nmdp > new_machine_lifespan:
            raise ValueError("Амортизационный период нового оборудования "
                             "не может превышать срок службы оборудования")

        # список из нулей
        zeros = [0] * (new_machine_lifespan - nmdp)

        if nmdp == 0:
            return zeros

        depreciation = [round(new_machine_price / nmdp,
                              CURRENCY_ROUNDING_VALUE)] * nmdp
        return depreciation + zeros  # depreciation.extend(zeros)

    @staticmethod
    def taxable_profit(sales_vol: list[float | int],
                       prod_costs: list[float],
                       depreciation: list[float]) -> list[float]:

        """
        Рассчитывает налогооблагаемую прибыль.

        :param sales_vol: Объём реализации
        :param prod_costs: Издержки производства
        :param depreciation: Амортизационные отчисления
        :return: Налогооблагаемая прибыль
        """

        if not (len(sales_vol) == len(prod_costs) == len(depreciation)):
            raise ValueError("Количество элементов в 'Объём реализации', "
                             "'Издержки производства' и "
                             "'Амортизационные отчисления' различаются")

        return [round(sales_vol[i] - prod_costs[i] - depreciation[i],
                      CURRENCY_ROUNDING_VALUE)
                for i in range(len(sales_vol))]

    @staticmethod
    def profit_tax(taxable_profit_data: list[float],
                   tax_rate: float) -> list[float]:
        """
        Рассчитывает налог на прибыль.

        :param taxable_profit_data: Налогооблагаемая прибыль
        :param tax_rate: Налоговая ставка
        :return: Налог на прибыль. Если налогооблагаемая прибыль является
         отрицательным числом, то налог будет равен 0.
        """

        return [round(max(profit * tax_rate, 0), CURRENCY_ROUNDING_VALUE)
                for profit in taxable_profit_data]

    @staticmethod
    def net_profit(taxable_profit_data: list[float],
                   profit_tax_data: list[float]) -> list[float]:
        """
        Рассчитывает чистую прибыль.

        :param taxable_profit_data: Налогооблагаемая прибыль
        :param profit_tax_data: Налог на прибыль
        :return: Чистая прибыль.
        """

        if len(taxable_profit_data) != len(profit_tax_data):
            raise ValueError(
                "Количество элементов в 'Налогооблагаемая прибыль' "
                "и 'Налог на прибыль' различаются")

        return [round(taxable_profit_data[i] - profit_tax_data[i],
                      CURRENCY_ROUNDING_VALUE)
                for i in range(len(taxable_profit_data))]

    @staticmethod
    def cash_flow_from_op(depreciation: list[float],
                          net_profit_data: list[float]) -> list[float]:
        """
        Рассчитывает "Cash Flow From Operations".

        Денежные потоки от операций (CFFO) — это мера денежных средств,
        которые компания генерирует в результате своей обычной деятельности.
        Сюда входят деньги от таких вещей, как продажи, а также деньги,
        которые тратятся на такие вещи, как заработная плата, аренда и
        другие расходы.

        :param depreciation: Амортизационные отчисления
        :param net_profit_data: Чистая прибыль
        :return: Cash Flow From Operations
        """

        if len(depreciation) != len(net_profit_data):
            raise ValueError(
                "Количество элементов в 'Амортизационные отчисления' "
                "и 'Чистая прибыль' различаются"
            )

        return [round(depreciation[i] - net_profit_data[i],
                      CURRENCY_ROUNDING_VALUE)
                for i in range(len(depreciation))]

    @staticmethod
    def working_capital(sales_vol: list[float | int],
                        capital_requirement: float) -> list[float]:
        """
        Рассчитывает оборотный капитал.

        :param sales_vol: Объём реализации
        :param capital_requirement: Потребность в оборотном капитале
        :return: Оборотный капитал
        """

        return [round(vol * capital_requirement,
                      CURRENCY_ROUNDING_VALUE)
                for vol in sales_vol]

    @staticmethod
    def working_capital_gain(
            working_capital_data: list[float]) -> list[float]:

        """
        Рассчитывает прирост оборотного капитала.

        Первый элемент списка working_capital_data добавляется в gain 
        без изменений, затем в gain записывается значение по формуле:
        `текущее_значение - предыдущее`

        :param working_capital_data: Оборотный капитал
        :return: Прирост оборотного капитала
        """

        gain = [round(working_capital_data[i + 1] - working_capital_data[i],
                      CURRENCY_ROUNDING_VALUE)
                for i in range(len(working_capital_data))]

        gain.insert(0, working_capital_data[0])

        return gain

    @staticmethod
    def capital_investments(period: int,
                            new_machine_price: int | float,
                            old_liquidation: int | float,
                            new_liquidation: int | float,
                            tax_rate: float,
                            implemented=None) -> list[float]:
        """
        Рассчитывает капитальные выложения.\n\n

        ---

        **Первый и последний элемент рассчитываются по следующим формулам:**

        - При реализации:
            - Первый элемент списка: new_machine_price - (old_liquidation * (1 - tax_rate))
            - Последний элемент списка: new_liquidation - (new_liquidation * tax_rate)
        - При отказе от реализации:
            - Первый элемент списка: Равен 0
            - Последний элемент списка: old_liquidation - (old_liquidation * tax_rate)
        - Между этими элементами могут быть добавлены значение 0


        :param period: Период времени (Срок службы нового оборудования)
        :param new_machine_price: Цена нового оборудования
        :param old_liquidation: Ликвидационная стоимость старого оборудования
        :param new_liquidation: Ликвидационная стоимость нового оборудования
        :param tax_rate: Ставка налога на прибыль
        :param implemented: При реализации или при отказе от реализации.
        По умолчанию None
        :return: Капитальные выложения
        """

        zeros: list[int | float] = [0] * period

        if implemented is not None:
            last_item = old_liquidation - (old_liquidation * tax_rate)
            zeros.append(last_item)
            return zeros

        first_item = new_machine_price - (old_liquidation * (1 - tax_rate))
        last_item = new_liquidation - (new_liquidation * tax_rate)
        zeros[0] = first_item  # заменить первый элемент
        zeros.append(last_item)

        return zeros

    @staticmethod
    def cash_flow(depreciation: list[float],
                  net_profit_data: list[float],
                  working_capital_gain_data: list[float],
                  capital_investments_data: list[float]) -> list[float]:
        """
        Рассчитывает Cash Flow.

        Cash Flow (денежный поток) показывает реальный объем наличных
        и денег на счетах компании. Чтобы рассчитать показатель, нужно
        сложить все поступления денег за выбранный период и вычесть из
        них уже понесенные затраты - выбытия денег со счета.

        В начале реализации проекта (первый год) не может быть амортизации
        и чистой прибыли, поэтому к исходным данным depreciation и
        net_profit_data в начале добавляется значение 0 (ноль)

        :param depreciation: Амортизационные отчисления
        :param net_profit_data: Чистая прибыль
        :param working_capital_gain_data: Прирост оборотного капитала
        :param capital_investments_data: Капитальные выложения
        :return: Cash Flow
        """

        FIRST_YEAR_COST = 0

        depreciation.insert(0, FIRST_YEAR_COST)
        net_profit_data.insert(0, FIRST_YEAR_COST)

        if not (len(depreciation) ==
                len(net_profit_data) ==
                len(working_capital_gain_data) ==
                len(capital_investments_data)):
            raise ValueError(
                "Количество элементов в 'Амортизационные отчисления', "
                "'Чистая прибыль', 'Прирост оборотного капитала' и "
                "'Капитальные выложения' различаются"
            )

        return [
            round(
                (depreciation[i] + net_profit_data[i]) -
                (working_capital_gain_data[i] - capital_investments_data[i]),
                CURRENCY_ROUNDING_VALUE
            )
            for i in range(len(depreciation))
        ]


if __name__ == "__main__":
    pass
