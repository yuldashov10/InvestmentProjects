import pytest

from calculations.production_costs import ProductionCosts
from tests.data import (
    ANNUAL_SALES_NO,
    ANNUAL_SALES_YES,
    EXPECTED_PROD_COSTS,
    INFLATION,
    PROD_COSTS_NO,
    PROD_COSTS_YES,
)


@pytest.mark.parametrize(
    "annual_sales, production_costs_per_unit, inflation, expected_key",
    [
        (
            ANNUAL_SALES_YES,
            PROD_COSTS_YES,
            None,
            "prod_sales_yes",
        ),
        (
            ANNUAL_SALES_NO,
            PROD_COSTS_NO,
            None,
            "prod_sales_no",
        ),
        (
            ANNUAL_SALES_YES,
            PROD_COSTS_YES,
            INFLATION,
            "prod_sales_infl_yes",
        ),
        (
            ANNUAL_SALES_NO,
            PROD_COSTS_NO,
            INFLATION,
            "prod_sales_infl_no",
        ),
    ],
)
def test_production_costs(
    annual_sales, production_costs_per_unit, inflation, expected_key
):
    pc = ProductionCosts(annual_sales, production_costs_per_unit, inflation)
    result = pc.calc()
    expected = EXPECTED_PROD_COSTS[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
