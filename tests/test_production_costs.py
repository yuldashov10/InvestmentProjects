from calculations.index import Index
from data import (
    ANNUAL_SALES_YES,
    ANNUAL_SALES_NO,
    EXPECTED_PROD_COSTS,
    INFLATION,
    PROD_COSTS_YES,
    PROD_COSTS_NO,
)


def test_production_costs(annual_sales,
                          production_costs_per_unit,
                          inflation=None):
    if inflation is not None:
        return Index.production_costs(
            annual_sales, production_costs_per_unit, inflation)
    return Index.production_costs(annual_sales, production_costs_per_unit)


if __name__ == "__main__":
    assert test_production_costs(ANNUAL_SALES_YES, PROD_COSTS_YES) == EXPECTED_PROD_COSTS["prod_sales_yes"]
    assert test_production_costs(ANNUAL_SALES_NO, PROD_COSTS_NO) == EXPECTED_PROD_COSTS["prod_sales_no"]
    assert test_production_costs(ANNUAL_SALES_YES, PROD_COSTS_YES, INFLATION) == EXPECTED_PROD_COSTS["prod_sales_infl_yes"]
    assert test_production_costs(ANNUAL_SALES_NO, PROD_COSTS_NO, INFLATION) == EXPECTED_PROD_COSTS["prod_sales_infl_no"]
