from tests import run_tests


def valid_word_abbreviation(word: str, abbr: str) -> bool:
    i, j = 0, 0

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            n = 0
            if abbr[j] == "0":
                return False
            while j < len(abbr) and abbr[j].isdigit():
                n = n * 10 + int(abbr[j])
                j += 1
            i += n
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)


tests = [
    (("internationalization", "i12iz4n"), True),
    (("internationalization", "i5a11o1"), True),
    (("apple", "a2e"), False),
    (("a", "01"), False),
    (("hi", "2i"), False),
]
run_tests(valid_word_abbreviation, tests)
