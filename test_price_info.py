import price_info

def test_total_cost():
    cost = 46.75
    result = price_info.total_cost_shopping()
    assert (result == cost)

def test_cost_of_fruit():
    cost = 12
    result = price_info.cost_of_fruits('apple',10)
    assert (result == cost)