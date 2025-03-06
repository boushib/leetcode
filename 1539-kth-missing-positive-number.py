from typing import List
from tests import run_tests


def find_kth_positive(nums: List[int], k: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        missing_count_at_mid = nums[mid] - mid - 1

        if missing_count_at_mid < k:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo + k


tests = [(([2, 3, 4, 7, 11], 5), 9), (([1, 2, 3, 4], 2), 6)]
run_tests(find_kth_positive, tests)
"""
nums[hi] + k      -> Potential value of the kth missing number if there were no missing numbers between nums[hi] and nums[lo].
nums[hi] - hi - 1 -> number of positive integers that are missing before nums[hi].
Actual value of the kth missing number.
nums[hi] + k - (nums[hi] - hi - 1) = k + hi + 1
"""
