from typing import List
from tests import run_tests


def can_attend_all_meetings(meetings: List[List[int]]) -> bool:
    meetings.sort()

    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i - 1][1]:
            return False

    return True


# Time complexity: O(n * log(n))
# Space complexity: O(log(n)) - needed by the sorting algorithm


tests = [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
]
run_tests(can_attend_all_meetings, tests)
