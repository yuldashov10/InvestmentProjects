from calculations.index import Index
from data import (
    EXPECTED_CFFO,
    EXPECTED_DEPRECIATION,
    EXPECTED_NET_PROFIT
)


def test_cash_flow_from_op(depreciation, net_profit_data):
    return Index.cash_flow_from_op(depreciation, net_profit_data)


if __name__ == "__main__":
    cffo_yes = test_cash_flow_from_op(
        EXPECTED_DEPRECIATION["depreciation_yes"],
        EXPECTED_NET_PROFIT["net_profit_yes"]
    )
    cffo_no = test_cash_flow_from_op(
        EXPECTED_DEPRECIATION["depreciation_no"],
        EXPECTED_NET_PROFIT["net_profit_no"]
    )
    cffo_infl_yes = test_cash_flow_from_op(
        EXPECTED_DEPRECIATION["depreciation_yes"],
        EXPECTED_NET_PROFIT["net_profit_infl_yes"]
    )
    cffo_infl_no = test_cash_flow_from_op(
        EXPECTED_DEPRECIATION["depreciation_no"],
        EXPECTED_NET_PROFIT["net_profit_infl_no"]
    )

    assert cffo_yes == EXPECTED_CFFO["cffo_yes"]
    assert cffo_no == EXPECTED_CFFO["cffo_no"]
    assert cffo_infl_yes == EXPECTED_CFFO["cffo_infl_yes"]
    assert cffo_infl_no == EXPECTED_CFFO["cffo_infl_no"]
