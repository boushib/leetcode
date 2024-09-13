from typing import List
from tests import run_tests


def height_checker(heights: List[int]) -> int:
    sorted_heights = sorted(heights)
    res = 0

    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            res += 1

    return res


tests = [([1, 1, 4, 2, 1, 3], 3), ([5, 1, 2, 3, 4], 5), ([1, 2, 3, 4, 5], 0)]
run_tests(height_checker, tests)
