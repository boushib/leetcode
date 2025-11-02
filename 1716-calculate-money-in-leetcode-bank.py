from typing import List
from tests import run_tests

def total_money_linear(n: int) -> int:
    week = 0
    res = 0

    for d in range(n):
        res += d % 7 + 1 + week

        if d % 7 == 6:
            week += 1

    return res

def total_money(n: int) -> int:
    # week_sum(k) = (1 + k) + (2 + k) + (3 + k) + (4 + k) + (5 + k) + (6 + k) + (7 + k) = 28 + 7k 

    # split to full weeks + leftover days
    weeks = n // 7
    days = n % 7

    # full_week_total = sum(k=0...weeks-1) of 28 + 7k
    # which is an arithmetic serie = 28 * weeks + 7 (weeks - 1) * weeks / 2

    # leftover_days = sum(i=1...days) weeks + i = weeks * days + days * (days + 1) / 2

    # putting it all together
    # res = 28 * weeks + 7 * (weeks - 1) * weeks / 2 + weeks * days + days * (days + 1) / 2

    return 28 * weeks + 7 * (weeks - 1) * weeks / 2 + weeks * days + days * (days + 1) / 2


# Time complexity: O(1)
# Space complexity: O(1)


tests = [((4), 10), ((10), 37), ((20), 96), ((25), 127)]
run_tests(total_money, tests)