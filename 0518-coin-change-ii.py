from typing import List
from tests import run_tests


def coin_change(amount: int, coins: List[int]) -> int:
    dp = [1] + [0] * amount

    for i in range(len(coins) - 1, -1, -1):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[amount]


# Time complexity: O(amount * len(coins))
# Space complexity: O(amount)


tests = [((5, [1, 2, 5]), 4), ((3, [2]), 0), ((10, [10]), 1)]
run_tests(coin_change, tests)
