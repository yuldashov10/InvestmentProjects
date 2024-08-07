import pytest

from calculations.net_profit import NetProfit
from tests.data import (
    EXPECTED_NET_PROFIT,
    EXPECTED_PROFIT_TAX,
    EXPECTED_TAXABLE_PROFIT,
)


@pytest.mark.parametrize(
    "taxable_profit_data, profit_tax_data, expected_key",
    [
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_yes"],
            EXPECTED_PROFIT_TAX["profit_tax_yes"],
            "net_profit_yes",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_no"],
            EXPECTED_PROFIT_TAX["profit_tax_no"],
            "net_profit_no",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_yes"],
            EXPECTED_PROFIT_TAX["profit_tax_infl_yes"],
            "net_profit_infl_yes",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_no"],
            EXPECTED_PROFIT_TAX["profit_tax_infl_no"],
            "net_profit_infl_no",
        ),
    ],
)
def test_net_profit(taxable_profit_data, profit_tax_data, expected_key):
    np = NetProfit(taxable_profit_data, profit_tax_data)
    result = np.calc()
    expected = EXPECTED_NET_PROFIT[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
