from typing import List
from tests import run_tests


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    num_set = set()

    for i, n in enumerate(nums):
        if n in num_set:
            return True

        num_set.add(n)

        if len(num_set) > k:
            num_set.remove(nums[i - k])

    return False


# Time complexity: O(n)
# Space complexity: O(k)


tests = [(([1, 2, 3, 1], 3), True), (([1, 0, 1, 1], 1), True), (([1, 2, 3, 1, 2, 3], 2), False)]
run_tests(contains_nearby_duplicate, tests)
