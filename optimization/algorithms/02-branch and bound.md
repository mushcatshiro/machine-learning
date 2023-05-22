# branch and bound

integer programming. due to integer's nature, its feasible region is not a full
polygon. an approach is to first solve its linear relaxation, which is a form
of linear program. with the initial solution e.g. $(2.3, Y)$, two subproblem is
formed with $x\geq{3}$ and $x\leq{2}$ as the additional constraints. the
process is repeated until there is a interger solution found.

main focus on this chapter is on BnB and heuristics for solving linear IP. BnB
finds optimal solution for any IP by solving multiple LPs. each of the LPs are
solve independently and is time consuming. often this is addressed by looking
for a near optimal feasible solution. an algorithm that generates a feasible
solution is short time is called heuristics. generally it works for most of the
time.

## linear relaxation

using simplex method the assumption is the feasible region is continuous,
however IP's feasible is discrete thus not possible to move along edges.

definition: given an IP, linear relaxation is the resulting LP after removing
all the integer constraints.

in short from $x_i\in{\mathbb{Z}_{+}}$ to $x_i\geq{0}$. note that 
$x_i\in{\mathbb{Z}_{+}}$ is equivalent to $x_i\in{\mathbb{Z}}$ and $x_i\geq{0}$

in a minimization IP, its linear relaxation provides a lower bound.

proposition: let $z^\ast$ and $z^\prime$ be the objective values associated to the
optimal solutions of a minimization IP and its linear relaxation respectively,
then $z^\prime\leq{z^\ast}$

in a maximization IP, linear relaxation provides an upper bound for the
solution.

as a result of the proposition earlier, if a linear relaxation is infeasible,
unbounded or obtained an optimal solution that is also feasible to the IP, the
IP is solved.

a simple idea of rounding up or down is proposed. a simple example is shown
below

$$
\begin{align*}
\max \quad 8x_1+5x_2\\
\text{s.t. } x_1+x_2\leq{6}\\
9x_1+5x_2\leq{45}\\
x_i\in{\mathbb{Z}_{+}}\forall{i}=1,2
\end{align*}
$$

where the LR-optimal solution is $(15/4, 9/4)$ however its IP optimal solution
is $(5,0)$. thus rounding linear relaxation is proven not IP optimal.

## branch and bound algorithm

the idea of rounding fails due to the fact that it eliminates too many feasible
points. instead of adding equalities (rounding), add inequalities. think it as
removing the points in between and limits (with constraint) at nearest integer
values. by branching into two new problems with the added constraints.

> the constraints increases as the branching operation goes on

BnB is supposed to stop when there is no better solutions be found in $n+1$
nodes and/or infeasible solution, i.e. bounding situation.

on where exactly to select a node to branch, a common approach is to always
choose the node with largest value. in general this yields a higher chance of
getting an overall large value. also focus on one subtree to get the IP
solution instead of jumping between non IP solution.

> variable selection to branch on is not discussed here.

BnB guarantees a solution if it exists at exponential time complexity $O(2^n)$
where $n$ is the number of integer variables. 

## solving knapsack problem

simplex method is general for LP however if the problem given has some unique
features, simplex method is not needed i.e. avoid simplex method is possible.

| item | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| value | 2 | 3 | 4 | 1 | 3 |
| weight | 4 | 5 | 3 | 1 | 4 |

choose four item and knapsack capacity is 11kg.

instead of adding 6 slack variables, sort all items according to the descending
order of value to weight ratio. select items one by on according to the order
until knapsack is full. last item may be partially selected and thus obtained a
LR-optimal solution.

next, branch on the zeroes and non integer variables. values is getting fixed
when constraints is added as knapsack problem only allows 1 and 0.

## heuristics

knapsack problem is NP hard. most researcher belives there is no efficient (
i.e. polynomial time) exact algorithm that finds an optimal solution. BnB might
be too slow for problems with large amount of variables. heuristic algorithms
is explored as it reports a solution in polynomial time and is near optimal.

### greedy algorithm

as described in the knapsack problem minus the branching part. the reported
$z^{ALG}=8$ and the optimal solution for this IP is 9. an optimality gap is the
quality/performance measurement of the reported solution. the absolute error is
$1$ and the percentage error is $11.1%$.

> optimality gap is always positive

### performance evaluation

the average case performance is measured by using small scale random instances.
each instance is solved by the algorithm and an exact one. average the
percentage error. the smaller it is the better it is.

large scale random instance test is conducted. however solving large scale
random instance is time consuming, instead obtain the upper bound of the
objective value of the optimal solution by linear relaxation.

> $\frac{z^\star-z^{\text{ALG}}}{z^\star}\leq{\frac{z^{\text{LR}}-z^{\text{ALG}}}{z^{\text{LR}}}}$

alternatively worst-case performance guarantee is analyzed i.e. $\alpha\leq{z^{\text{ALG}}/z^\star}$
it is interesting but difficult.

> designing heuristic algorithm is simple however evaluation and analysis is
> hard.