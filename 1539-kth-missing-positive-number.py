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
