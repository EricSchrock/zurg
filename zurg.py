from itertools import combinations
from typing import List


def one_returns(not_across: List[int], across: List[int], time_spent: int, time_limit: int, accumulator: list) -> List[list]:
    '''Splits the search problem by every toy that could return across the bridge with the flashlight. Terminates early if the time limit for getting all the toys across the bridge is exceeded. Also terminates if all the toys are across the bridge.

    :param not_across: Toys not yet across the bridge
    :type not_across: List[int]
    :param across: Toys across the bridge
    :type across: List[int]
    :param time_spent: Time spent so far crossing the bridge
    :type time_spent: int
    :param time_limit: Time toys must all be across the bridge by
    :type time_limit: int
    :param accumulator: Partial solution being explored
    :type accumulator: list

    :returns: A list of solutions
    :rtype: List[list]
    '''
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
    '''Splits the search problem by every pair of toys that could cross the bridge. Terminates early if the time limit for getting all the toys across the bridge is exceeded.

    :param not_across: Toys not yet across the bridge
    :type not_across: List[int]
    :param across: Toys across the bridge
    :type across: List[int]
    :param time_spent: Time spent so far crossing the bridge
    :type time_spent: int
    :param time_limit: Time toys must all be across the bridge by
    :type time_limit: int
    :param accumulator: Partial solution being explored
    :type accumulator: list

    :returns: A list of solutions
    :rtype: List[list]
    '''
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
    '''Solves the "Escape from Zurg" puzzle.

    :returns: A list of solutions
    :rtype: List[list]
    '''
    return two_cross(not_across  = [5,10,20,25],
                     across      = [],
                     time_spent  = 0,
                     time_limit  = 60,
                     accumulator = [])


if __name__ == "__main__":
    for solution in zurg():
        print(solution)
