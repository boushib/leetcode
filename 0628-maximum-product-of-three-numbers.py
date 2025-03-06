from typing import List
from tests import run_tests


def max_product(nums: List[int]) -> int:
    min1 = min2 = float("inf")
    max1 = max2 = max3 = float("-inf")

    for n in nums:
        if n <= min1:  # n < min1 < min2
            min2 = min1
            min1 = n
        elif n <= min2:  # min1 < n < min2
            min2 = n

        if n >= max3:  # max2 <= max2 <= max3 <= n
            max1 = max2
            max2 = max3
            max3 = n
        elif n >= max2:  # max1 <= max2 <= n <= max3
            max1 = max2
            max2 = n
        elif n >= max1:  # max1 <= n <= max2 <= max3
            max1 = n

    return max(max1 * max2 * max3, min1 * min2 * max3)


tests = [([1, 2, 3], 6), ([1, 2, 3, 4], 24), ([-1, -2, -3], -6)]
run_tests(max_product, tests)
