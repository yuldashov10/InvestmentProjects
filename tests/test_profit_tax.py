from calculations.index import Index
from data import (
    EXPECTED_PROFIT_TAX,
    EXPECTED_TAXABLE_PROFIT,
    TAX_RATE
)


def test_profit_tax(taxable_profit_data, tax_rate):
    return Index.profit_tax(taxable_profit_data, tax_rate)


if __name__ == "__main__":
    profit_tax_yes = test_profit_tax(EXPECTED_TAXABLE_PROFIT["taxable_profit_yes"], TAX_RATE)
    profit_tax_no = test_profit_tax(EXPECTED_TAXABLE_PROFIT["taxable_profit_no"], TAX_RATE)
    profit_tax_infl_yes = test_profit_tax(EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_yes"], TAX_RATE)
    profit_tax_infl_no = test_profit_tax(EXPECTED_TAXABLE_PROFIT["taxable_profit_infl_no"], TAX_RATE)

    assert profit_tax_yes == EXPECTED_PROFIT_TAX["profit_tax_yes"]
    assert profit_tax_no == EXPECTED_PROFIT_TAX["profit_tax_no"]
    assert profit_tax_infl_yes == EXPECTED_PROFIT_TAX["profit_tax_infl_yes"]
    assert profit_tax_infl_no == EXPECTED_PROFIT_TAX["profit_tax_infl_no"]
   