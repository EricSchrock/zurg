from itertools import combinations
from typing import List


def one_returns(not_across: List[int], across: List[int], time_spent: int, time_limit: int, accumulator: list) -> List[list]:
    if time_spent > time_limit:
        return []

    if not_across == []:
        return [accumulator]

    solutions = []
    for toy in across:
        solutions += two_cross(not_across  = not_across + [toy],
                               across      = [x for x in across if x is not toy],
                               time_spent  = time_spent + toy,
                               time_limit  = time_limit,
                               accumulator = accumulator + [toy])

    return solutions


def two_cross(not_across: List[int], across: List[int], time_spent: int, time_limit: int, accumulator: list) -> List[list]:
    if time_spent > time_limit:
        return []

    pairs = list(combinations(not_across, r=2))

    solutions = []
    for pair in pairs:
        pair = sorted(list(pair))
        solutions += one_returns(not_across  = [x for x in not_across if x not in pair],
                                 across      = across + pair,
                                 time_spent  = time_spent + max(pair),
                                 time_limit  = time_limit,
                                 accumulator = accumulator + [pair])

    return solutions


def zurg() -> List[list]:
    return two_cross(not_across  = [5,10,20,25],
                     across      = [],
                     time_spent  = 0,
                     time_limit  = 60,
                     accumulator = [])


if __name__ == "__main__":
    for solution in zurg():
        print(solution)
