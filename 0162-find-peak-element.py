from typing import List
from tests import run_tests


def find_peak_element(nums: List[int]) -> int:
    lo, hi = 0, len(nums)

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            lo = mid + 1
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            hi = mid - 1
        else:
            return mid


# Time complexity: O(log(n))
# Space complexity: O(1)


tests = [([1, 2, 3, 1], 2), ([1, 2, 1, 3, 5, 6, 4], 5)]
run_tests(find_peak_element, tests)
