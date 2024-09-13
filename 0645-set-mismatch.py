from typing import List
from tests import run_tests


def find_set_mismatch(nums: List[int]) -> List[int]:
    missing, dup = -1, -1

    for n in nums:
        if nums[abs(n) - 1] < 0:
            dup = abs(n)
        else:
            nums[abs(n) - 1] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1

    return [dup, missing]


tests = [([1, 2, 2, 4], [2, 3]), ([1, 1], [1, 2])]
run_tests(find_set_mismatch, tests)
