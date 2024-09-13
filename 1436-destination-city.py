from typing import List
from tests import run_tests


def destination_city(paths: List[List[str]]) -> str:
    start_cities = set()

    for a, _ in paths:
        start_cities.add(a)

    for _, b in paths:
        if b not in start_cities:
            return b

    return ""


tests = [([["London", "New York"], ["New York", "Lima"],
           ["Lima", "Sao Paulo"]], "Sao Paulo"),
         ([["B", "C"], ["D", "B"], ["C", "A"]], "A")]
run_tests(destination_city, tests)
