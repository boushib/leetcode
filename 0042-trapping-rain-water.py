from typing import List
from tests import run_tests


def trapping_water(heights: List[int]) -> int:
    n = len(heights)
    max_left = [0] * n
    max_right = [0] * n
    max_left[0] = heights[0]
    max_right[-1] = heights[-1]

    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i])
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i])

    res = 0

    for i in range(n):
        res += max(0, min(max_left[i], max_right[i]) - heights[i])

    return res


tests = [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 0, 3, 2, 5], 9)]
run_tests(trapping_water, tests)
