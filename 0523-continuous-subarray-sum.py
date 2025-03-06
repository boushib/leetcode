from typing import List
from tests import run_tests


def check_subarray_sum(nums: List[int], k: int) -> bool:
    cum_sum = 0
    remainder_map = {0: -1}

    for i, n in enumerate(nums):
        cum_sum += n
        remainder = cum_sum % k

        if remainder in remainder_map and i - remainder_map[remainder] >= 2:
            return True
        if remainder not in remainder_map:
            remainder_map[remainder] = i

    return False


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    (([23, 2, 4, 6, 7], 6), True),
    (([23, 2, 6, 4, 7], 6), True),
    (([23, 2, 6, 4, 7], 13), False),
    (([5, 0, 0, 0], 3), True),
]
run_tests(check_subarray_sum, tests)
