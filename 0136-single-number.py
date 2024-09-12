from typing import List
from tests import run_tests


def single_number(nums: List[int]) -> int:
    pass


tests = [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)]
run_tests(single_number, tests)
