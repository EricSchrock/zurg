from itertools import combinations

def one_returns(not_across, across, time_limit, accumulator):
    if not_across == []:
        return [accumulator]

    solutions = []
    for toy in across:
        solutions += two_cross(not_across  = not_across + [toy],
                               across      = [x for x in across if x is not toy],
                               time_limit  = time_limit,
                               accumulator = accumulator + [toy])

    return solutions


def two_cross(not_across, across, time_limit, accumulator):
    pairs = list(combinations(not_across, r=2))

    solutions = []
    for pair in pairs:
        pair = sorted(list(pair))
        solutions += one_returns(not_across  = [x for x in not_across if x not in pair],
                                 across      = across + pair,
                                 time_limit  = time_limit,
                                 accumulator = accumulator + [pair])

    return solutions


def zurg():
    not_across = [5,10,20,25]
    across = []
    time_limit = 60

    return two_cross(not_across, across, time_limit, accumulator=[])


if __name__ == "__main__":
    for solution in zurg():
        print(solution)
