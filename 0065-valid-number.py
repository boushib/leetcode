from tests import run_tests


def is_number(s: str) -> bool:
    """
    Rules:
    1. At least 1 digit
    2. If a sign is present it should come first (begenning of the number of after the exponent)
    3. <= 1 exponents
    4. <= 1 dots (only integers are allowed in exponent)
    """
    digit_count, exponent_count, dot_count = 0, 0, 0

    for i, c in enumerate(s):
        if c.isdigit():
            digit_count += 1
        elif c in ["+", "-"]:
            if i > 0 and s[i - 1].lower() != "e":
                return False
        elif c.lower() == "e":
            if digit_count == 0 or exponent_count == 1:
                return False
            exponent_count += 1
            digit_count = 0
        elif c == ".":
            if dot_count == 1 or exponent_count == 1:
                return False
            dot_count += 1
        else:
            return False

    return digit_count >= 1


tests = [
    ("2", True),
    ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("-.9", True),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("+6e-1", True),
    ("53.5e93", True),
    ("-123.456e789", True),
    ("abc", False),
    ("1a", False),
    ("1e", False),
    ("e3", False),
    ("99e2.5", False),
    ("--6", False),
    ("-+3", False),
    ("95a54e53", False),
]
run_tests(is_number, tests)
