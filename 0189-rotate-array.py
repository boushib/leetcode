from typing import List
from tests import run_tests


def rotate_array(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    k %= n

    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return nums


# Time complexity: O(n)
# Space complexity: O(1)


tests = [(([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]), (([-1, -100, 3, 99], 2), [3, 99, -1, -100])]
run_tests(rotate_array, tests)
