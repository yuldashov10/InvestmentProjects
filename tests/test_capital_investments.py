from calculations.index import Index
from data import (
    EXPECTED_CAPITAL_INVEST,
    NEW_MACHINE_LIFESPAN,
    NEW_MACHINE_LIQUIDATION_VALUE,
    NEW_MACHINE_PRICE,
    OLD_MACHINE_LIQUIDATION_VALUE,
    TAX_RATE
)


def test_capital_investments(period, new_machine_price,
                             old_liquidation, new_liquidation,
                             tax_rate, implemented=None):
    return Index.capital_investments(
        period, new_machine_price,
        old_liquidation, new_liquidation,
        tax_rate, implemented
    )


if __name__ == "__main__":
    capital_invest_yes = test_capital_investments(
        NEW_MACHINE_LIFESPAN,
        NEW_MACHINE_PRICE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        NEW_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
    )
    capital_invest_no = test_capital_investments(
        NEW_MACHINE_LIFESPAN,
        NEW_MACHINE_PRICE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        NEW_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
        implemented=False
    )

    capital_invest_infl_yes = test_capital_investments(
        NEW_MACHINE_LIFESPAN,
        NEW_MACHINE_PRICE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        NEW_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
    )
    capital_invest_infl_no = test_capital_investments(
        NEW_MACHINE_LIFESPAN,
        NEW_MACHINE_PRICE,
        OLD_MACHINE_LIQUIDATION_VALUE,
        NEW_MACHINE_LIQUIDATION_VALUE,
        TAX_RATE,
        implemented=False
    )

    assert capital_invest_yes == EXPECTED_CAPITAL_INVEST["capital_invest_yes"]
    assert capital_invest_no == EXPECTED_CAPITAL_INVEST["capital_invest_no"]
    assert capital_invest_infl_yes == EXPECTED_CAPITAL_INVEST["capital_invest_infl_yes"]
    assert capital_invest_infl_no == EXPECTED_CAPITAL_INVEST["capital_invest_infl_no"]
