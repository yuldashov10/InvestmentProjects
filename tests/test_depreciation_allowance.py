from calculations.index import Index
from data import (
    EXPECTED_DEPRECIATION,
    NEW_MACHINE_PRICE,
    NEW_MACHINE_DEPRECIATION_PERIOD,
    NEW_MACHINE_LIFESPAN
)


def test_depreciation_allowance(new_machine_price,
                                nmdp,
                                new_machine_lifespan):
    return Index.depreciation_allowance(
        new_machine_price, nmdp, new_machine_lifespan)


if __name__ == "__main__":
    assert test_depreciation_allowance(NEW_MACHINE_PRICE, NEW_MACHINE_DEPRECIATION_PERIOD, NEW_MACHINE_LIFESPAN) == EXPECTED_DEPRECIATION["depreciation_yes"]
    assert test_depreciation_allowance(NEW_MACHINE_PRICE, 0, NEW_MACHINE_LIFESPAN) == EXPECTED_DEPRECIATION["depreciation_no"]
