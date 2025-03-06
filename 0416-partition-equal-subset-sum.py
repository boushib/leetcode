from typing import List
from tests import run_tests


def can_partition(nums: List[int]) -> bool:
    if sum(nums) % 2 == 1:
        return False

    target = sum(nums) // 2
    dp = set([0])

    for n in nums:
        # Should not change set size during iteration
        next_dp = dp.copy()

        for m in dp:
            next_dp.add(n + m)

        dp = next_dp
    return target in dp


# Time complexity: O(n * sum(nums))
# Space complexity: O(sum(nums))


tests = [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)]
run_tests(can_partition, tests)
