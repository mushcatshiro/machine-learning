# linear programming duality

for any primal LP there is a dual LP which is

- unique and symmetric
- the dual of the dual LP is the primary LP formulation
- same objective value? function?
- if primal is solvable, solving dual is by looking at $C_{B}^{T}A_{B}^{-1}$
- primal's solution $x_{j}^{*}$ is +ve, the dual constraint is binding

the focus on this lecture is to duscuss on shadow price and do sensitivity
analysis. shadow price in short is if there is a slight chage in the constraint
, what is the new optimal solution? duality property helps to answer this
question easily.

## Primal-Dual pairs

consider the following LP

$$
\begin{align*}
z^*=\max{4x_1+5x_2+8x_3}\\
\text{s.t. }x_1+2x_2+3x_3\leq{6}\\
2x_1+x_2+2x_3\leq{4}\\
x_n\geq{0}\quad \forall{n}\in{1, 2, 3}
\end{align*}
$$

supposed the LP is difficult to solve and a propose solution of $\hat{x}=(0.5,1,1)$
with $\hat{z}=15$ given, if we know $z^{*}$ we can compare it with $\hat{z}$.
based on the question it is difficult to know $z^{*}$, if we can find an upper
bound of $z^{*}$ it means it is not good enough, else $z^{*}=\hat{z}$

by multiplying the first constraint by 2 and the second constraint by 1 and
adding them together we get

$$
4x_1+5x_2+8x_3\leq{16}
$$

compare this objective function we know $z^{*}\leq{16}$ (note this third 
constrained is purposely designed to be equal to objective function). in such
case, the upper bound is tight i.e. the objective value is known. with $\hat{z}=15$
, it can be concluded as quite good. even if the manipulation does not directly
yields the objective function, through comparisons it still gives some hint on
what might be the upper bound. in essence, finding appropriate coefficient to
multiply to constraints is equivalent to doing linear combinations.

for this case there are two constraints function thus by setting $y_1,y_2$ as
the coefficients,

$$
(y_1+2y_2)x_1+...\leq{6y_1+4y_2}
$$

> having $y_1,y_2\geq{0}$ to preserve $\leq{}$

next is to ensure that the objective function's $x_n$ are $\leq{ay_1+...zy_n}$
such that $z^{*}\leq{6y_1+4y_2}$ (see original constraints). this is
essentially solving another LP.

$$
\begin{align*}
\min{6y_1+4y_2}\\
\text{s.t. }y_1+2y_2\geq{3}\\
2y_1+y_2\geq{4}\\
3y_1+2y_2\geq{8}\\
y_n\geq{0}\quad \forall{y}\in{1,2}
\end{align*}
$$

the new LP is knows as the dual LP.

### nonpositive or free variables

the example showed is having all non negative constraints. supposed that the
given LP is the following,

$$
\begin{align*}
\max{3x_1+4x_2+8x_3}\\
\text{s.t. }x_1+2x_2+3x_3\leq{6}\\
2x_1+x_2+2x_3\leq{4}\\
x_1\geq{0}\\
x_2\leq{0}\\
x_3 \text{urs.}
\end{align*}
$$

> urs. -> unrestricted sign

the dual LP would be

$$
3x_1+4x_2+8x_3\leq{
    (y_1+2y_2)x_1+
    (2y_1+y_2)x_2+
    (3y_1+2y_2)x_3}
$$

and we need

$$
\begin{align*}
y_1+2y_2\geq{3}\\
2y_1+y_2\leq{4}\\
3y_1+2y_2=8
\end{align*}
$$

> think about the leq and geq's. equality because $x_3$ is free.

some observations

- primal max => dual min
- primal objective => dual RHS
- primal RHS => dual objective

- primal $\geq{0}$ variable => dual $\geq{}$ constraint
- primal $\leq{0}$ variable => dual $\leq{}$ constraint
- primal free variable => dual $={}$ constraint

> what about $\geq$ and $=$ primal constraints?

supposed

$$
\begin{align*}
\max{3x_1+4x_2+8x_3}\\
\text{s.t. }x_1+2x_2+3x_3\geq{6}\\
2x_1+x_2+2x_3={4}\\
x_1\geq{0}\\
x_2\leq{0}\\
x_3 \text{urs.}
\end{align*}
$$

to obtain

$$
y_1(x_1+2x_2+3x_3)+y_2(2x_1+x_2+2x_3)\leq{6y_1+4y_2}
$$

$y_1\leq{0}$ and $y_2$ is now free/urs.

> note that the arrangement is different from the above, this helps to reach
> the conclusion.

thus the final piece of formulating dual LP

- primal $\geq{}$ constraint => dual $\geq{0}$ variable 
- primal $\leq{}$ constraint => dual $\leq{0}$ variable
- primal $=$ constraint => dual free variable 

> qns is the property of duality that is the one implies every max problem has
> an equivalent min LP pair?

## general rule

matrix representation of a standard form LP

$$
\begin{align*}
\max{c^{T}x}\\
\text{s.t. }Ax=b\\
x\geq{0}
\end{align*}
$$

and

$$
\begin{align*}
\min{y^{T}b}\\
\text{s.t. }y^{T}A\geq{c^{T}}
\end{align*}
$$

> note standard from LP only equal sign in constraint and all decision
> variables are non negatives

for a minimization LP, its dual LP is to maximize the lower bound. the rules
for direction of variables and constraints are reversed.

## Duality Theorems

duality besied provides upper/lower bound for primal problem it also help to
understand what are the condition and properties that a primal/dual solution
might have. the subsequent discussion will be using standard LP for
simplification and other primal-dual pairs have the same property demonstrated.

$$
\begin{align*}
\max{c^{T}x}\\
\text{s.t. }Ax=b\\
x\geq{0}
\end{align*}
\iff
\begin{align*}
\max{y^{T}b}\\
\text{s.t. }y^{T}A=c^{T}\\
\end{align*}
$$

> note equal sign in primal constraint results in unrestricted sign variables
> in dual LP formulation

### Property 1: Weak duality

the dual LP provides an upper bound of the primal (max) LP. formally, for any
LP defined if $x$ and $y$ are primal and dual feasible then $c^{T}x\leq{y^{T}b}$

proof: as long as they are primal and dual feasible,

$$
\begin{align*}
c^{T}x & \leq{y^{T}Ax}(x\geq{0},y^{T}A\geq{c^{T}})\\
       & \leq{y^{T}b}(Ax=b)
\end{align*}
$$

this helps to understand the sufficiency of optimality, i.e. having sufficient
condition for optimal solutions. if $\bar{x},\bar{y}$ are primal and dual
solutions are feasible and $c^{T}\hat{x}=\hat{y}^{T}b$ (objective value are
identical) then $\bar{x},\bar{y}$ are primal and dual optimal.

proof: for all dual feasible $y$ implies $c^{T}\bar{x}\leq{y^{T}b}$ by weak
duality. given that $c^{T}\bar{x}=\bar{y}^{T}b$ we have $\bar{y}^{T}b\leq{y}^{T}b$
for all dual feasible $y$, which implies $\bar{y}$ is optimal. same for $\bar{x}$.

given a primal feasible solution $\bar{x}$ if a dual feasible solution can be
find such that their objective values are identical, $\bar{x}$ is optimal.

> think for a max problem the dual is finding a lower bound and primal an
> upper bound if the objective value matches i.e. no other solution is better
> than either primal or dual, it is confirmed to be optimal.

implication: as long as the dual LP is proven feasible, the primal is feasible,
no need to resolve from primal's reduce costs pov.

### dual optimal solution

if primal LP is solved, dual optimal solution is also found i.e. if $\bar{x}$
is primal optimal with basis $B$ then $\bar{y}^{T}=c^{T}_{B}A^{-1}_B$ is dual
optimal.

proof: if $B$ is optimal the reduced costs $c_B^{T}A^{-1}_{B}A_N-c^{T}_N\geq{0}$
as $c^{T}_{B}=c_B^{T}A^{-1}_{B}A_B$ we have,

$$
\begin{align*}
\hat{y}^{T}A & =c_B^{T}A_B^{-1}A\\
             & =c_B^TA_B^{-1}[A_B\quad A_N]\\
             & \geq{[c_B^{T}\quad c_N^{T}]}\\
             & =c^{T}
\end{align*}
$$

> line 3 above can be derived from the reduced costs equation by moving $c_N^{T}$
> to RHS. the equation above should yield the conclusion $\bar{y}^{T}A\geq{c}^{T}$

thus $\bar{y}$ is dual feasible. as $\bar{y}^{T}b=c_B^{-1}b=c_B^{T}\bar{x}_B=c^{T}\bar{x}$,
$\bar{x}$ and $\bar{y}$ have same objective valueand thus both optimal.

### strong duality