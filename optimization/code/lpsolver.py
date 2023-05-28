import numpy as np  # noqa

from dataclasses import dataclass
import logging


logger = logging.getLogger(__name__)
MAX_ITERATIONS = 1_000_000
MIN_PROBELM = "min"
MAX_PROBLEM = "max"


# @dataclass
class LinearProgramResult:
    is_feasible: bool = True
    is_bounded: bool = True
    x: list = []
    opt_val: float = 0.0
    out_of_max_iterations: bool = 0.0


class SimplexSolver:
    def __init__(
        self,
        c,
        a_ub=None,
        b_ub=None,
        a_eq=None,
        b_eq=None,
        a_lb=None,
        b_lb=None,
        bounds=(0, None),
        mode=None,
    ):
        """
        assumes:
        - a min problem is provided thus `a_lb`, `b_lb` and `mode` are None.
        - inputs `a_*`, `b_*`, `c` are vertically aligned (?)
        - inputs are np.ndarray(s)
        """
        self.c = c
        self.a_ub = a_ub
        self.b_ub = b_ub
        self.a_eq = a_eq
        self.b_eq = b_eq
        self.a_lb = a_lb
        self.b_lb = b_lb
        self.lbounds = bounds[0]
        self.ubound = bounds[1]
        self.slack_idx = None
        self.artificial_idx = None
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

    def shape_check(self):
        # dealing with None?
        assert self.a_eq.shape[0] == self.a_lb.shape[0] == self.a_ub.shape[0]
        self.slack_idx = self.a_lb.shape[0]

    def standardize_matrix(self):
        # TODO turn into min problem?
        # with such it simplifies the code a bit

        # all RHS value are non negative
        c = self.b_ub.T.shape
        neg_idx_b_ub = np.where(self.b_ub < np.zeros((c, 1)))
        # neg_idx_b_lb = np.where(self.b_lb < 0)
        print(f"neg idx b ub: {neg_idx_b_ub}")
        # print(f"neg_idx_b_lb: {neg_idx_b_lb}")
        for idx in neg_idx_b_ub:
            self.a_ub[idx, :] *= -1
        # for idx in neg_idx_b_lb:
        #     self.a_lb[idx, :] *= -1
        print(f"a_ub: {self.a_ub}")
        print(f"a_lb: {self.a_lb}")
        # all variables are nonnegatives
        if self.lbounds < 0:
            raise ValueError("variables lower must be geq 0")
        # all constraints are equalities
        if self.mode == MIN_PROBELM:
            # first deal with upper bound
            r, c = self.b_ub.shape
            ub_slack = np.ones((r, c))
            self.a_ub = np.concatenate((self.a_ub, ub_slack), axis=1)
            # addition of new slacks does not affect self.[l|u]bounds
            # TODO
            # edge case: dealing with 0s in constraints?
            # i.e. 2x_1 + 3x_2 \geq 0

            # next deal with lower bound
            r, c = self.b_lb.shape
            lb_slack = np.ones((r, c)) * -1
            self.a_ub = np.concatenate((self.a_ub, lb_slack), axis=1)
        elif self.mode == MAX_PROBLEM:
            raise ValueError("not supporting max problem")

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
        # self.shape_check()
        self.standardize_matrix()
        print(f"c   : {self.c}")
        print(f"a_ub: {self.a_ub}")
        return
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
