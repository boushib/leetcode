from typing import List
from tests import run_tests


def depth_sum(nested_list: List[int]) -> int:
    res = 0

    def dfs(items, depth):
        for item in items:
            if isinstance(item, int):
                res[0] += item * depth
            else:
                dfs(item, depth + 1)

    dfs(nested_list, 1)
    return 0


tests = [([[1, 1], 2, [1, 1]], 10), ([1, [4, [6]]], 27), ([0], 0)]
run_tests(depth_sum, tests)
