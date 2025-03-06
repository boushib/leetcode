from typing import List
from tests import run_tests


def search_range(nums: List[int], target: int) -> List[int]:
    def search(target: int, is_first: bool):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if is_first:
                    if mid == lo or nums[mid - 1] != target:
                        return mid
                    else:
                        hi = mid - 1
                else:
                    if mid == hi or nums[mid + 1] != target:
                        return mid
                    else:
                        lo = mid + 1

        return -1

    first = search(target, True)

    if first == -1:
        return [-1, -1]

    last = search(target, False)

    return [first, last]


# Time complexity: O(log(n))
# Space complexity: O(1)


tests = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 0), [-1, -1]),
]
run_tests(search_range, tests)
