from typing import List
from tests import run_tests


def is_monotonic(nums: List[int]) -> bool:
    is_increasing, is_decreasing = False, False

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            is_increasing = True
        if nums[i] < nums[i - 1]:
            is_decreasing = True

        if is_increasing and is_decreasing:
            return False

    return True


# Time complexity: O(n)
# Space complexity: O(1)


tests = [([1, 2, 2, 3], True), ([6, 5, 4, 4], True), ([1, 3, 2], False)]
run_tests(is_monotonic, tests)
