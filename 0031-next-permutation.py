from typing import List
from tests import run_tests


def next_permutation(nums: List[int]) -> List[int]:
    pivot = len(nums) - 1

    while pivot > 0 and nums[pivot] < nums[pivot - 1]:
        pivot -= 1

    if pivot != 0:
        i = len(nums) - 1

        while nums[i] < nums[pivot - 1]:
            i -= 1

        nums[i], nums[pivot - 1] = nums[pivot - 1], nums[i]

    lo, hi = pivot, len(nums) - 1

    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

    return nums


# Time complexity: O(n)
# Space complexity: O(1)


tests = [
    ([1, 2, 3], [1, 3, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
    ([1, 2, 5, 7, 3], [1, 2, 7, 3, 5]),
    ([1, 2, 7, 5, 3], [1, 3, 2, 5, 7]),
]
run_tests(next_permutation, tests)
