from calculations.index import Index
from data import (
    EXPECTED_DEPRECIATION,
    EXPECTED_PROD_COSTS,
    EXPECTED_SALES_VOLUME,
    EXPECTED_TAXABLE_PROFIT,
)


def test_taxable_profit(sales_vol, prod_costs, depreciation):
    return Index.taxable_profit(sales_vol, prod_costs, depreciation)


if __name__ == "__main__":
    # calc data
    taxable_profit_yes = test_taxable_profit(
        EXPECTED_SALES_VOLUME["sales_vol_yes"],
        EXPECTED_PROD_COSTS["prod_sales_yes"],
        EXPECTED_DEPRECIATION["depreciation_yes"]
    )

    taxable_profit_no = test_taxable_profit(
        EXPECTED_SALES_VOLUME["sales_vol_no"],
        EXPECTED_PROD_COSTS["prod_sales_no"],
        EXPECTED_DEPRECIATION["depreciation_no"]
    )

    taxable_profit_infl_yes = test_taxable_profit(
        EXPECTED_SALES_VOLUME["sales_vol_infl_yes"],
        EXPECTED_PROD_COSTS["prod_sales_infl_yes"],
        EXPECTED_DEPRECIATION["depreciation_yes"]

    )
    taxable_profit_infl_no = test_taxable_profit(
        EXPECTED_SALES_VOLUME["sales_vol_infl_no"],
        EXPECTED_PROD_COSTS["prod_sales_infl_no"],
        EXPECTED_DEPRECIATION["depreciation_no"]
    )

    # test
    assert taxable_profit_yes == EXPECTED_TAXABLE_PROFIT["taxable_profit_yes"]
    assert taxable_profit_no == EXPECTED_TAXABLE_PROFIT["taxable_profit_no"]
    assert taxable_profit_infl_yes == EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_yes"]
    assert taxable_profit_infl_no == EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_no"]
