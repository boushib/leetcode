from typing import List
from tests import run_tests


def find_diagonal_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    res = []
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, 0
    is_moving_up_right = True

    while r < rows and c < cols:
        res.append(matrix[r][c])
        next_row = r - 1 if is_moving_up_right else r + 1
        next_col = c + 1 if is_moving_up_right else c - 1

        # we're still within bounds
        if 0 <= next_row < rows and 0 <= next_col < cols:
            r, c = next_row, next_col
            continue

        if is_moving_up_right:
            # r == 0 -> cannot go to r -1 -> increment col &
            # switch dirfection bottom-left if possible
            if c < cols - 1:
                c += 1
            else:  # we're at top-right where c == cols - 1 -> move to next row
                r += 1
        else:
            if r < rows - 1:  # col == 0 -> wd cannot move to col -1 -> increment r &
                # switch direction up-right if possible
                r += 1
            else:
                c += 1

        is_moving_up_right = not is_moving_up_right

    return res


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
]
run_tests(find_diagonal_order, tests)
