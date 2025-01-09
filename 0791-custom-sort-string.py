from tests import run_tests


def custom_sort_string(order: str, s: str) -> str:
    res = []
    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in order:
        if c in count:
            res.append(c * count.get(c))

    for c in s:
        if c not in order:
            res.append(c * count[c])

    return "".join(res)


tests = [
    (("cba", "abcd"), "cbad"),
    (("bcafg", "abcd"), "bcad"),
]
run_tests(custom_sort_string, tests)
