# nonlinear programming

e.g price to demand is not a linear function and should be addressed with a
nonlinear approach instead. other examples including inventory i.e. tradeoff
between order cost and inventory cost and portfolio optimization i.e.
involvement of considering risk (standard deviation). notice that tradeoff is
a emphasized concept here because tradeoffs can only be modeled in a nonlinear
way.

## examples

below are a few examples to illustrate nonlinear problems.

example of pricing a product. a product has a unit cost $c$ and a unit retail
price $p$. the demand is denote as $p: D(p)=a-bp$ where . to formulate the
problem of maximizing price by

- parameters: $a,b,c\gt{0}$
- decision variables: $p$
- constraint: $p\geq{0}$

thus,

$$
\begin{align*}
\max_{p} (p-c)(a-bp)\\
s.t. \quad p\geq{0}\\
\end{align*}
$$

> why not $p\geq{c}$

example of folding a piece of paper. given a piece of square paper whose edge
length is $a$. by cutting down four small squares on the edge of length $d$ and
fold the paper to create a container that maximizes the volume of container.

$$
\max_{d\in{\{0,a/2\}}}{(a-2d)^2}d
$$

example of locating a hospital. in a country there is $n$ cities and each of
them is located at $(x_i,y_i)$. to locate a hospital at location $(x,y)$ to
minimize the average euclidean distance from the cities to the hospital.

$$
\min_{x,y} \sum_{i=1}^{n}{\sqrt{(x-x_i)^2+(y-y_i)^2}}
$$

in general NLP can be formulated as

$$
\begin{align*}
\min_{x\in{\mathbb{R}^n}}{f(x)}\\
s.t. \quad g_i(x)\leq{b_i} \quad \forall{i}=1,...m\\
\end{align*}
$$

- $x\in{\mathbb{R}^n}$ are the $n$ decision variables
- there are $m$ constraints
- its LP if $f$ and $g_i$ are all linear in $x$ and nonlinear if at least one isnt

its easy to formulat but challenging to optimize.

## the Economic Odering Quantity problem

a company needs a $x$ parts of component per year and there is a unit price.
the part's consume rate is consistent throughout the year and there is a
ordering cost incurred regardless of the order quantity. there is also a
holding cost per month per unit. goal it so minimize overall costs. such
problem as the following assumptions

- demand is deterministic and having a constant rate
- regardless of ordering quantity having a fixed ordering cost
- no shortage is allowed
- zero lead time
- inventory holding cost is constant

to formulate the problem the following notations is used.

- parameters
  - $D$ annual damand (units)
  - $K$ unit ordering costs
  - $h$ unit holding costs per year
  - $p$ unit purchasing cost
- decision variable
  - $q$ order quantity per order

> to understand how inventory level affect the decision i.e. because no lead
> time order is always placed when inventory level is zero and the inventory
> level vs time graph will look like a repeated "N" shape pattern and an
> average of $q/2$ inventory level is maintained.

$$
\min_{q\geq{0}} (KD)/q+pD+(hq)/2
$$

where $(KD)/q$ is the annual ordering costs, $(hq)/2$ is the annual holding
costs and $pD$ is the annual purchasing costs. note that $pD$ is a constant, a
more relavant objective function would be,

$$
TC(q)=(KD)/q+(hq)/2
$$

## the porfolio optimization problem

to invest in a set of stocks with current price and future expected price a LP
is formulated as such,

$$
\begin{align*}
\max 55x_1+50x_2+20x_3\\
s.t. \quad 50x_1+40x_2+25x_3\leq{100,000}\\
x_1,x_2,x_3\geq{0}
\end{align*}
$$

however it is not that simple if risk is also considered. Nobel Ecomonic Prize
Laureates in 1990 (Markowitz and Sharpe) suggested that the total revenue is
random and the larget the variance of the total revenue the higher the risk. a
better problem is to minimize the total variance while ensuring certain
expected revenue.

### variance

let $X$ be a random variable, $\mu$ be its expected value, $x_i$ be the $i$th
possible realization and $Pr(X=x_i)$ be the probability for $x_i$ to occur,
variance of $X$ is

$$
Var(X)=\sum_{i=1}^{n}{Pr(X=x_1)(x_i-\mu)^2}
$$

in general $Var(bX)=b^2Var(x)$. thus let variance of buying each stock be
$100,1600,100$ respectively; $R$ is the minimum required expected revenue. the
NLP formulation is

$$
\begin{align*}
\min 100x_1^2+1600x_2^2+100x_3^2\\
s.t. \quad 50x_1+40x_2+25x_3\leq{100,000}\\
55x_1+50x_2+20x_3\geq{R}\\
x_i\geq{0} \quad \forall{i}=1,...,3
\end{align*}
$$

given different values of $R$, different optimal portfolios is obtained. a
generalized formulation would be

$$
\begin{align*}
\min \sum_{i=1}^{n}{\sigma_i^2x_i^2}\\
s.t. \quad \sum_{i=1}^{n}{p_ix_i}\leq{B}\\
\sum_{i=1}^{n}{\mu_ix_i}\geq{R}\\
x_i\geq{0} \quad \forall{i}=1,...,3
\end{align*}
$$

knowing that the stock price are typically correlated thus the objective
function can be further improved by introducing covariance
$\min \sum_{i=1}^{n}{\sigma_i^2x_i^2}+2\sum_{i=1}^{n}\sum_{j=i+1}^{n}{\sigma_{ij}x_ix_j}$

## linearizing

### an absolute value function

the problem: to allocate $1000 to two person in a **fair** way with fair
defined as the smaller the difference two ammount the fairer the allocation is.
the obvious answer is to give each person $500 but how to formulate a linear
program to solve this problem?

$$
\begin{align*}
\min x_1-x_2\\
s.t. \quad x_1+x_2=1000\\
x_i\geq{0} \quad \forall{i}=1,2
\end{align*}
$$

the formulation above is wrong as the best solution is to have $x_2=1000$. the
correct formulation should be

$$
\begin{align*}
\min |x_1-x_2|\\
s.t. \quad x_1+x_2=1000\\
x_i\geq{0} \quad \forall{i}=1,2
\end{align*}
$$

which $|\cdot|$ is a nonlinear function. to linearize, replace target function
with $w=|x_1-x_2|$ and argues that $w\geq{|x_1-x_2|}$ does not change the
program because if $w\gt{|x_1-x_2|}$ is true, the target function have not
achieve its goal. in other words, $w\gt{|x_1-x_2|}$ is not optimal. the only
thing changed is the feasible region.

$$
\begin{align*}
\min w\\
s.t. \quad x_1+x_2=1000\\
w\geq{|x_1-x_2|}\\
x_i\geq{0} \quad \forall{i}=1,2\\
\end{align*}
$$

from $|x_1-x_2|$, it also imply that $\max{\{x_2-x_1,x_1-x_2\}}$ and thus
$w\geq{\{x_2-x_1,x_1-x_2\}}$ therefore,

$$
\begin{align*}
\min w\\
s.t. \quad x_1+x_2=1000\\
w\geq{x_2-x_1}\\
w\geq{x_1-x_2}\\
x_i\geq{0} \quad \forall{i}=1,2\\
\end{align*}
$$

then to reduce the three decision variable $(w,x_1,x_2)$ to one, from $x_2=1000-x_1$

$$
\begin{align*}
\min w\\
s.t. \quad w\geq{1000-2x_1}\\
w\geq{2x_1-1000}\\
x_1\geq{0}\\
\end{align*}
$$

### max_min functions

1. when a **maximum** function is at the **smaller** side of the equality i.e.
$y\geq{max_{i=1,...,n}{x_i}}\implies{y\geq{x_1} \quad \forall{i}=1,...,n}$
2. when a **minimum** funtion is at the **larger** side of the equality

however the technique does not apply to,

- a maximum function at the larger side $y\leq{\max{\{\cdot\}}}$
- a minimum function at the smaller side
- a maximum or minimum function in an equality function

> to validate condition 3 the addition of function if its correct?

it is possible to minimize a maximum function or vice versa.

$$
\min\max{\{x_1,x_2\}}\implies{\min{w}\quad s.t.\quad w\geq{x_1}\And w\geq{x_2}}
$$

> corollary: an absolute function is just a maximum function thus minimizing an
> absolute function can be minimized; an absolute function at the smaller side
> of an inequality can be linearized.

### revisiting the hospital location problem

in a country with $n$ cities that locates at $(x_i,y_i)$ and the goal is to
minimize average **manhattan** distance from cities to hospital,

$$
\min_{x,y}{\sum_{i=1}^{n}{(|x-x_i|+|y-y_i|)}}
$$

is linearized to

$$
\begin{align*}
\min{\sum_{i=1}^{n}{u_i+v_i}}\\
s.t. \quad u_i\geq{x-x_i},u_i\geq{x_i-x} \quad \forall{i}=1,...,n\\
\quad v_i\geq{y-y_i},v_i\geq{y_i-y} \quad \forall{i}=1,...,n\\
\end{align*}
$$

### linearizing products of decision variables

product of decision variables e.g. $x^2$ or $xy$. they can be linearized if the
two variables are a combination of binary and continuous variable or both are
binary.

#### scenario 1A

a company manufactures and sells two product with limited resources. each
product requires a setup cost and manufacturing both results in some reduction
in setup cost

$$
\begin{align*}
\max 10x_1+12x_2-20z_1-25z_2+10z1z2\\
s.t. \quad 2x_1+x_2\leq{6}\\
x_1+2x_2\leq{8}\\
x_1\leq{2z_1}\\
x_2\leq{4z_1}\\
x_1,x_2\geq{0}\\
z_1,z_2\in{\{0,1\}}
\end{align*}
$$

by introducing $w=z_1z_2$ it appears in a maximization of objective function
thus suffice to introduce $w\leq{z_1}$ and $w\leq{z_2}$ to make $w=z_1z_2$.

$$
\begin{align*}
\max 10x_1+12x_2-20z_1-25z_2+10w\\
s.t. \quad ...\\
w\leq{z_1}\\
w\leq{z_2}\\
w\in{\{0,1\}}
\end{align*}
$$

#### scenario 1B

a company manufactures and sells two product with limited resources. each
product requires a setup cost and manufacturing both results in some addition 
in setup cost

$$
\begin{align*}
\max 10x_1+12x_2-20z_1-25z_2-10z1z2\\
s.t. \quad 2x_1+x_2\leq{6}\\
x_1+2x_2\leq{8}\\
x_1\leq{2z_1}\\
x_2\leq{4z_1}\\
x_1,x_2\geq{0}\\
z_1,z_2\in{\{0,1\}}
\end{align*}
$$

by introducing $w=z_1z_2$ it appears in a minimizing of objective function
thus suffice to introduce $w\leq{z_1}$ and $w\leq{z_2}$ does not make $w=z_1z_2$.
instead use $w\geq{z_1+z_2-1}$

> using $w\leq{z_1}$ and $w\leq{z_2}$ does not impose any bound to $w$ and it
> still engourages $w$ in the objective function to be 0 despite both $z_1,z_2$
> are $0$. $w\geq{z_1+z_2-1}$ is essentially providing lower bound.

$$
\begin{align*}
\max 10x_1+12x_2-20z_1-25z_2-10w\\
s.t. \quad ...\\
w\geq{z_1+z_2-1}\\
w\in{\{0,1\}}
\end{align*}
$$

#### scenario 1C

product term appears in constraint? it matters if it appears at the larger or
smaller side. if it appears at the larger side, it may be linearized as if it
appears in a maximization objective function as the product term should be $1$
only if both terms are $1$.

$$
\begin{align*}
\max ...\\
s.t. \quad x\leq{5z_1z_2}\\
x\geq{0}\\
z_1,z_2\in{\{0,1\}}
\end{align*}
$$

into

$$
\begin{align*}
\max ...\\
s.t. \quad x\leq{5w}\\
x\geq{0}\\
z_1,z_2\in{\{0,1\}}\\
w\leq{z_1},w\leq{z_2}\\
w\in{\{0,1\}}
\end{align*}
$$

#### scenario 1D

if the product term is at the smaller side, it may be linearized as if it
appears in a minimization objective function as the product term cannot be $1$
if either term is $0$.

$$
\begin{align*}
\max ...\\
s.t. \quad x\geq{5z_1z_2}\\
x\geq{0}\\
z_1,z_2\in{\{0,1\}}
\end{align*}
$$

into

$$
\begin{align*}
\max ...\\
s.t. \quad x\geq{5w}\\
x\geq{0}\\
z_1,z_2\in{\{0,1\}}\\
w\geq{z_1+z_2-1}\\
w\in{\{0,1\}}
\end{align*}
$$

#### scenario 2A

a company that manufactures and sells two products with two limited resources.
starting the business requires fixed payment to local goverment. if the payment
is not made, the products cannot be sold regardless of the production quantity.

$$
\begin{align*}
\max (10x_1+12x_2)z-15z\\
s.t. \quad 2x_1+x_2\leq{6}\\
x_1+2x_2\leq{8}\\
x_1,x_2\geq{0}\\
z\in{\{0,1\}}
\end{align*}
$$

it is not possible to make $w_1=x_1z$ and $w_2=x_2z$ as for $w_1$ it can not
impose $w_1\leq{x_1}$ and $w_1\leq{z}$. the latter is too tight and we should
remove the contraint when $z=1$ or in other words, the RHS should contain a
value that is an upper bound of $x_1$.

$$
\begin{align*}
\max 10w_1z+12w_2z-15z\\
s.t. ...\\
w_1\leq{x_1},w_1\leq{3z}\\
w_2\leq{x_2},w_2\leq{4z}\\
w_1,w_2\in{\{0,1\}}
\end{align*}
$$

> $w_1\leq{x_1},w_1\leq{3z}$ obtained from $2x_1+x_2\leq{6}$ where making the
> upper bound as the value of $x_1$

#### scenario 2B

a company may run two production process to fulfull the demands for two
products if it accepts an order.

$$
\begin{align*}
\max 50z-(10x_1+12x_2)z\\
s.t. \quad 2x_1+x_2\geq{6}\\
x_1+2x_2\geq{8}\\
x_1,x_2\geq{0}\\
z\in{0,1}\\
\end{align*}
$$

by introducing $w_1=x_1z$ and $w_2=x_2z$ now $w$ appears in a minimization
objective function and $w$ should be lower bounded rather than upper bounded.
using $w_1\geq{x_1-8(1-z)}$ and  $w_2\geq{x_2-6(1-z)}$ therefore,

$$
\begin{align*}
\max 50z-10w_1+12w_2\\
s.t. ...\\
w_1\geq{x_1-8(1-z)}\\
w_2\geq{x_2-6(1-z)}\\
w_1,w_2\in{0,1}\\
\end{align*}
$$

> thinking problem: why $8$ and $6$? in fact it can be set as some arbitrary
> large number, but its better to be precise.

#### scenario 2C

when a product term appears at the larger side of constraint, it may be
linearized as if it appears in a maximization objective function and should be
upper bounded.

$$
\begin{align*}
\max ...\\
s.t. \quad x_1z\geq{5x_2}\\
x_1+x_2\leq{10}\\
x_1,x_2\geq{0}\\
z\in{\{0,1\}}
\end{align*}
$$

into

$$
\begin{align*}
\max ...\\
s.t. \quad w\geq{5x_2}\\
x_1+x_2\leq{10}\\
x_1,x_2\geq{0}\\
z\in{\{0,1\}}\\
w\leq{x_1},w\leq{10z}\\
w\geq{0}
\end{align*}
$$

#### scenario 2D

when a product term appears at the smaller side of constraint, it may be
linearized as if it appears in a minimization objective function and should be
lower bounded.

$$
\begin{align*}
\max ...\\
s.t. \quad x_1z\leq{5x_2}\\
x_1+x_2\leq{10}\\
x_1,x_2\geq{0}\\
z\in{\{0,1\}}
\end{align*}
$$

into

$$
\begin{align*}
\max ...\\
s.t. \quad w\leq{5x_2}\\
x_2\leq{10}\\
x_1,x_2\geq{0}\\
z\in{\{0,1\}}\\
w\geq{x_1-10(1-z)}\\
w\geq{0}
\end{align*}
$$

### why linearization

it fasten the solving process given linear programs are easy and IP are doable
while NLP and NILP are hard or very hard. it is important in practice for OR to
be able to estimate the solvability of a formulation.

## quiz

### q1

A retailer is importing a product from an overseas supplier. If there are $q$
units on the market, the unit price of the product will be  $a−bq$ dollars
(this is called the market clearing price. The unit procurement cost of the
product is $c$. The retailer wants to determine a procurement quantity that
maximizes its profit. In an NLP that maximizes the retailer's profit, which of
the following is the correct objective function?

- [ ] $\max q(qa-b-c)$
- [x] $\max q(a-bq-c)$
- [ ] $\max q(a-b-cq)$
- [ ] $\max (q-c)(a-bq)$
- [ ] none of the above

### q2

to linearize the following NLP, what should be replacing the first constraint?

$$
\begin{align*}
\max 5x_1+2x_2\\
s.t. \quad max{\{x_1,12\}}\leq{\min{\{16,x_1+2x_2\}}}\\
x_1+4x_2\leq{20}\\
x_1\geq{0},x_2\geq{0}
\end{align*}
$$

- [x] $x_1\leq{16},12\leq{x_1+2x_2}$
- [ ] $x_1\leq{16},12\geq{x_1+2x_2}$
- [ ] $x_1\geq{16},12\leq{x_1+2x_2}$
- [ ] $x_1\geq{16},12\geq{x_1+2x_2}$
- [ ] none of the above

### q3

The IEDO county is trying to determine where to placeone fire station. The
locations of the county's sixmajor towns are given in the following coordinates
measured in kilometers. City 1: (20,20); city 2: (60,10); city 3: (40,30);
city 4: (40,60); city 5: (30,0); city 6: (10,70). City 1 has in average 20
fires per year. For cities 2 to 6, the average numbers of fires are 30, 50, 20,
15, and 25, respectively. The county wants to minimizes the average "distance
to travel". Because in the county roads all run in either an east-west or a
north-south direction, we use Manhattan distances rather than Euclidean
distances. For example, if the fire station were located at (50,40) and a fire
occurred at city 4, the "distance to travel" is $|50-40|+|40-60|=30$km. we
define the following parameters,

- $X_i$ x-coordinate of location for city $i,i=1,...,6$
- $Y_i$ y-coordinate of location for city $i,i=1,...,6$
- $N_i$ average number of fire for city $i,i=1,...,6$

let $x,y$ be the location of hospital a mathematical program that solves the
problem is

$$
\min{\sum_{i=1}^{6}{N_i(|x-X_1|+|y-Y_i|)}}
$$

check the correct statments

- [ ] this is a linear program
- [x] this is a nonlinear program that can be linearized
- [ ] this is a nonlinear program that cannot be linearized
- [x] this program has two decision variables
- [ ] this program has twelve decision variables

### q4

We want to invest $1,000 to five stocks. For stock $i$, the current price is 
$p_i$​ per share, expected future price is $\mu_i$ per share, and variance is 
$\sigma_{i}^{2}$ per share. The objective is to maximize the total expected
revenue minus one half of the variance of the revenue. Let $x_i$​ be the shares
of stock $i$ we buy. Which of the following is the correct objective function?

- [ ] $\max{\sum_{i=1}^{5}{\mu_i x_i}-\frac{1}{2}\sum_{i=1}^{5}{\sigma_{i}^{2}x_i}}$
- [x] $\max{\sum_{i=1}^{5}{\mu_i x_i}-\frac{1}{2}\sum_{i=1}^{5}{\sigma_{i}^{2}x_{i}^{2}}}$
- [ ] $\max{\sum_{i=1}^{5}{\mu_i x_i}}-\frac{1}{2} (\sum_{i=1}^{5}{\sigma_{i}x_i})^{2}$
- [ ] $\max{\sum_{i=1}^{5}{\mu_i x_i}}-(\frac{1}{2}\sum_{i=1}^{5}{\sigma_{i}x_i})^{2}$
- [ ] none of the above

### q5

Consider the following nonlinear program

$$
\begin{align*}
\max 10x_1+12x_2-20z_1-25z_2-10z_1z_2\\
s.t. \quad 2x_1+x_2\leq{6}\\
x_1+2x_2\leq{8}\\
x_1\leq{3z_1}\\
x_2\leq{4z_2}\\
x_1,x_2\geq{0}\\
z_1,z_2\in{\{0,1\}}
\end{align*}
$$

to linearize the program above let $w=z_1z_2$ after replacing $z1z2$ in the
objective function which of the following constraint(s) should be added into
the program above?

- [ ] $w\leq{z_1}$ and $w\leq{z_2}$
- [ ] $w\leq{z_1+z_2}$
- [ ] $w\geq{z_1}$ and $w\geq{z_2}$
- [ ] $w\leq{z_1+z_2}$
- [x] none of the above