from typing import List
from tests import run_tests


def ocean_view(heights: List[int]) -> List[int]:
    res = []
    curr_max = float("-inf")

    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > curr_max:
            res.append(i)
            curr_max = heights[i]

    return res[::-1]


tests = [([4, 2, 3, 1], [0, 2, 3]), ([4, 3, 2, 1], [0, 1, 2, 3])]
run_tests(ocean_view, tests)
