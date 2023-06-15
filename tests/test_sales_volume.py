from calculations.index import Index


def test_sales_volume(sales, unit_price, inflation=None):
    if inflation is not None:
        return Index.sales_volume(sales, unit_price, inflation)
    return Index.sales_volume(sales, unit_price)


if __name__ == "__main__":
    sales_yes = [49500, 54000, 58500, 63000, 63000, 63000, 63000, 63000]
    sales_no = [45000, 44550, 44100, 43650, 43200, 42750, 42300, 41850]
    price = 2740.00
    infl = 0.10

    sales_infl_yes_res = [
        149193000.0, 179031600.0, 213345990.0,
        252732942.0, 278006236.2, 305806859.82,
        336387545.8, 370026300.38
    ]

    sales_no_res = [
        135630000.0, 147960000.0, 160290000.0,
        172620000.0, 172620000.0, 172620000.0,
        172620000.0, 172620000.0
    ]

    msg_yes = "Index.sales_volume с учетом инфляции работает неправильно"
    msg_no = "Index.sales_volume без учета инфляции работает неправильно"
    assert test_sales_volume(sales_yes, price, infl) == sales_infl_yes_res, msg_yes

    assert test_sales_volume(sales_yes, price) == sales_no_res, msg_no
