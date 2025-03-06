from typing import List
from tests import run_tests


def is_sorted_and_rotated(nums: List[int]) -> bool:
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1

        if count > 1:
            return False

    return True


# Time complexity: O(n)
# Space complexity: O(1)


tests = [([3, 4, 5, 1, 2], True), ([2, 1, 3, 4], False), ([1, 2, 3], True)]
run_tests(is_sorted_and_rotated, tests)
