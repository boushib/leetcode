from typing import List
from tests import run_tests


def add_ops(s: str, target: int) -> List[str]:
    res = []

    def dfs(path, pos, curr_sum, prev):
        if pos == len(s):
            if curr_sum == target:
                res.append(path)
            return

        for i in range(pos, len(s)):
            n = int(s[pos : i + 1])

            if not path:
                dfs(str(n), i + 1, n, n)
            else:
                dfs(path + "+" + str(n), i + 1, curr_sum + n, n)
                dfs(path + "-" + str(n), i + 1, curr_sum - n, -n)
                dfs(path + "*" + str(n), i + 1, curr_sum - prev + n * prev, n * prev)

            if s[pos] == "0":
                break

    dfs("", 0, 0, 0)
    return res


tests = [
    (("123", 6), ["1*2*3", "1+2+3"]),
    (("232", 8), ["2*3+2", "2+3*2"]),
    (("3456237490", 9191), []),
]
run_tests(add_ops, tests)
