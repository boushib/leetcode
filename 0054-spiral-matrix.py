from typing import List
from tests import run_tests


def traverse_in_spiral_order(nums: List[List[int]]) -> List[int]:
    res = []
    top, left = 0, 0
    bottom, right = len(nums) - 1, len(nums[0]) - 1

    while top <= bottom and left <= right:
        # left to right
        for i in range(left, right + 1):
            res.append(nums[top][i])
        top += 1

        # top to bottom
        for i in range(top, bottom + 1):
            res.append(nums[i][right])
        right -= 1

        # right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(nums[bottom][i])
            bottom -= 1

        # bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(nums[i][left])
            left += 1

    return res


# Time complexity: O(m * n)
# Space complexity: O(1)


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
]
run_tests(traverse_in_spiral_order, tests)
