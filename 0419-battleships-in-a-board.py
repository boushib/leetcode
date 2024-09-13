from typing import List
from tests import run_tests


def count_battleships(board: List[List[str]]) -> int:
    res = 0
    rows, cols = len(board), len(board[0])

    def is_part_of_battleship(i, j):
        return i >= 0 and j >= 0 and board[i][j] == "X"

    for i in range(rows):
        for j in range(cols):
            if (
                is_part_of_battleship(i, j)
                and not is_part_of_battleship(i - 1, j)
                and not is_part_of_battleship(i, j - 1)
            ):
                res += 1

    return res


tests = [([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]], 2), ([["."]], 0)]
run_tests(count_battleships, tests)
