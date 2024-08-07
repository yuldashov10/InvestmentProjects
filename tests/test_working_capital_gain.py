import pytest

from calculations.working_capital_gain import WorkingCapitalGain
from tests.data import EXPECTED_WC_GAIN, EXPECTED_WORKING_CAPITAL


@pytest.mark.parametrize(
    "working_capital_data, expected_key",
    [
        (
            EXPECTED_WORKING_CAPITAL["working_capital_yes"],
            "wc_gain_yes",
        ),
        (
            EXPECTED_WORKING_CAPITAL["working_capital_no"],
            "wc_gain_no",
        ),
        (
            EXPECTED_WORKING_CAPITAL["working_capital_infl_yes"],
            "wc_gain_infl_yes",
        ),
        (
            EXPECTED_WORKING_CAPITAL["working_capital_infl_no"],
            "wc_gain_infl_no",
        ),
    ],
)
def test_working_capital_gain(working_capital_data, expected_key):
    wcg = WorkingCapitalGain(working_capital_data)
    result = wcg.calc()
    expected = EXPECTED_WC_GAIN[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
