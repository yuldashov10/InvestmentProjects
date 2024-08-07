import pytest

from calculations.profit_tax import ProfitTax
from tests.data import EXPECTED_PROFIT_TAX, EXPECTED_TAXABLE_PROFIT, TAX_RATE


@pytest.mark.parametrize(
    "taxable_profit_data, expected_key",
    [
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_yes"],
            "profit_tax_yes",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_no"],
            "profit_tax_no",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_yes"],
            "profit_tax_infl_yes",
        ),
        (
            EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_no"],
            "profit_tax_infl_no",
        ),
    ],
)
def test_profit_tax(taxable_profit_data, expected_key):
    pt = ProfitTax(taxable_profit_data, TAX_RATE)
    result = pt.calc()
    expected = EXPECTED_PROFIT_TAX[expected_key]
    assert result == expected, f"Ожидается {expected} получено {result}"
