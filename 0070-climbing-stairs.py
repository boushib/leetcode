from tests import run_tests


def climb_stairs_n_space(n: int) -> int:
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs(n: int) -> int:
    x, y = 1, 1

    for i in range(2, n + 1):
        n_ways = x + y
        x, y = y, n_ways

    return y


tests = [
    (2, 2),
    (6, 13),
    (12, 233),
    (20, 10946),
]
run_tests(climb_stairs, tests)
