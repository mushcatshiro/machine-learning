import numpy as np  # noqa

from dataclasses import dataclass
import logging


logger = logging.getLogger(__name__)
MAX_ITERATIONS = 1_000_000
MIN_PROBELM = "min"
MAX_PROBLEM = "max"


@dataclass
class LinearProgramResult:
    is_feasible: bool = True
    is_bounded: bool = True
    x: list = []
    opt_val: float = 0.0
    out_of_max_iterations: bool = 0.0


class SimplexSolver:
    def __init__(
        self, c, a_ub, b_ub, a_eq, b_eq, a_lb=None, b_lb=None, mode=None
    ):
        """
        assumes:
        - a min problem is provided thus `a_lb`, `b_lb` and `mode` are None.
        - inputs `a_*`, `b_*`, `c` are vertically aligned (?)
        """
        self.c = c
        self.a_ub = a_ub
        self.b_ub = b_ub
        self.a_eq = a_eq
        self.b_eq = b_eq
        self.a_lb = a_lb
        self.b_lb = b_lb
        self.iterations = 0
        if mode is None:
            self.mode = "min"
        elif mode in [MAX_PROBLEM, MIN_PROBELM]:
            self.mode = mode
        else:
            raise ValueError("expected 'min' or 'max'")

    def is_feasible(self):
        return True

    def is_bounded(self):
        return True

    def is_valid_matrix(self):
        return True

    def is_optimal(self):
        return True

    def row_operation(self):
        pass

    def standardize_matrix(self):
        # TODO turn into min problem?
        if self.mode == MIN_PROBELM:
            pass
        elif self.mode == MAX_PROBLEM:
            pass

    def make_matrix_valid(self):
        pass

    def make_matrix_with_one_basic_variable(self):
        pass

    def choose_row_col(self):
        r = 0
        c = 0
        return r, c

    def _check(self, r, c):
        """
        had a feeling that checking for feasibility and bounded will be called
        throughout the iterations
        it feels weird shouldnt it is validated bounded before moving to solve
        it? on second thought, it should be check every iteration
        """
        if not self.is_bounded():
            return LinearProgramResult(is_bounded=False)
        if not self.is_feasible():
            return LinearProgramResult(is_feasible=False)
        if not self.is_valid_matrix():
            self.make_matrix_valid()
        self.make_matrix_with_one_basic_variable()
        return

    def find_bfs(self):
        pass

    def solve(self):
        self.standardize_matrix()
        while self.iterations <= MAX_ITERATIONS:
            """
            choose row and col?
            """
            r, c = self.choose_row_col()
            res = self._check()
            if isinstance(res, LinearProgramResult):
                return res
            self.find_bfs()
            if self.is_optimal():
                break
        return LinearProgramResult()
