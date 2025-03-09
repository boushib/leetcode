from tests import run_tests
from heapq import heapify, heappush, heappop
from collections import Counter


def reorganize_string(s):
    res = []
    prev_char, prev_char_count = None, 0
    max_heap = [(-count, char) for char, count in Counter(s).items()]
    heapify(max_heap)

    while max_heap:
        char_count, char = heappop(max_heap)
        res.append(char)

        if prev_char_count < 0:
            heappush(max_heap, (prev_char_count, prev_char))

        prev_char, prev_char_count = char, char_count + 1

    return "".join(res) if len(res) == len(s) else ""


# Time complexity: O(n * log(k)) with k total unique chars in s -> O(n) since k is bounded by 26
# Space complexity: O(k) -> O(1)


tests = [("aab", "aba"), ("aaab", "")]
run_tests(reorganize_string, tests)
