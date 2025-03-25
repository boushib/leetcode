from typing import List
from tests import run_tests
from heapq import heappop, heappush


def most_booked_meeting_room(n: int, meetings: List[List[int]]) -> int:
    meetings.sort()
    available_rooms = [i for i in range(n)]
    used_rooms = []  # (end_time, room_id)
    meetings_scheduled_by_room = {i: 0 for i in range(n)}  # room -> meetings_scheduled

    for start_time, end_time in meetings:
        # end meetings that are finished <= start
        while used_rooms and used_rooms[0][0] <= start_time:
            heappush(available_rooms, heappop(used_rooms)[1])

        # if no room is available
        if not available_rooms:
            curr_end_time, room_id = heappop(used_rooms)
            end_time = curr_end_time + (end_time - start_time)
            heappush(available_rooms, room_id)

        room_id = heappop(available_rooms)
        heappush(used_rooms, [end_time, room_id])
        meetings_scheduled_by_room[room_id] += 1

    max_booking_count = max(meetings_scheduled_by_room.values())

    for room, count in meetings_scheduled_by_room.items():
        if count == max_booking_count:
            return room


# Time complexity: O(m* log(m) + m * log(n))
# Space complexity: O(m + log(n))


tests = [((2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0), ((3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)]
run_tests(most_booked_meeting_room, tests)
