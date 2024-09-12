from tests import run_tests


def number_of_islands(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
            return None

        grid[i][j] = "0"

        for di, dj in directions:
            dfs(i + di, j + dj)

    res = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)

    return res


tests = [([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
           ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 1),
         ([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
           ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]], 3)]
run_tests(number_of_islands, tests)
