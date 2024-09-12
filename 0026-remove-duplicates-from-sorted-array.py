from typing import List
from tests import run_tests


def remove_duplicates(nums: List[int]) -> int:
    i, j = 1, 1

    while j < len(nums):
        if nums[j] != nums[j - 1]:
            nums[i] = nums[j]
            i += 1
        j += 1

    while i < len(nums):
        nums[i] = "_"
        i += 1

    return nums


tests = [([1, 1, 2], [1, 2, "_"]),
         ([0, 0, 1, 1, 1, 2, 2, 3, 3,
           4], [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]), ([], [])]
run_tests(remove_duplicates, tests)
