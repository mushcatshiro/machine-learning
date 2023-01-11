# linear programming

applications

- product mix
- production decision
- inventory decision
- personnel scheduling

## terminology

basic elements of a program

$$
\min{f(x_1, x_2,...,x_n)}\\
s.t.\quad g_i(x_1, x_2,...,x_n)\leq{b_i}\quad\forall{i}=1,...,m\\
x_j\in{\mathbb{R}}\quad\forall{j}=1,...,n
$$

- objective function (to minimize or maximize)
- $m$ constraints
- $n$ decision variable

we may write the decision variables into

$$
X = \begin{bmatrix}
    x_1\\x_2\\...\\x_n
\end{bmatrix} = (x_1,x_2,...,x_n)
$$

as a vector.

> note the parenthesis (square vs round)

$f:\mathbb{R}^{n}\rarr\mathbb{R}$ and $g_i:\mathbb{R}^{n}\rarr\mathbb{R}$

### tranformation

- $\max{f(x)}\hArr\min{-f(x)}$
- $g_i(x)\geq{b_i}\hArr{-g_i(x)}\leq{-b_i}$
- $g_i(x)=b_i\hArr{g_i(x)\leq{b_i}\quad\And\quad g_i(x)\geq{b_i}\text{, i.e. }-g_i(x)\leq{-b_i}}$

SNOTE:
$$
\max(x_1-x_2)\\
s.t.\quad (-2x_1+x_2)\geq{-3}\\
x_1+4x_2=5
$$

is equivalent to

$$
\min(-x_1+x_2)\\
s.t.\quad (2x_1-x_2)\leq{3}\\
x_1+4x_2\leq{5}\\
-x_1-4x_2\leq{-5}
$$

thus we just need to learn to solve minimize problem.

### sign constraints

- sign constraints: $x_i\geq{0}\parallel x_i\leq{0}$
- functional constraints: all others

for a variable $x_i$
- nonnegative
- nonpositive
- unrestricted in sign (urs.) or free

### feasible solutions

- a feasible solutions satisfies all the constraints
- an infeasible solution violates at least one constraints

by combining all sets of feasible solution we have a feasible region or feasible
set, which might be empty. an optiminal solution is a feasible solution that
attains the largest objective value for a maxization problem or vice versa.
however it might not be unique and there might not be an optimal solution.

### binding constraints

for any given solution, a constraint may be binding with the following definition:

let $g(\cdot)\leq{b}$ be an inequality constraint and $\bar{x}$ be a solution.
$g(\cdot)\leq{b}$ is binding at $\bar{x}$ if $g(\bar{x})={b}$. an inequality is
nonbinding at a point if it is strict "better" at that point. an equality
constraint is always binding at any feasible solution.

SNOTE:

- $x_1+x_2\leq{10}$ is binding at $(x_1,x_2)=(2,8)$
- $2x_1+x_2\geq{6}$ is nonbinding at $(x_1,x_2)=(2,8)$
- $x_1+3x_2=9$ is binding at $(x_1,x_2)=(6,1)$

### strict constraints

an inequality maybe strict or weak. if its strict then the two sides cannot be
equal; it its weak then the two sides may be equal. a practical mathematical
program's inequalities are all weak as strict inequalities will results in
failed to obtain optimal solution.

SNOTE: $\min{x}\quad s.t. \quad x>0$

think of a budget of $500, we should be able to use up to $500 thus in OR weak
constraints is used for discussion.

## linear programs

a LP is such that if all $f$ and $g_i$s are linear functions. linear functions
are functions that may be expressed as $\sum{a_jx_j}$ where $a_j\in{\mathbb{R}}$
for all $j$ s. it can be rewritten as $\hat{a}=(a_1,...a_n)$ and $f(x)=\hat{a}^{T}x$.

- constraints coefficients
- objective coefficients

## graphical approach

for LP with two decision variables, it is prossible to solve them with the
graphical approach. basically we first draw out all the constraints equations 
on the cartesian plane and find their intersection. then draw isoquant lines
for the objective function. push the isoquant lines to the end of the feasible
region and stop when its infeasible. identify the (2) binding constraints at
the optimal solutions. set the binding constraints to equalities and then solve
the linear system for an optimal solution.

> note the difference between optimal solution and objective functions

## three type of LPs

- infeasible: feasible region is empty
- unbounded: for any feasible solution, there is some better solution
- finitely optimal (having an optimal solution): not infeasible nor unbounded
  - unique optimal solution
  - multiple optimal solution

> note unbounded feasible region does not imply unbounded LP

### simple LP formulation - product mix

desk and tables. desk requires 3 unit of wood, 1 hour of labour and 50 minutes
of machine time; table requires 5 unit of wood, 2 hour of labour and 20 minutes
of machine time. all produced goods will be sold out. for each days, 200
labours each work 8 hours, 50 machines that runs for 16 hours and a supply of
3600 units of wood. desk and tables are sold at $700 and $900 per unit.

solution

$$
\begin{align*}
\max{(700x_d+900x_t)}\\
s.t.\quad 3x_d+5x_t\leq{3600}\\
x_d+2x_t\leq{200*8}\\
50x_d+20x_t\leq{50*16*60}\\
x_d\geq{0}\\
x_t\geq{0}   
\end{align*}
$$

ans: $(884.21, 189.47)$

### simple LP formulation - production and inventory

decision making includes those that happens in the future, this is also known
as **multi-period problems**.

for the coming four days, the marketing manager promised to fulfill the
following demands,

- d1: 100
- d2: 150
- d3: 200
- d4: 170

unit production costs are diferent for different days

- d1: 9
- d2: 12
- d3: 10
- d4: 12

price is fixed i.e. maximizing profit equals to minimizing costs. inventory is
possible with cost of $1 per unit per day.

hint: begining inventory + production - sales = ending inventory. inventory
costs are calculated according to ending inventory. there are inventory balance
constraints (first four) and demand fulfullment constraints (next four).

$$
x_t: \text{day t production quantity}\\
y_t: \text{day t ending inventory}\\
\begin{align*}
\min{(9x_1+12x_2+10x_3+12x_4+y_1+y_2+y_3+y_4)}\\
s.t.\quad x_1\geq{100}\\
x_2+y_1\geq{150}\\
x_3+y_2\geq{200}\\
x_4+y_3\geq{170}\\
x_1-100=y_1\\
y_1+x_2-150=y_2\\
y_2+x_3-200=y_3\\
y_3+x_4-170=y_4\\
x_t\geq{0}\\  
y_t\geq{0}
\end{align*}
$$

the formulation above might be slightly daunting. it is possible to simplify it
. inventory balancing and nonnegativity imply demand fulfillment. e.g. day 1
$x_1-100=y_1$ and $y_1\geq{0}$ means $x_1\geq{100}$. thus,

$$
\begin{align*}
\min{(9x_1+12x_2+10x_3+12x_4+y_1+y_2+y_3+y_4)}\\
s.t.\quad x_1-100=y_1\\
y_1+x_2-150=y_2\\
y_2+x_3-200=y_3\\
y_3+x_4-170=y_4\\
x_t\geq{0}\\  
y_t\geq{0}
\end{align*}
$$

identifying redundant constraints and removing them (will not alter the
feasible region) helps to reduce program complexity. a further simplification
involve modifying $y_3+x_4-170=y_4$ into $y_3+x_4-170=0$ and removing $y_4 from
the objective function. however this is not recommended because,

- solver should be able to notice this
- too difficult especially instance scale is large i.e. 10k variate objective function

### simple LP formulation - scheduling

each employee must work for five consecutive days and take two consecutive days
of leave. number of employee required for each day,

| mon | tues | wed | thu | fri | sat | sun |
|-----|------|-----|-----|-----|-----|-----|
| 110 | 80   | 150 | 30  | 70  | 160 | 120 |

there are seven shifts and objective is to minimize number of employees.

$$
\begin{align*}
\min{(x_m+x_t+x_w+x_{th}+x_f+x_{sa}+x_{su})}\\
s.t.\quad x_m+x_{th}+x_f+x_{sa}+x_{su}\geq{110}\\
x_m+x_t+x_f+x_{sa}+x_{su}\geq{80}\\
x_m+x_t+x_w+x_{sa}+x_{su}\geq{150}\\
x_m+x_t+x_w+x_{th}+x_{su}\geq{30}\\
x_m+x_t+x_w+x_{th}+x_f\geq{70}\\
x_{sa}+x_t+x_w+x_{th}+x_f\geq{160}\\
x_{sa}+x_{su}+x_w+x_{th}+x_f\geq{120}\\
x_i\geq{0}\\  
\end{align*}
$$

> note x_i >= 0 meaning it can be fraction, which is totally fine. solving linear
> program is much easier than integer program

decision variable what can we control

> also on setting decision variables i.e. x_i one need to consider carefully
> such that they fits to the definition of objective and constraints functions

ans:

## Compact LP formulation

problems in practice are usually in large scale i.e. variable and constraints
are more than hand be able to write down, and they may be groupped together.
compact formulation is used to enhance readability and efficiency, using

- indices $(i, j, k)$
- summation $\sum$a
- for all $(\forall)$

### production-inventory problem revisited

having several periods, in each period we produce and sell. unsold products
becomes ending inventories. same goal to minimize total cost.


$$
\min{(9x_1+12x_2+10x_3+12x_4+y_1+y_2+y_3+y_4)}\\
\text{into}\\
\min \sum_{t=1}^{4}{C_tx_t+y_t}\\
$$

where $C_t$ is cost of day $t=1, 2, 3, 4$

$$
x_1-100=y_1,\quad y_1+x_2-150=y_2, \quad y_2+x_3-200=y_3, \quad y_3+x_4-170=y_4\\
\text{into}\\
y_{t-1}+x_t-D_t=y_t \forall{t}=0, ..., 4\\
y_0 = 0
$$

which $y_t =\text{ending inventory of day t, t = 0, 1, ... 4}$

> some convention: lower case for variables; uppercase for parameters

#### parameter declaration

when creating parameter sets, specific values are not needed. specify **range**
through indices. they should be at the begining of the formulation.

| parameters   | variables        |
|--------------|------------------|
| known values | to be determined |
| exogenous (fixed) | endogenous  |

### product mix

$$
\begin{align*}
\max{(700x_d+900x_t)}\\
s.t.\quad 3x_d+5x_t\leq{3600}\\
x_d+2x_t\leq{200*8}\\
50x_d+20x_t\leq{50*16*60}\\
x_d\geq{0}\\
x_t\geq{0}   
\end{align*}
$$

into

$$
\begin{align*}
\max{\sum_{j=1}^{n}{P_jx_j}}\\
s.t.\quad \sum_{j=1}^{n}A_{ij}x_j\leq{R_i}\quad \forall{i}=1,....m\\
x_j\geq{0}\quad \forall{j}=1,...,n\\
\end{align*}
$$

which

$$P_j=\text{units of product j to produce } \forall{j}=1,...n\\
R_i=\text{resource supply limit}\\
A_{ij}=\text{resource i required for producing one unit of product j}
$$

or taking it even further,

$$
\begin{align*}
\max{\sum_{j=1}^{n}{P_jx_j}}\\
s.t.\quad \sum_{j\in{J}}A_{ij}x_j\leq{R_i}\quad \forall{i}\in{I}\\
x_j\geq{0}\quad \forall{j}\in{J}\\
\end{align*}
$$

by defining index sets $J=\{1,2,...,n\}$ and $I=\{1,2,...,m\}$

## course terminology

| problem | intance |
|---------|---------|
| abstract task | concrete specification of a problem |
| everything in symbol | concrete values into symbol |

once a problem is solve all instance can be solve using the formulation. e.g.
having same set of equipments and different line of product with same
constraints, once it solved for one product line we just need to run another
instance to know whats is the optimum solution for that product line.

## python LP solver

```python
from scipy.optimize import linprog

# solving the product mix problem

obj = [-700, -900]
lhs_ineq = [[3, 5],
            [1, 2],
            [50, 20]]
rhs_ineq = [[3600],
            [200*8],
            [50*16*60]]
bounds = [(0, float("inf")),
          (0, float("inf"))]


opt = linprog(
    c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
    bounds=bounds
)
```

## assignments

### q1

consider the following LP

$$
\begin{align*}
\max{2x_1-x_2}\\
s.t. \quad 8x_1-4x_2\leq{16}\\
3x_1-4x_2\leq{16}\\
x_1\geq{0}\\
x_2\leq{0}
\end{align*}
$$

using `scipy.optimize.linprog` allows user to find the first optimal solution,
however if there is multiple optimal solution, it will not be able to tell.
next on binding, it can also be true for $x_2\leq{0}$

ans: The LP has multiple optimal solution. The constraints $8x_1-4x_2\leq{16}$
and $x_2\leq{0}$ are binding at $(x_1,x_2)=(2,0)$

### q2

consider the following t/f questions

- If an LP is unbounded, its feasible region must be unbounded.
- If an LP has an unbounded feasible region, it must be unbounded.
- If an LP has an optimal solution, there must be at least two binding constraint(s) at that optimal solution.
- If an LP has two optimal solutions, there must be another optimal solution that is different from the first two.
- An LP's optimal solution is always an extreme point. 

ans: (incorrect) TFTFF, TFTFT, TFTTF

### q3

solve

$$
\begin{align*}
\max 3x_1+5x_2\\
s.t. \quad x_1+x_2\leq{16}\\
x_1+4x_2\leq{20}\\
2x_1+x_2\geq{6}\\
x_1\geq{0}\\
x_2\leq{0}
\end{align*}
$$

ans: $(44/3, 4/3)$

### q4

factory produce table and chair. wood is needed to build the products, $13 per
piece, with max 50 per day. table need 7 woods and chair need 4. time taken for
table is 1.1 and chair is 0.7. 10 hour work per day. price is $100 for table
and $70 for chair.

$$
\begin{align*}
\max Ax_1+18x_2\\
s.t. \quad 7x_1+4x_2\leq{50}\\
Bx_1+Cx_2\leq{10}\\
x_i\geq{0} \quad \forall{i}=1, 2
\end{align*}
$$

ans: $A=9,B=1/1.1,C=1/0.7$

> take note of B and C, one need to understand that 0.7 and 1.1 are product
> per hour, but the constraint is on hour

### q5

how many chair should be produced in q4?

ans: 7