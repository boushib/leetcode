from tests import run_tests


def to_goat_latin(s: str) -> str:
    volwels = set(["a", "e", "i", "o", "u"])
    words = s.split(" ")

    for i, w in enumerate(words):
        if w[0].lower() not in volwels:
            w = w[1:] + w[0]
        words[i] = w + "ma" + "a" * (i + 1)

    return " ".join(words)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    (
        "The quick brown fox jumped over the lazy dog",
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
    ),
    (
        "Each word consists of lowercase and uppercase letters only",
        "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa",
    ),
]
run_tests(to_goat_latin, tests)
