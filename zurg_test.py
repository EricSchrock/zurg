from zurg import *

def test_zurg():
    solutions = zurg()

    assert len(solutions) == 108
    assert [[5,10], 5,[20,25],10,[5,10]] in solutions
    assert [[5,10],10,[20,25], 5,[5,10]] in solutions
