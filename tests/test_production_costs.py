from calculations.index import Index


def test_production_costs(annual_sales,
                          production_costs_per_unit,
                          inflation=None):
    if inflation is not None:
        return Index.production_costs(
            annual_sales, production_costs_per_unit, inflation)
    return Index.production_costs(annual_sales, production_costs_per_unit)


if __name__ == "__main__":
    sales_yes = [49500, 54000, 58500, 63000, 63000, 63000, 63000, 63000]
    prod_costs_yes = [2250, 2295, 2340, 2385, 2430, 2475, 2520, 2565]

    sales_no = [45000, 44550, 44100, 43650, 43200, 42750, 42300, 41850]
    prod_costs_no = [2475, 2565, 2655, 2790, 2880, 2970, 3060, 3150]

    infl = 0.10

    prod_sales_yes_res = [
        111375000, 123930000, 136890000,
        150255000, 153090000, 155925000,
        158760000, 161595000
    ]

    prod_sales_infl_no_res = [
        122512500.0, 138267607.5, 155840800.5,
        178303222.35, 200373212.16, 224930671.27,
        252238043.99, 282583953.85
    ]

    msg_yes = "Index.production_costs без учета инфляции работает неправильно"
    msg_no = "Index.production_costs с учетом инфляции работает неправильно"

    print(test_production_costs(sales_yes, prod_costs_yes))
    print(test_production_costs(sales_no, prod_costs_no, infl))

    assert test_production_costs(sales_yes, prod_costs_yes) == prod_sales_yes_res, msg_yes
    assert test_production_costs(sales_no, prod_costs_no, infl) == prod_sales_infl_no_res, msg_no
