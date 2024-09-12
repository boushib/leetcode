from typing import List
from tests import run_tests


def two_sum(nums: List[int], target: int) -> List[int]:
    comp = {}

    for i, n in enumerate(nums):
        if target - n in comp:
            return [comp[target - n], i]

        comp[n] = i

    return []


tests = [(([2, 7, 11, 15], 9), [0, 1]), (([3, 2, 4], 6), [1, 2]),
         (([3, 3], 6), [0, 1])]
run_tests(two_sum, tests)
