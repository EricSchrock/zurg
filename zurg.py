def one_returns_with_flashlight(not_across, across, time_limit, solution):
    if not_across == []:
        return solution

    toy = across.pop()
    not_across.append(toy)
    solution.append(toy)

    return two_cross_bridge(not_across, across, time_limit, solution)


def two_cross_bridge(not_across, across, time_limit, solution):
    toy1 = not_across.pop()
    toy2 = not_across.pop()

    across += [toy1,toy2]
    solution.append([toy1,toy2])

    return one_returns_with_flashlight(not_across, across, time_limit, solution)


def zurg():
    not_across = [5,10,20,25]
    across = []
    time_limit = 60

    return two_cross_bridge(not_across, across, time_limit, solution=[])


if __name__ == "__main__":
    print(zurg())
