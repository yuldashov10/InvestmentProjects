from calculations.index import Index
from data import (
    EXPECTED_WC_GAIN,
    EXPECTED_WORKING_CAPITAL
)


def test_working_capital_gain(working_capital_data):
    return Index.working_capital_gain(working_capital_data)


if __name__ == "__main__":
    wc_gain_yes = test_working_capital_gain(
        EXPECTED_WORKING_CAPITAL["working_capital_yes"]
    )
    wc_gain_no = test_working_capital_gain(
        EXPECTED_WORKING_CAPITAL["working_capital_no"]
    )
    wc_gain_infl_yes = test_working_capital_gain(
        EXPECTED_WORKING_CAPITAL["working_capital_infl_yes"]
    )
    wc_gain_infl_no = test_working_capital_gain(
        EXPECTED_WORKING_CAPITAL["working_capital_infl_no"]
    )

    assert wc_gain_yes == EXPECTED_WC_GAIN["wc_gain_yes"]
    assert wc_gain_no == EXPECTED_WC_GAIN["wc_gain_no"]
    assert wc_gain_infl_yes == EXPECTED_WC_GAIN["wc_gain_infl_yes"]
    assert wc_gain_infl_no == EXPECTED_WC_GAIN["wc_gain_infl_no"]
