# simplex method

by converting any linear programs into a standard LP (format) and it can be
solved by simplex method. the simplified idea is to find corners or extreme
points or basic feasible solution. 

## extreme points

is defined as for a given set $S\subset{\mathbb{{R}^n}}$ a point $x$ is an
extreme point if there does not exists a three-tuple $(x^1,x^2,\mathbb{lambda})$
s.t. $x^1\in{S}\setminus\{x\},x^2\in{S}\setminus\{x\},\mathbb{\lambda}\in{(0,1)}$
and $x=\mathbb{\lambda}x^1+(1-\mathbb{\lambda})x^2$ (a convex combination). to
put to perspective, as long as a line can be drawn such that at least one point
is within the set, it is not an extreme point. for any LP if there is an
optimal solution there is an extreme point optimal solution.

> note if a soluiton is optimal it might not be an extreme point. solution can
> be a line in 2d space.

extreme points are geometric definition but by expressing it algebrically the
foundation for using simplex method is established.

## standard form LP

an LP is in standard form if the following is satisfied

1. all RHS value are nonnegative (LHS are $f(x)$)
1. all the variables are nonnegatives
1. all constraints are equalities

no restrictions on objective functions

for 2. if $2x_1+3x_2\leq{4},x_1\leq{0}\implies{-2x_1+3x_2\leq{4},x_1\geq{0}}$;
if $x_i$ is free replace it by $x'-x''$ where $x',x''\geq{0}$ for $2x_1+3x_2\leq{4},x_1 urs.$

for 3. for a geq or leq constraint, add a slack variable e.g.
$2x_1+3x_2\leq{4}\implies{2x_1+3x_2+x_3=4,x_3\geq{0}}$ and
$2x_1+3x_2\geq{4}\implies{2x_1+3x_2-x_3=4,x_3\geq{0}}$. this variable measures
the gap between LHS and RHS.

once LP is standardized it is solved by finding

$$
\min{c^Tx}\\
\text{s.t. } Ax=b\\
x\geq{0}
$$

where $c$ is the objective function, $A$ is the constraints and $b$ is the RHS;
objective function can be either max or min.

> why objective function can be either max or min?

## basic solutions

by having $A,b,c$ how to obtain extreme points? it does not concerns about the
objective function thus $c$. it only considers the boundary of the feasible
region. supposed that in standard LP with $m$ constraints and $n$ variables,
assuming $A$ has $m$ pivots i.e. all rows are independent, then it implies that
$m\leq{n}$

> rows independent? is the statement of $n\times{n}$ invertible matrix ? if
> $r\geq{c}$ there exists some dependencies i.e. redundant? is that why we are
> interested only in $r\leq{c}$

given that $r\leq{c}$, basic solution is formed by selecting some columns. a
basic solution to a standardized LP is a solution that (1) has $n-m$ variables
being $0$ and (2) satisfies $Ax=b$.

- $n-m$ variables chosen to be zero are nonbasic variables
- remaining $m$ variables are basic variables
- set of basic variables are called basis
- these $m$ columns form a invertible $m\times{m}$ matrix

it is denoted that $x_B\in{\mathbb{R}^m}$ and $x_N\in{\mathbb{R}^{n-m}}$ to
denote basic and nonbasic variables, with respect to a given set of basic
variables $B$. $x_N=0,x_B=A_B^{-1}b$

> although mixed usage, rc and mn are equivalent.

there is at most $\begin{pmatrix}n\\ m\end{pmatrix}$ bases can be choosed from.
it is less than nCr as basis cant be formed i.e. non invertible. among the
basic solutions only some are feasible. the definition ensure that $Ax=b$ is
satisfied, if it also satisfies $\forall{x_i}\geq{0}$ it satisfies all
constraints and thus basic feasible solutions (bfs). bfs are extreme points.

> note focus on the original variables and ignore the slack variables when
> identifying extreme points on the plot

theorem: standardized LP's solution is an extreme point of the feasible region
iff it is a bfs to the LP.

extreme points are geometrical definition and bfs are algebraical definitions.
search among bfs is by moving to a better adjacent bfs from the current one.
two bases are adjacent if exactly one of their **variables** is different, two
bfs are adjacent if their associated bases are adjacent.

> movement through edges, if there is a better bfs it hints improving direction
> , if there isnt bfs is optimal

## the idea

qns

- which edge to move along?
- when to stop moving?

these qns must be answered algebraically instead of geometrically. this is
achieved by replacing one basic variable by a nonbasic variable. first select
one nonbasic variable to enter the basis and select one basic variable to leave
the basis, e.g.

$$
B_1=(x_1, x_2, x_3)\rArr B_2=(x_2, x_3, x_5)
$$

where $x_5$ is nonbasic.

> "entering and leaving": nonbasic variable entering means making it nonzero
> increasing its value from zero to some positive value and become basic, and
> when this variable decrease, the removed basic variable decreases to zero
> becomes nonbasic.
> how to think about it? is it suggesting that that basic variable is not
> contributing to the objective?

### the first step

$$
\begin{alignedat}{7}
\max\quad        & 2x_1 & {} + {} & 3x_2  &         &         & \\
\text{s.t.}\quad & x_1  & {} + {} & 2x_2  & {} + {} & x_3 & {} + {} &     & {} = {} & 6\\
                 & 2x_1 & {} + {} & x_2   & {} + {} &     & {} + {} & x_4 & {} = {} & 8\\
\end{alignedat}
$$
$$
x_i\geq{0}\quad \forall{i}=1,...,4
$$

by having $z=2x_1+3x_2$ and rearranging it into $z-2x_1-3x_2=0$ allows to solve
for the z value i.e. maximizing it. also non z variables must be non negatives.
it is the zeroth constraint.

an initial bfs can be found by taking $x_1=x_2=z$ as $0$ and have $x_3=6$,
$x_4=8$. this is feasible given it is an identity matrix and the RHS is
nonnegative. next check the 0th constraint if $z$ increases (in max problem),
if the nonbasic variables increases and in this case, yes. thus,

$$
(0,0,6,8,)\Rarr(1,0,5,6)\Rarr(2,0,4,4)\Rarr...
$$

while $x_2$ remains 0 and eventually stops at $(4,0,2,0)$. this is indicated by
the ratio of RHS and entering column because $\frac{8}{2}\lt\frac{6}{1}$. $x_4$
becomes 0 sonner than $x_3$. choose $\min{\text{Var}_j(r_i)},\forall{i}=1,...,m$
where $j$ is the basic variable of interest.

> such scanario almost never exists.

### the second step

it is rather mundane to explain. basically trying to check all the constrains
how would each variable behaves if there is an increase of a the entering
nonbasic variable w.r.t to $z$. this does not scale well with the number of
variables.

a better approach is to ensure that the system only allows exactly one basic
variable and 0th constraint no basic variable. in other words, basic columns
should be in identity matrix (row 1 to m) and a zero vector in row 0. another
way of thinking is to make sure that for all rowsl$=$ to $n$ have exactly one
basic variable and this is achieved through elementary row operations.

### the last step

it is reached by finding no more improvement for $z$ i.e. $z + Ax_3 + Bx_4=C$.
any increment of $x_3,x_4$ does not improve $z$ w.r.t the objective.

### summing up

find bfs with its basis. for nonbasic variables with +ve coefficients in the
0th row (for min problem), choose one to enter. if there is none, terminate
and report current bfs is optimal. do a ratio test from the nonbasic/entering
variables, decide which one to leave. find new basis. ensure system meets 1.
identity matrix in constraints (row 1 to row m) and 2. zeros in objective
function. for any ties, choose the smallest index suitable variable.

a great visualization method is the tableau format. in the format

| -1 | 0 | 0 | 0 | 0 | 0 |
|----|---|---|---|---|---|
| 2 | -1 | 1 | 0 | 0 | $x_3=4$ |
| 2 | 1 | 0 | 1 | 0 | $x_4=8 |
| 0 | 1 | 0 | 0 | 1 | $x_5=3$ |

do a ratio test we got row 1 col 1. $x_3$ to leave, $x_1$ of row 1 to reduce to
1 and remaining to zero by elementary row operations. in the case where in a
max problem the entering column $m$th row's ratio test turns out to be -ve, it
is excluded from the ratio test.

> what about min problem? same no -ve

the numbers in 0th row is called reduced costs and they should hint the
entering column

## unbounded LP

LP is unbounded if:

- there is an improving direction
- but in that direction there is always a better solution

this can be checked easily from a simplex tableau. if the ratio test fails
completely i.e. all ratio test values is -ve.

## infeasible LP

for $\geq{0}$ in a $\min{}$ problem finding bfs is trivial as feasible basis
with slack variable $y$ can be added. what if there are some $=$ and $\geq{}$
constraints? by implementing a two phase LP where

phase I LP is formed by first getting the standard form (P) and brute force
introducing slack variables (Q). if has a trivial bfs $(x,y)=(0,b)$ we can
apply the simplex method, i.e.

$$
\begin{align*}
\min \quad c^Tx\\
\text{s.t.} \quad Ax=b\\
x\geq{0}
\end{align*}
\rArr
\begin{align*}
\min \quad 1^Ty\\
\text{s.t.} \quad Ax+Iy=b\\
x,y\geq{0}
\end{align*}
$$

proposition: (P) is feaible iif (Q) has optimal $bfs(x,y)$ = $(\bar{x},0)$. in
this case $\bar{x}$ is a $bfs$ of (P).

if it is feasible, objective function of original (P) is recovered to get a
phase II LP. for the added variables, they are artificial and no physical
meaning, if a constraint already has a variables that can be included in the
trivial basis, the artificial variable is not required to be added in that
constraint. this happens to those $\leq{}$ constrais (if the RHS is
nonnegative). note the tableau has to be a valid one i.e. the basic columns
of 0th row should contain only 0.