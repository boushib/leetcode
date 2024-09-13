from typing import List
from tests import run_tests


def max_profit(prices: List[int]) -> int:
    res = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        res = max(res, price - min_price)

    return res


tests = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
run_tests(max_profit, tests)
