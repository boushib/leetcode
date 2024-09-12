from typing import List
from tests import run_tests


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(subset, index):
        res.append(subset[:])

        for i in range(index, len(nums)):
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()

    backtrack([], 0)
    return res


tests = [([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
         ([0], [[], [0]])]
run_tests(subsets, tests)
