from typing import List
from collections import deque
from tests import run_tests


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    n = len(grid)

    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1

    while queue:
        x, y, path_length = queue.popleft()

        if x == y == n - 1:
            return path_length

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                queue.append((nx, ny, path_length + 1))
                grid[nx][ny] = 1

    return -1


tests = [([[0, 1], [1, 0]], 2), ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4), ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1)]
run_tests(shortest_path_binary_matrix, tests)
