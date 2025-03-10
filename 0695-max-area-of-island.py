from typing import List
from tests import run_tests


def max_area_of_island(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
            return 0

        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

    return max([dfs(r, c) for r in range(rows) for c in range(cols)])


# Time complexity: O(m * n)
# Space complexity: O(m * n)


tests = [
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
]
run_tests(max_area_of_island, tests)
