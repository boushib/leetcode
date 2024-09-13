from typing import List
from tests import run_tests


def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    for r in range(rows - 1):
        for c in range(cols - 1):
            if matrix[r][c] != matrix[r + 1][c + 1]:
                return False

    return True


tests = [([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True), ([[1, 2], [2, 2]], False)]
run_tests(is_toeplitz_matrix, tests)
