from calculations.index import Index
from data import (
    ANNUAL_SALES_YES,
    ANNUAL_SALES_NO,
    EXPECTED_SALES_VOLUME,
    INFLATION,
    UNIT_PRICE
)


def test_sales_volume(sales, unit_price, inflation=None):
    if inflation is not None:
        return Index.sales_volume(sales, unit_price, inflation)
    return Index.sales_volume(sales, unit_price)


if __name__ == "__main__":
    assert test_sales_volume(ANNUAL_SALES_YES, UNIT_PRICE) == EXPECTED_SALES_VOLUME["sales_vol_yes"]
    assert test_sales_volume(ANNUAL_SALES_NO, UNIT_PRICE) == EXPECTED_SALES_VOLUME["sales_vol_no"]

    assert test_sales_volume(ANNUAL_SALES_YES, UNIT_PRICE, INFLATION) == EXPECTED_SALES_VOLUME["sales_vol_infl_yes"]
    assert test_sales_volume(ANNUAL_SALES_NO, UNIT_PRICE, INFLATION) == EXPECTED_SALES_VOLUME["sales_vol_infl_no"]
