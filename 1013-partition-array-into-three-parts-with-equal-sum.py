from typing import List
from tests import run_tests


def can_three_part_eq_sum(nums: List[int]) -> bool:
    s = sum(nums)
    n = len(nums)

    if s % 3 != 0:
        return False

    target_sum = s // 3
    left_sum, right_sum = nums[0], nums[n - 1]
    lo, hi = 1, n - 2

    while lo < hi:
        if lo < hi and left_sum != target_sum:
            left_sum += nums[lo]
            lo += 1
        if lo < hi and right_sum != target_sum:
            right_sum += nums[hi]
            hi -= 1

        if left_sum == right_sum == target_sum:
            return True

    return False


# Time complexity: O(n)
# Space complexity: O(1)


tests = [
    ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
    ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
    ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
    ([1, 1, 1, 1], False),
    ([1, -1, 1, -1], False),
]
run_tests(can_three_part_eq_sum, tests)
