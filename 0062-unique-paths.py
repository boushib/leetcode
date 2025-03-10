from tests import run_tests


def unique_paths(m: int, n: int) -> int:
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]


# Time complexity: O(m * n)
# Space complexity: O(m * n)

tests = [
    ((3, 7), 28),
    ((3, 2), 3),
]
run_tests(unique_paths, tests)
