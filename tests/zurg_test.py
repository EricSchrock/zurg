from math import inf
from zurg import one_returns, two_cross, zurg


class TestOneReturns:
    def test_termination_case_time_limit(self):
        solutions = one_returns(not_across  = [1],
                                across      = [2,3],
                                time_left   = -1,
                                accumulator = [[2,3]])

        assert solutions == []


    def test_termination_case_solution_found(self):
        solutions = one_returns(not_across  = [],
                                across      = [1,2,3],
                                time_left   = 0,
                                accumulator = [[2,3],2,[1,2]])

        assert len(solutions) == 1
        assert [[2,3], 2, [1,2]] in solutions


    def test_recursive_case_without_time_limit(self):
        solutions = one_returns(not_across  = [1],
                                across      = [2,3],
                                time_left   = inf,
                                accumulator = [[2,3]])

        assert len(solutions) == 2
        assert [[2,3],2,[1,2]] in solutions
        assert [[2,3],3,[1,3]] in solutions


    def test_recursive_case_with_time_limit(self):
        solutions = one_returns(not_across  = [1],
                                across      = [2,3],
                                time_left   = 4,
                                accumulator = [[2,3]])

        assert len(solutions) == 1
        assert [[2,3],2,[1,2]] in solutions


class TestTwoCross:
    def test_termination_case_time_limit(self):
        solutions = two_cross(not_across  = [1,2],
                              across      = [3],
                              time_left   = -1,
                              accumulator = [[2,3], 2])

        assert solutions == []


    def test_termination_case_solution_found(self):
        solutions = two_cross(not_across  = [1,2],
                              across      = [3],
                              time_left   = 2,
                              accumulator = [[2,3], 2])

        assert len(solutions) == 1
        assert [[2,3],2,[1,2]] in solutions


    def test_recursive_case_without_time_limit(self):
        solutions = two_cross(not_across  = [1,2,3],
                              across      = [],
                              time_left   = inf,
                              accumulator = [])

        assert len(solutions) == 6
        assert [[2,3],2,[1,2]] in solutions
        assert [[2,3],3,[1,3]] in solutions


    def test_recursive_case_with_time_limit(self):
        solutions = two_cross(not_across  = [1,2,3],
                              across      = [],
                              time_left   = 6,
                              accumulator = [])

        assert len(solutions) == 2
        assert [[1,2],1,[1,3]] in solutions
        assert [[1,3],1,[1,2]] in solutions


class TestZurg:
    def test_zurg(self):
        solutions = zurg()

        assert len(solutions) == 2
        assert [[5,10], 5,[20,25],10,[5,10]] in solutions
        assert [[5,10],10,[20,25], 5,[5,10]] in solutions
