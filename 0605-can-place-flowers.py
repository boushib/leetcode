from typing import List
from tests import run_tests


def can_place_flowers(flowerbed: List[int], n) -> bool:
    if n == 0:
        return True

    planted = 0

    for i in range(len(flowerbed)):
        if (
            flowerbed[i] == 0
            and (i == 0 or flowerbed[i - 1] == 0)
            and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):
            planted += 1
            flowerbed[i] = 1

        if planted == n:
            return True

    return False


# Time complexity: O(n)
# Space complexity: O(1)


tests = [(([1, 0, 0, 0, 1], 1), True), (([1, 0, 0, 0, 1], 2), False)]
run_tests(can_place_flowers, tests)
