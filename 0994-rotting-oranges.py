from typing import List
from collections import deque
from tests import run_tests


def rotting_oranges(grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return -1

    fresh_orange_count = 0
    res = 0  # minutes elapses
    queue = deque()
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_orange_count += 1
            if grid[r][c] == 2:
                queue.append((r, c, 0))

    while queue:
        r, c, mins = queue.popleft()
        res = max(res, mins)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_orange_count -= 1
                queue.append((nr, nc, mins + 1))

    return res if fresh_orange_count == 0 else -1


tests = [([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4), ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1), ([[0, 2]], 0)]
run_tests(rotting_oranges, tests)
