import pytest

from calculations.capital_investments import CapitalInvestments
from tests.data import (
    EXPECTED_CAPITAL_INVEST,
    NEW_MACHINE_LIFESPAN,
    NEW_MACHINE_LIQUIDATION_VALUE,
    NEW_MACHINE_PRICE,
    OLD_MACHINE_LIQUIDATION_VALUE,
    TAX_RATE,
)


@pytest.mark.parametrize(
    "period, new_machine_price, old_liquidation, new_liquidation, tax_rate, implemented, expected_key",
    [
        (
            NEW_MACHINE_LIFESPAN,
            NEW_MACHINE_PRICE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            NEW_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            True,
            "capital_invest_yes",
        ),
        (
            NEW_MACHINE_LIFESPAN,
            NEW_MACHINE_PRICE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            NEW_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            False,
            "capital_invest_no",
        ),
        (
            NEW_MACHINE_LIFESPAN,
            NEW_MACHINE_PRICE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            NEW_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            True,
            "capital_invest_infl_yes",
        ),
        (
            NEW_MACHINE_LIFESPAN,
            NEW_MACHINE_PRICE,
            OLD_MACHINE_LIQUIDATION_VALUE,
            NEW_MACHINE_LIQUIDATION_VALUE,
            TAX_RATE,
            False,
            "capital_invest_infl_no",
        ),
    ],
)
def test_capital_investments(
    period,
    new_machine_price,
    old_liquidation,
    new_liquidation,
    tax_rate,
    implemented,
    expected_key,
):
    ci = CapitalInvestments(
        period,
        new_machine_price,
        old_liquidation,
        new_liquidation,
        tax_rate,
        implemented,
    )
    result = ci.calc()
    expected = EXPECTED_CAPITAL_INVEST[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
