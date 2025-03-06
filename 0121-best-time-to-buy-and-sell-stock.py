from typing import List
from tests import run_tests


def max_profit(prices: List[int]) -> int:
    res = 0
    min_price_so_far = prices[0]

    for price in prices:
        res = max(res, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)

    return res


tests = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
run_tests(max_profit, tests)
