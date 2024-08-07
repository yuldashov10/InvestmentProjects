import pytest

from calculations.working_capital import WorkingCapital
from tests.data import (
    CAPITAL_REQUIREMENT_NO,
    CAPITAL_REQUIREMENT_YES,
    EXPECTED_SALES_VOLUME,
    EXPECTED_WORKING_CAPITAL,
)


@pytest.mark.parametrize(
    "sales_vol, capital_requirement, expected_key",
    [
        (
            EXPECTED_SALES_VOLUME["sales_vol_yes"],
            CAPITAL_REQUIREMENT_YES,
            "working_capital_yes",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_no"],
            CAPITAL_REQUIREMENT_NO,
            "working_capital_no",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_infl_yes"],
            CAPITAL_REQUIREMENT_YES,
            "working_capital_infl_yes",
        ),
        (
            EXPECTED_SALES_VOLUME["sales_vol_infl_no"],
            CAPITAL_REQUIREMENT_NO,
            "working_capital_infl_no",
        ),
    ],
)
def test_working_capital(sales_vol, capital_requirement, expected_key):
    wc = WorkingCapital(sales_vol, capital_requirement)
    result = wc.calc()
    expected = EXPECTED_WORKING_CAPITAL[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
