from typing import List
from tests import run_tests


def subarray_sum(nums: List[int], k: int) -> int:
    res = 0
    cum_sum = 0
    prefix_sum = {0: 1}

    for n in nums:
        cum_sum += n
        res += prefix_sum.get(cum_sum - k, 0)
        prefix_sum[cum_sum] = prefix_sum.get(cum_sum, 0) + 1

    return res


# Time complexity: O(n)
# Space complexity: O(n)


tests = [(([1, -1, 1, 1, 1], 2), 4), (([1, 1, 1], 2), 2), (([1, 2, 3], 3), 2)]
run_tests(subarray_sum, tests)
