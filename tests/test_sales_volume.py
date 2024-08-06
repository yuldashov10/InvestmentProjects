import pytest

from calculations.sales_volume import SalesVolume
from tests.data import (
    ANNUAL_SALES_NO,
    ANNUAL_SALES_YES,
    EXPECTED_SALES_VOLUME,
    INFLATION,
    UNIT_PRICE,
)


@pytest.mark.parametrize(
    "sales, unit_price, inflation, expected",
    [
        (
            ANNUAL_SALES_YES,
            UNIT_PRICE,
            None,
            EXPECTED_SALES_VOLUME["sales_vol_yes"],
        ),
        (
            ANNUAL_SALES_NO,
            UNIT_PRICE,
            None,
            EXPECTED_SALES_VOLUME["sales_vol_no"],
        ),
        (
            ANNUAL_SALES_YES,
            UNIT_PRICE,
            INFLATION,
            EXPECTED_SALES_VOLUME["sales_vol_infl_yes"],
        ),
        (
            ANNUAL_SALES_NO,
            UNIT_PRICE,
            INFLATION,
            EXPECTED_SALES_VOLUME["sales_vol_infl_no"],
        ),
    ],
)
def test_sales_volume(sales, unit_price, inflation, expected):
    sv = SalesVolume(sales, unit_price, inflation)
    result: list[int | float] = sv.calc()
    assert result == expected, f"Ожидается {expected} получено {result}"
