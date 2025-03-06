from tests import run_tests


def climb_stairs_n_space(n: int) -> int:
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs(n: int) -> int:
    a, b = 2, 1

    for i in range(3, n + 1):
        c = a + b
        a, b = c, a

    return a if n > 1 else 1


tests = [(2, 2), (6, 13), (12, 233), (20, 10946)]
run_tests(climb_stairs, tests)
