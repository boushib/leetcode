from typing import List
from tests import run_tests


def common_chars(words: List[str]) -> List[str]:
    res = []
    count = {}

    for c in words[0]:
        count[c] = count.get(c, 0) + 1

    for w in words[1:]:
        curr_count = {}

        for c in w:
            curr_count[c] = curr_count.get(c, 0) + 1

        for k, v in count.items():
            count[k] = min(count[k], curr_count.get(k, 0))

    for k, v in count.items():
        for _ in range(v):
            res.append(k)

    return res


tests = [(["bella", "label", "roller"], ["e", "l", "l"]), (["cool", "lock", "cook"], ["c", "o"])]
run_tests(common_chars, tests)
