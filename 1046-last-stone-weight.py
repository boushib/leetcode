from typing import List
from heapq import heapify, heappush, heappop
from tests import run_tests


def last_stone_weight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapify(stones)

    while len(stones) >= 2:
        a = -heappop(stones)
        b = -heappop(stones)

        if a > b:
            heappush(stones, b - a)

    return -stones[0] if stones else 0


# Time complexity: O(n * log(n))
# Space complexity: O(1)


tests = [([2, 7, 4, 1, 8, 1], 1), ([1], 1)]
run_tests(last_stone_weight, tests)
