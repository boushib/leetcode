from typing import List
from tests import run_tests


def plus_one(digits: List[int]) -> List[int]:
    digits = digits[::-1]
    carry = 1

    for i, d in enumerate(digits):
        n = d + carry
        digits[i] = n % 10
        carry = n // 10

    if carry:
        digits.append(carry)

    return digits[::-1]


tests = [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0])]
run_tests(plus_one, tests)
