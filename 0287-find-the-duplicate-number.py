from typing import List
from tests import run_tests


def find_duplicate_number(nums: List[int]) -> int:
    # Floyd's Tortoise and Hare (Cycle Detection)
    slow_ptr, fast_ptr = 0, 0

    while True:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[nums[fast_ptr]]

        if slow_ptr == fast_ptr:
            break

    slow_ptr2 = 0

    while True:
        slow_ptr = nums[slow_ptr]
        slow_ptr2 = nums[slow_ptr2]

        if slow_ptr == slow_ptr2:
            return slow_ptr2


tests = [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 3, 3, 3, 3], 3),
]
run_tests(find_duplicate_number, tests)
