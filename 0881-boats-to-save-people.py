from typing import List
from tests import run_tests


def num_of_rescue_boats(people: List[int], limit: int) -> int:
    res = 0
    people.sort()
    lo, hi = 0, len(people) - 1

    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
        hi -= 1
        res += 1

    return res


# Time complexity: O(n * log(n))
# Space complexity: O(log(n))


tests = [
    (([1, 2], 3), 1),
    (([3, 2, 2, 1], 3), 3),
    (([3, 5, 3, 4], 5), 4),
]
run_tests(num_of_rescue_boats, tests)
