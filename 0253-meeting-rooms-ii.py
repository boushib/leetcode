from typing import List
from tests import run_tests


def min_meeting_rooms(meetings: List[List[int]]) -> int:
    res = 0  # max rooms
    used_rooms = 0
    meeting_start_times = sorted(m[0] for m in meetings)
    meeting_end_times = sorted(m[1] for m in meetings)
    i, j = 0, 0

    while i < len(meetings):
        # new meeting started before current meeting ends
        if meeting_start_times[i] < meeting_end_times[j]:
            used_rooms += 1
            i += 1
        else:
            used_rooms -= 1
            j += 1

        res = max(res, used_rooms)

    return res


# Time complexity: ??
# Space complexity: ??


tests = [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1)]
run_tests(min_meeting_rooms, tests)
