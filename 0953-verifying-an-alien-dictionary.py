from typing import List
from tests import run_tests


def is_alien_sorted(words: List[str], order: str) -> bool:
    order_map = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False

            x, y = words[i][j], words[i + 1][j]

            if x != y:
                if order_map[x] > order_map[y]:
                    return False
                break

    return True


# Time complexity: O(n * m), where n is the number of words and m is the size of the longest word
# Space complexity: O(1)


tests = [
    ((["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True),
    ((["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False),
    ((["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), False),
]
run_tests(is_alien_sorted, tests)
