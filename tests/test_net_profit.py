from calculations.index import Index
from data import (
    EXPECTED_NET_PROFIT,
    EXPECTED_PROFIT_TAX,
    EXPECTED_TAXABLE_PROFIT
)


def test_net_profit(taxable_profit_data, profit_tax_data):
    return Index.net_profit(taxable_profit_data, profit_tax_data)


if __name__ == "__main__":
    net_profit_yes = test_net_profit(
        EXPECTED_TAXABLE_PROFIT["taxable_profit_yes"],
        EXPECTED_PROFIT_TAX["profit_tax_yes"]
    )
    net_profit_no = test_net_profit(
        EXPECTED_TAXABLE_PROFIT["taxable_profit_no"],
        EXPECTED_PROFIT_TAX["profit_tax_no"]
    )
    net_profit_infl_yes = test_net_profit(
        EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_yes"],
        EXPECTED_PROFIT_TAX["profit_tax_infl_yes"]
    )
    net_profit_infl_no = test_net_profit(
        EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_no"],
        EXPECTED_PROFIT_TAX["profit_tax_infl_no"]
    )

    assert net_profit_yes == EXPECTED_NET_PROFIT["net_profit_yes"]
    assert net_profit_no == EXPECTED_NET_PROFIT["net_profit_no"]
    assert net_profit_infl_yes == EXPECTED_NET_PROFIT["net_profit_infl_yes"]
    assert net_profit_infl_no == EXPECTED_NET_PROFIT["net_profit_infl_no"]
