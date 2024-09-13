from tests import run_tests


def is_power_of_two(n: int) -> bool:
    return n != 0 and n & (n - 1) == 0


tests = [(0, False), (1, True), (3, False), (16, True)]
run_tests(is_power_of_two, tests)
