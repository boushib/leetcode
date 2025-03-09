from typing import List
from tests import run_tests


def max_area(heights: List[int]) -> int:
    lo, hi = 0, len(heights) - 1
    res = 0

    while lo < hi:
        res = max(res, (hi - lo) * min(heights[lo], heights[hi]))

        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1

    return res


# Time complexity: O(n)
# Space complexity: O(1)


tests = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
run_tests(max_area, tests)
