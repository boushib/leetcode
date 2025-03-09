from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop
from tests import run_tests


def solve_sudoku(board: List[List[str]]) -> List[List[str]]:
    rows = defaultdict(set)
    cols = defaultdict(set)
    sub_boxes = defaultdict(set)
    empty_cells = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                empty_cells.append((r, c))
            else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_boxes[(r // 3, c // 3)].add(board[r][c])
    # (# of possible valid nums, r, c)
    empty_cells = [(9 - len(rows[r] | cols[c] | sub_boxes[(r // 3, c // 3)]), r, c) for r, c in empty_cells]
    heapify(empty_cells)

    def backtrack():
        if not empty_cells:  # board is complete
            return True

        _, r, c = heappop(empty_cells)
        valid_candidate_count = 0

        for n in "123456789":
            if n in rows[r] or n in cols[c] or n in sub_boxes[(r // 3, c // 3)]:
                continue

            board[r][c] = n
            rows[r].add(n)
            cols[c].add(n)
            sub_boxes[((r // 3, c // 3))].add(n)

            # Try to fill rest of the board
            if backtrack():
                return True

            rows[r].remove(n)
            cols[c].remove(n)
            sub_boxes[((r // 3, c // 3))].remove(n)
            valid_candidate_count += 1
        heappush(empty_cells, (valid_candidate_count, r, c))
        return False

    backtrack()
    return board


# Time complexity: O(9^81) -> O(1)
# Space complexity: O(81) -> O(1)


tests = [
    (
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ],
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "9", ".", ".", "1", ".", ".", "3", "."],
            [".", ".", "6", ".", "2", ".", "7", ".", "."],
            [".", ".", ".", "3", ".", "4", ".", ".", "."],
            ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "2", "5", ".", "6", "4", ".", "."],
            [".", "8", ".", ".", ".", ".", ".", "1", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ],
        [
            ["7", "2", "1", "8", "5", "3", "9", "4", "6"],
            ["4", "9", "5", "6", "1", "7", "8", "3", "2"],
            ["8", "3", "6", "4", "2", "9", "7", "5", "1"],
            ["9", "6", "7", "3", "8", "4", "1", "2", "5"],
            ["2", "1", "4", "7", "6", "5", "3", "9", "8"],
            ["3", "5", "8", "2", "9", "1", "6", "7", "4"],
            ["1", "7", "2", "5", "3", "6", "4", "8", "9"],
            ["6", "8", "3", "9", "4", "2", "5", "1", "7"],
            ["5", "4", "9", "1", "7", "8", "2", "6", "3"],
        ],
    ),
]
run_tests(solve_sudoku, tests)
