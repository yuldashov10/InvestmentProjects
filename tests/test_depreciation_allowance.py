import pytest

from calculations.depreciation_allowance import DepreciationAllowance
from tests.data import (
    EXPECTED_DEPRECIATION,
    NEW_MACHINE_DEPRECIATION_PERIOD,
    NEW_MACHINE_LIFESPAN,
    NEW_MACHINE_PRICE,
)


@pytest.mark.parametrize(
    "new_machine_price, nmdp, new_machine_lifespan, expected_key",
    [
        (
            NEW_MACHINE_PRICE,
            NEW_MACHINE_DEPRECIATION_PERIOD,
            NEW_MACHINE_LIFESPAN,
            "depreciation_yes",
        ),
        (
            NEW_MACHINE_PRICE,
            0,
            NEW_MACHINE_LIFESPAN,
            "depreciation_no",
        ),
    ],
)
def test_depreciation_allowance(
    new_machine_price, nmdp, new_machine_lifespan, expected_key
):
    da = DepreciationAllowance(new_machine_price, nmdp, new_machine_lifespan)
    result = da.calc()
    expected = EXPECTED_DEPRECIATION[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
