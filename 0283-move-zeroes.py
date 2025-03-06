from typing import List
from tests import run_tests


def move_zeroes(nums: List[int]) -> List[int]:
    lo, hi = 0, 0

    while hi < len(nums):
        if nums[hi] != 0:
            nums[hi], nums[lo] = nums[lo], nums[hi]
            lo += 1

        hi += 1

    return nums


# Time complexity: O(n)
# Space complexity: O(1)


tests = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0])]
run_tests(move_zeroes, tests)
