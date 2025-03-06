from typing import List
from tests import run_tests


def find_max_length(nums: List[int]) -> int:
    res = 0
    count = 0
    count_map = {0: -1}

    for i, n in enumerate(nums):
        count += 1 if n == 1 else -1

        if count in count_map:
            res = max(res, i - count_map[count])
        else:
            count_map[count] = i

    return res


# Time complexity: O(n)
# Space complexity: O(n)


tests = [([0, 1], 2), ([0, 1, 0], 2)]
run_tests(find_max_length, tests)
