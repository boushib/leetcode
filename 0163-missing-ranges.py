from typing import List
from tests import run_tests


def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    res = []
    left = lower

    for n in nums:
        if n > left:
            res.append([left, n - 1])
        left = n + 1

    if upper >= left:
        res.append([left, upper])

    return res


# Time complexity: O(n)
# Space complexity: O(1)


tests = [(([0, 1, 3, 50, 75], 0, 99), [[2, 2], [4, 49], [51, 74], [76, 99]]), (([-1], -1, -1), [])]
run_tests(find_missing_ranges, tests)
