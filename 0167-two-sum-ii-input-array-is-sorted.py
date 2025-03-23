from typing import List
from tests import run_tests


def two_sum(nums: List[int], target: int) -> List[int]:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        if nums[lo] + nums[hi] == target:
            return [lo + 1, hi + 1]

        if nums[lo] + nums[hi] < target:
            lo += 1
        else:
            hi -= 1

    return []


# Time complexity: O(n)
# Space complexity: O(1)


tests = [(([2, 7, 11, 15], 9), [1, 2]), (([2, 3, 4], 6), [1, 3]), (([3, 3], 6), [1, 2]), (([-1, 0], -1), [1, 2])]
run_tests(two_sum, tests)
