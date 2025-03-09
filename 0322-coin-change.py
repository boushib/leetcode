from typing import List
from tests import run_tests


def coin_change(coins: List[int], amount: int) -> int:
    dp = [0] + [float("inf")] * (amount)

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float("inf") else -1


tests = [(([1, 2, 5], 11), 3), (([2], 3), -1), (([1], 0), 0)]
run_tests(coin_change, tests)
