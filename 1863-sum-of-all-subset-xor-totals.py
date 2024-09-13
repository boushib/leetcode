from typing import List
from tests import run_tests


def subset_xor_sum(nums: List[int]) -> int:
    n = len(nums)
    res = 0

    for subset_mask in range(1 << n):
        subset_xor = 0

        for i in range(n):
            if subset_mask & (1 << i):
                subset_xor ^= nums[i]

        res += subset_xor

    return res


tests = [([1, 3], 6), ([5, 1, 6], 28)]
run_tests(subset_xor_sum, tests)
