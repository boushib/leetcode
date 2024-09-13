from math import sqrt
from tests import run_tests


def bulb_switch(n: int) -> int:
    return int(sqrt(n))


tests = [(3, 1), (0, 0), (1, 1)]
run_tests(bulb_switch, tests)
