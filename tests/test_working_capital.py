from calculations.index import Index
from data import (
    CAPITAL_REQUIREMENT_NO,
    CAPITAL_REQUIREMENT_YES,
    EXPECTED_SALES_VOLUME,
    EXPECTED_WORKING_CAPITAL
)


def test_working_capital(sales_vol, capital_requirement):
    return Index.working_capital(sales_vol, capital_requirement)


if __name__ == "__main__":
    working_capital_yes = test_working_capital(
        EXPECTED_SALES_VOLUME["sales_vol_yes"],
        CAPITAL_REQUIREMENT_YES
    )
    working_capital_no = test_working_capital(
        EXPECTED_SALES_VOLUME["sales_vol_no"],
        CAPITAL_REQUIREMENT_NO
    )
    working_capital_infl_yes = test_working_capital(
        EXPECTED_SALES_VOLUME["sales_vol_infl_yes"],
        CAPITAL_REQUIREMENT_YES
    )
    working_capital_infl_no = test_working_capital(
        EXPECTED_SALES_VOLUME["sales_vol_infl_no"],
        CAPITAL_REQUIREMENT_NO
    )

    assert working_capital_yes == EXPECTED_WORKING_CAPITAL["working_capital_yes"]
    assert working_capital_no == EXPECTED_WORKING_CAPITAL["working_capital_no"]
    assert working_capital_infl_yes == EXPECTED_WORKING_CAPITAL["working_capital_infl_yes"]
    assert working_capital_infl_no == EXPECTED_WORKING_CAPITAL["working_capital_infl_no"]
