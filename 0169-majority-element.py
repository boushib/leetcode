from typing import List
from tests import run_tests


def majority_element(nums: List[int]) -> int:
    count, candidate = 0, nums[0]

    for n in nums:
        if count == 0:
            candidate = n

        count += 1 if n == candidate else -1

    return candidate


# Time complexity: O(n)
# Space complexity: O(1)


tests = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
run_tests(majority_element, tests)
