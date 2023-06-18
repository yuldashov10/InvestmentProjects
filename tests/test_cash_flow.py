from calculations.index import Index
from data import (
    EXPECTED_CAPITAL_INVEST,
    EXPECTED_CASH_FLOW,
    EXPECTED_DEPRECIATION,
    EXPECTED_NET_PROFIT,
    EXPECTED_WC_GAIN
)


def test_cash_flow(depreciation, net_profit_data,
                   working_capital_gain_data, capital_investments_data,
                   inflation=False):
    return Index.cash_flow(
        depreciation,
        net_profit_data,
        working_capital_gain_data,
        capital_investments_data,
        inflation
    )


if __name__ == "__main__":
    cf_yes = test_cash_flow(
        EXPECTED_DEPRECIATION["depreciation_yes"],
        EXPECTED_NET_PROFIT["net_profit_yes"],
        EXPECTED_WC_GAIN["wc_gain_yes"],
        EXPECTED_CAPITAL_INVEST["capital_invest_yes"]
    )
    cf_no = test_cash_flow(
        EXPECTED_DEPRECIATION["depreciation_no"],
        EXPECTED_NET_PROFIT["net_profit_no"],
        EXPECTED_WC_GAIN["wc_gain_no"],
        EXPECTED_CAPITAL_INVEST["capital_invest_no"],
    )
    cf_infl_yes = test_cash_flow(
        EXPECTED_DEPRECIATION["depreciation_yes"],
        EXPECTED_NET_PROFIT["net_profit_infl_yes"],
        EXPECTED_WC_GAIN["wc_gain_infl_yes"],
        EXPECTED_CAPITAL_INVEST["capital_invest_infl_yes"],
        inflation=True
    )
    cf_infl_no = test_cash_flow(
        EXPECTED_DEPRECIATION["depreciation_no"],
        EXPECTED_NET_PROFIT["net_profit_infl_no"],
        EXPECTED_WC_GAIN["wc_gain_infl_no"],
        EXPECTED_CAPITAL_INVEST["capital_invest_infl_no"],
        inflation=True
    )

    assert cf_yes == EXPECTED_CASH_FLOW["cf_yes"]
    assert cf_no == EXPECTED_CASH_FLOW["cf_no"]
    assert cf_infl_yes == EXPECTED_CASH_FLOW["cf_infl_yes"]
    assert cf_infl_no == EXPECTED_CASH_FLOW["cf_infl_no"]
