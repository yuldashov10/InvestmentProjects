import pytest

from calculations.cash_flow_from_operations import CashFlowFromOperations
from tests.data import (
    EXPECTED_CFFO,
    EXPECTED_DEPRECIATION,
    EXPECTED_NET_PROFIT,
)


@pytest.mark.parametrize(
    "depreciation, net_profit_data, expected_key",
    [
        (
            EXPECTED_DEPRECIATION["depreciation_yes"],
            EXPECTED_NET_PROFIT["net_profit_yes"],
            "cffo_yes",
        ),
        (
            EXPECTED_DEPRECIATION["depreciation_no"],
            EXPECTED_NET_PROFIT["net_profit_no"],
            "cffo_no",
        ),
        (
            EXPECTED_DEPRECIATION["depreciation_yes"],
            EXPECTED_NET_PROFIT["net_profit_infl_yes"],
            "cffo_infl_yes",
        ),
        (
            EXPECTED_DEPRECIATION["depreciation_no"],
            EXPECTED_NET_PROFIT["net_profit_infl_no"],
            "cffo_infl_no",
        ),
    ],
)
def test_cash_flow_from_op(depreciation, net_profit_data, expected_key):
    cffo = CashFlowFromOperations(depreciation, net_profit_data)
    result = cffo.calc()
    expected = EXPECTED_CFFO[expected_key]
    assert result == expected, f"Ожидается {expected}, получено {result}"
