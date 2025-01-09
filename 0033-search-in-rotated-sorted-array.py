from typing import List
from tests import run_tests


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        # left part is not rotated
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:  # target exists in the left part
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


tests = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
]
run_tests(search_in_rotated_sorted_array, tests)
