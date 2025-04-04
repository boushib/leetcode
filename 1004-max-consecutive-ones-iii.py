from typing import List
from tests import run_tests


def max_consecutive_ones(nums: List[int], k: int) -> int:
    res = 0
    lo = 0
    zero_count = 0

    for hi in range(len(nums)):
        if nums[hi] == 0:
            zero_count += 1

        if zero_count > k:
            if nums[lo] == 0:
                zero_count -= 1
            lo += 1

        res = max(res, hi - lo + 1)

    return res


# Time complexity: O(n)
# Space complexity: O(1)


tests = [
    (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
    (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10),
]
run_tests(max_consecutive_ones, tests)
