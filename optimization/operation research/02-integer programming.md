# integer programming

things are discrete here. and the problem here can be intuitively think of as
selection or assignment problem i.e. telling some entity what to do exactly
on a specific time.

- setup cost (whole units, and in scenarios where first unit is expensive and the followings are marginal)
- facility location
- machine scheduling
- vehicle routing

IP requires the variables to be only integer values. IP essentially is
referring to linear IP, NLIP is a separate discussion. here we visit the
personnel scheduling problem with IP. using LP to solve for scenario where
staff number is small can be a problem when rounding is applied. when the scale
is large i.e. staff of thousands, rounding up or down does not significanty
affect productivity, however 3.8 and 4.2 kind of values does. another example
is on route selection. think the problem as a graph, give each edge a binary
variable 1 if included else 0. constraints are required to ensure edges are
forming a route. in this case using LP also dont make sense as the value has to
be 1 or 0.

## Integer programming formulation

### knapsack problem

| item | 1 | 2 | 3 | 4 |
|------|---|---|---|---|
| value | 16 | 22 | 12 | 8 |
| weight | 5 | 7 | 4 | 3 |

the knapsack capacity is 10kg and the formulation is,

$$
\begin{align*}
\max 16x_1+22x_2+12x_3+8x_4\\
s.t. \quad 5x_1+7x_2+4x_3+3x_4\leq{10}\\
x_i\in{\{0,1\}} \quad \forall{i}=1,...,4
\end{align*}
$$

IP allow implementation of selection rules.

#### At least or at most

variables: at least one among item 2, 3, 4

$$
x_2+x_3+x_4\geq{1}
$$

variables: at most two among item 1, 3, 4

$$
x_1+x_3+x_4\leq{2}
$$

constraints: satisfying one of two constraints $g_1(x)\leq{b_1}\text{ and }g_2(x)\leq{b2}$
by defining,

$$
z=\begin{cases}
0 & \text{if } g_1(x)\leq{b_1} \text{ is satisfied,}\\
1 & \text{if } g_2(x)\leq{b_2} \text{ is satisfied}
\end{cases}
$$

with $M_1$ being an upper bound of each LHS the following two constraints
implement what is needed,

$$
g_1(x)-b_1\leq{M_1z}\\
g_2(x)-b_2\leq{M_2(1-z)}
$$

by introducing $M_i$ and having $g_1(x)-b_1\leq{M_1z}$ satisfied, $g_2(x)$ is
flexible.

constraints: at least two of the three constraints

$$
z_i=\begin{cases}
1 & \text{if } g_i(x)\leq{b_i} \text{ is satisfied,}\\
0 & \text{if } g_i(x)\leq{b_i} \text{ may be satisfied}
\end{cases}
$$

with $M_i$ being an upper bound of each LHS the following two constraints
implement what is needed,

$$
g_i(x)-b_i\leq{M_i(1-z)} \quad \forall{i}=1,2,3\\
z_1+z_2+z_3\geq{2}
$$

#### Or

select item 2 or 3

$$
x_2+x_3\geq{1}
$$

select item 2; otherwise item 3 and 4 together

$$
2x_2+x_3+x_4\geq{2}
$$

> question: why isnt leq?

> question: why condition are not "two-way"?

#### if-else

if item 2 is selected; select item 3

$$
x_2\leq{x_3}
$$

if item 1 is selected; do not select item 3 and 4

$$
2(1-x_1)\geq{x_3+x_4}
$$

### Fixed-charge constraints

there exists $n$ factories, 1 market and 1 product. $K_i$ is the capacity of
factory $i$. $C_i$ is the unit production cost at factory $i$. $D$ is the
demand of the product. goal is to minimize cost. however there is also a setup
cost at factory $i$: $S_i$, which is a one off payment as long as any **positive**
amount of products is produced.

let the decision variables be,

- $x_i$ production quantity at factory $i=1,...,n$
- $y_i=\begin{cases}1&\text{if product is produced at factory }i\\0\end{cases}$

objective function:

$$
\min \sum_{i=1}^{n}{C_ix_i}+\sum_{i=1}^{n}{S_iy_i}
$$

capacity limitation:

$$
x_i\leq{K_i} \quad \forall{i}=i,...,n
$$

demand fulfillment:

$$
\sum_{i=1}^{n}{x_i}\geq{D}
$$

noticed that there is no connection between $x$ and $y$ thus,

$$
x_i\leq{K_iy_i} \quad \forall{i}=i,...,n
$$

- if $x_i\gt{0}$, $y_i$ cannot be $0$
- if $x_i=0$, $y_i$ can be $0$ or $1$ however solver will always return 0 because this is a minimize function

above is known as a fixed-charge constraint, the general form is $x\leq{My}$
where both $x$ and $y$ are decision variables and $y$ is determined by $x$, $M$
is an upper bound of $x$. when $x$ is binary $x\leq{y}$ is sufficient.

> selecting upper bound should handled with care. in the example capacity was
> chosen, given if y = 1 it does not reduce the feasible region. alternatively
> if there is no capacity limitation, D is used as no reason to produce beyond
> demand.

binary and nonnegative constraints:

$$
x_i\geq{0},y_i\in{\{0,1\}}\quad \forall{i}=1,...,n
$$

## Facility Location

to answer question e.g. "where to build the facilities?" or "where to locate
the scarce resource?". to describe it generally, it solves the problem on how
to allocate a subset of entities from a set of finite entities with a limited
amount of resource. in general there are some demand nodes and some potential
locations. facility location problem are typically categoriezd based on their
objective functions. three facility location problem is covered,

- set covering problems: build a minumum no. of facilities to cover all demands
- maximum covering problems: build a given no. of facilities to cover as many demand as possible
- fixed charge location problems: find a balance between benefit of covering demands and cost of building

### set covering

consider a set of demands $I$ and a set of locations $J$. the traveling time
between demand $i$ and location $j$ is $d_{ij}\gt{0},i\in{I},j\in{J}$. a
service level of $s\gt{0}$ is given. demand $i$ is said to be covered by
location $j$ if $d_{ij}\lt{s}$. how to allocate as few facilities as possible
for the demand $I$?

![set-covering](./set-covering.PNG)

> note that there can be a $d_{ij}$ between 1 adn 4 however it is greater than
> $s$ thus it is not showed/simplified

$d_{ij}$ is not critical in the sense that as long as it satisfy $s$ it is
qualified. thus using $a_{ij}=1$ to represent if $d_{ij}\lt{s}$ or $0$
otherwise, $i\in{I},j\in{J}$. let $x_j=1$ if a facility is build on location $j$
or $0$ otherwise.

$$
\begin{align*}
\min \sum_{j\in{J}}{x_j}\\
s.t. \quad \sum_{j\in{J}}{a_{ij}x_j}\geq{1} \quad \forall{i}\in{I}\\
x_j\in{0,1} \quad \forall{j}\in{J}
\end{align*}
$$

> shouldnt it be $\sum_{j\in{J}}{a_{ij}x_j}\geq{I}$ or total demand?

the weighted version $\min \sum_{j\in{J}}{w_jx_j}$. weight can be e.g. cost and
etc.

### maximum covering

similar to set covering with additional constraint to only build **at most** $p\in{\mathbb{N}}$
facilities. in addition to the decision variable $x_j$, a new decision variable
$y_i=1$ is introduced if demand $i\in{I}$ is covered by any facility or $0$
otherwise.

$$
\begin{align*}
\max \sum_{i\in{I}}{y_i}\\
s.t. \quad \sum_{j\in{J}}{a_{ij}x_j}\geq{y_i} \quad \forall{i}\in{I}\\
\sum_{j\in{J}}{x_j}\leq{p}\\
x_j\in{\{0,1\}} \quad \forall{j}\in{J}\\
y_i\in{\{0,1\}} \quad \forall{i}\in{I}
\end{align*}
$$

### fixed charge location

consider a set of demands $I$ and a set of locations $J$. at demand $i$, the
demands size is $h_i\gt{0}$. the unit shipping cost from location $j$ to demand
$i$ is $d_{ij}\gt{0}$. the fixed construction cost at location $j$ is $f_j\gt{0}$
. how to allocate some facilities to minimize the total shipping and
construction costs? there are two sub questions:

1. where to allocate the facilities
2. how to assign them to customers

$x_j=1$ if facility is build at location $j\in{J}$ or $0$ otherwise. $y_{ij}=1$
if demand $i\in{I}$ is served by facility at location $j\in{J}$ or $0$
otherwise.

$$
\begin{align*}
\min \sum_{i\in{I}}\sum_{j\in{J}}{h_id_{ij}y_{ij}}+\sum_{j\in{J}}{f_jx_j}\\
s.t. \quad y_{ij}\leq{x_j} \quad \forall{i}\in{I},\forall{j}\in{J}\\
\sum_{j\in{J}}{y_{ij}}=1 \quad \forall{i}\in{I}\\
x_j\in{\{0,1\}} \quad \forall{j}\in{J}\\
y_i\in{\{0,1\}} \quad \forall{i}\in{I}
\end{align*}
$$

what is shown is a **uncapacitated** scenario. a facility can server any amount
of demand. if there is a capacity constraint of $K_j\gt{0}$ it is added as such
$\sum_{i\in{I}}{h_iy_{ij}}\leq{K_j} \quad \forall{j}\in{J}$. capacitated
scenario is known as CFL and the uncapacitated scenario is known as UFL.

### getting around with the problems type

set covering is where it is required to take care of all parties/stakeholders.
max covering is where budgets are limited. fixed charge location is when
service costs depends on distance.

## machine scheduling

jobs to be assigned to some entity. consider a factory producing one product
for $n$ customers. in a serial production scenario one job is run at a time 
with each has a due date, how to schedule $n$ jobs to minimize total delayed
jobs? splitting jobs is not helpful and there is always $n!$ ways to sequence $n$
jobs. there can be a few patterns,

- single machine serial production
- multiple machine
  - parallel production: only one processing step
  - flow shop problem: few steps and each machine can run one processing step
  - job shop problem: multiple steps/machine is allowed to mix and match

- job splitting
  - preemptive problem: process can be interupted and resumed
  - non-preemptive problem

- performance measurement
  - makespan (time all job completed)
  - (weighted) total completion time
  - (weighted) number of delayed jobs
  - (weighted) total lateness
  - (weighted) total tardiness
  - etc.

> if a job completed before due its considered -ve lateness but 0 tardiness

### completion time minimization

consider scheduling $n$ jobs on a single machine. job $j\in{J}={\{1,2,...,n\}}$
has processing time $p_j$. different schedules give these jobs different
completion times. the completion time of job $j$ is denoted as $x_j$. the
machine can process only on job at a time. goal is to schedule all the jobs to
minimize the total completion time $\sum_{j\in{J}}{x_j}$

## quick-note

- the lego production line problem i.e. how many parts to produce to minimize duplicated pieces?
- past 50 years stock price, what is an optimal set of stocks to pick (a slider to see how things has changed)