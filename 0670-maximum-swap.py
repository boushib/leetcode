from tests import run_tests


def maximum_swap(n: int) -> int:
    digits = list(map(int, str(n)))
    last = {x: i for i, x in enumerate(digits)}

    for i, d in enumerate(digits):
        for e in range(9, d, -1):
            j = last.get(e, -1)
            if j > i:
                digits[i], digits[j] = digits[j], digits[i]
                return int("".join(map(str, digits)))

    return n


tests = [(2736, 7236), (9973, 9973)]
run_tests(maximum_swap, tests)
