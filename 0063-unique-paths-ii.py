from typing import List
from tests import run_tests


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    pass


# Time complexity: O(m * n)
# Space complexity: O(m * n)

tests = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
    ([[0, 1], [0, 0]], 1),
]
run_tests(unique_paths_with_obstacles, tests)
