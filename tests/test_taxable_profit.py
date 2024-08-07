import pytest

from calculations.taxable_profit import TaxableProfit
from tests.data import (
    EXPECTED_DEPRECIATION,
    EXPECTED_PROD_COSTS,
    EXPECTED_SALES_VOLUME,
    EXPECTED_TAXABLE_PROFIT,
)


@pytest.mark.parametrize(
    "sales_vol, prod_costs, depreciation, expected_key",
    [
        (
            EXPECTED_SALES_VOLUME["sales_vol_yes"],
            EXPECTED_PROD_COSTS["prod_sales_yes"],
            EXPECTED_DEPRECIATION["depreciation_yes"],
            "taxable_profit_yes",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_no"],
            EXPECTED_PROD_COSTS["prod_sales_no"],
            EXPECTED_DEPRECIATION["depreciation_no"],
            "taxable_profit_no",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_infl_yes"],
            EXPECTED_PROD_COSTS["prod_sales_infl_yes"],
            EXPECTED_DEPRECIATION["depreciation_yes"],
            "taxable_profit_infl_yes",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_infl_no"],
            EXPECTED_PROD_COSTS["prod_sales_infl_no"],
            EXPECTED_DEPRECIATION["depreciation_no"],
            "taxable_profit_infl_no",
        ),
    ],
)
def test_taxable_profit(sales_vol, prod_costs, depreciation, expected_key):
    tp = TaxableProfit(sales_vol, prod_costs, depreciation)
    result = tp.calc()
    expected = EXPECTED_TAXABLE_PROFIT[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
