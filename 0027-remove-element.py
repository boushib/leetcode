from typing import List
from tests import run_tests


def remove_element(nums: List[int], target: int) -> List[int]:
    lo = 0

    for i, n in enumerate(nums):
        if n != target:
            nums[lo] = nums[i]
            lo += 1

    return nums[:lo] + ["_"] * (len(nums) - lo)


# Time complexity: O(n)
# Space complexity: O(1)


tests = [(([3, 2, 2, 3], 3), [2, 2, "_", "_"]), (([0, 1, 2, 2, 3, 0, 4, 2], 2), [0, 1, 4, 0, 3, "_", "_", "_"])]
run_tests(remove_element, tests)
