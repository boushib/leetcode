from typing import List
from tests import run_tests


def even_odd_bit(n: int) -> List[int]:
    res = [0, 0]

    for i, c in enumerate(bin(n)[2:][::-1]):
        if c == "1" and i % 2 == 0:
            res[0] += 1
        if c == "1" and i % 2 == 1:
            res[1] += 1

    return res


# Time complexity: O(log(n))
# Space complexity: O(1)


tests = [(50, [1, 2]), (2, [0, 1])]
run_tests(even_odd_bit, tests)
