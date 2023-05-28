from lpsolver import SimplexSolver
import numpy as np
import unittest

"""
original qns
min 6x_1 + 8x_2
s.t. x_1 + 2x_2 \leq 6
    2x_1 +  x_2 \leq 6
     x_i \geq 0
stabdard form
min 6x_1 + 8x_2
s.t. x_1 + 2x_2 + x_3       = 6
    2x_1 +  x_2       + x_4 = 6
     x_i \geq 0
"""
solvable = {
    "c": np.array([6, 8]).T,
    "a_ub": np.array([[1, 2], [2, 1]]),
    "b_ub": np.array([6, 6]).T,
}


class TestLPSolver(unittest.TestCase):
    def setUp(self):
        self.solver = SimplexSolver(
            c=solvable["c"], a_ub=solvable["a_ub"], b_ub=solvable["b_ub"], mode="min"
        )

    def tearDown(self):
        pass

    def test_infeasible(self):
        pass

    def test_unbounded(self):
        pass

    def test_success(self):
        self.solver.solve()
