from typing import List
from tests import run_tests


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []

    res = []
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(index, curr_comb):
        if len(curr_comb) == len(digits):
            res.append(curr_comb)
            return None

        for letter in phone_map[digits[index]]:
            dfs(index + 1, curr_comb + letter)

    dfs(0, "")
    return res


# Time complexity: O(4^n)
# Space complexity: O(n)


tests = [
    ("2", ["a", "b", "c"]),
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("", []),
]
run_tests(letter_combinations, tests)
