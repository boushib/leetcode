from typing import List
from tests import run_tests


def largest_island(grid: List[List[int]]) -> int:
    n = len(grid)
    current_island_id = 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    island_size_map = {}

    def dfs(r, c, island_id):
        if min(r, c) < 0 or max(r, c) >= n or grid[r][c] != 1:
            return 0

        island_size = 1
        grid[r][c] = island_id

        for dr, dc in directions:
            island_size += dfs(r + dr, c + dc, island_id)

        return island_size

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                island_size_map[current_island_id] = dfs(
                    r, c, current_island_id)
                current_island_id += 1

    res = max(island_size_map.values(), default=0)

    for r in range(n):
        for c in range(n):
            if grid[r][c] != 0:
                continue

            visited = set()
            merged_island_size = 1

            for dr, dc in directions:
                i, j = r + dr, c + dc

                if 0 <= i < n and 0 <= j < n and grid[i][j] >= 2:
                    island_id = grid[i][j]
                    if island_id not in visited:
                        merged_island_size += island_size_map[island_id]
                        visited.add(island_id)

            res = max(res, merged_island_size)

    return res


tests = [([[1, 0], [0, 1]], 3), ([[1, 1], [1, 0]], 4), ([[1, 1], [1, 1]], 4),
         ([[0, 0], [0, 0]], 1), ([[0, 0], [0, 1]], 2)]
run_tests(largest_island, tests)
