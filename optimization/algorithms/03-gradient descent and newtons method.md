# gradient descent and newton's method

in nonlinear setting, the solution does not necessarily lies on the
intersections/edges/boundaries. it can be anywhere between the search space. by
doing derivation and check on all possible direction, and chooses the direction
that aligns to the objective i.e. -ve direction for a minimize problem. GD is
a first order approximation. in cases where first order approach that does not
work, newton's method (idea) can be used. it is a second order approximation.

> note that to obtain any numerical solution numerical algorithms is needed.
> so what is a numerical algorithm?

NLP algorithms are typically

- iterative: move from a point to another and uses the current point as the
             starting point
- repetitive: same steps are executed in each iteration
- greedy: seeks some best thing achievable in each iteration
- approximation: relying on first or second order approximation of the original
                 program

limitations of NLP algorithms

- might fail to converge
  - convergence may happen if further iteration does not improve significantly
- might be trapped in local optimum
  - starting point matters
- requires domain to be continuous and connected
  - NLIP is even harder to solve

## gradient and hessians

both GD and newton's method are able to solve **unconstrained** NLP problem
i.e. $\min_{x\in{\mathbb{R}^n}}f(x)$. in such setting, all multivariate 
functions are assumed to be differentiable.

for a function $f:\mathbb{R}^{n}\rarr{\mathbb{R}}$ collecting its first- and
second-order partial derivatives generates its,

gradient
$$
\triangledown{f(x)}= \begin{bmatrix}
  \frac{\partial{f(x)}}{\partial{x_1}}\\
  ...\\
  \frac{\partial{f(x)}}{\partial{x_n}}\\
\end{bmatrix}
$$

and hessian
$$
\triangledown^{2}f(x)=\begin{bmatrix}
  \frac{\partial^{2}{f(x)}}{\partial{x_1}^{2}}&&\dots&\frac{\partial^{2}{f(x)}}{\partial{x_1}\partial{x_n}}\\
  ...\\
  \frac{\partial^{2}{f(x)}}{\partial{x_n}\partial{x_1}}&&\dots&\frac{\partial^{2}{f(x)}}{\partial^{2}{x_n}}\\
\end{bmatrix}
$$

> hessian in the course is assumed to be symmetric

## gradient descent

given a objective function $f(x)=x_0^2+x_1^2$ its gradient is a $n$ dimensional
vector see gradient example from the previous section and $n=2$`. gradient is
an increasing **direction**. for a twice-differentiable function $f(x)$ its
gradient is an increasing function i.e. $f(x+a\triangledown{f(x)})>f(x)$ for 
all $a>0$ that are small enough i.e. if $a>>0$ it might not be true.

proof:

$$
\lim_{a\rarr{0}}\frac{f(x+a\triangledown{f(x)})-f(x)}{a}=\triangledown{f(x)}^T\triangledown{f(x)}>0\\
\implies f(x+a\triangledown{f(x)})\gt{f(x)}
$$

if $a>0$ and $a$ is small enough.


> to avoid confusion gradient is an increasing function thus in GD move in the
> opposite direction instead.

> gradient is the fastest increasing direction.

thus given a solution $X$, it is updated to $x-a\triangledown{f(x)}$ for some
$a$ known as step size and stop when gradient of current solution is $0$.

### on choosing $a$

given $f(x)=x_0^2+x_1^2$, supposed starting at $(1, 1)$ the gradient is
$(2x_0, 2x_1)$. if $a=1/2$ it converges after one iteration but if $a=1$ it
will never converge.

by looking at the largest improvement i.e. along the improving direction
$-\triangledown{f(x)}$, solve $\min_{a\geq{0}}f(x-a\triangledown{f(x)})$ to see
how far to each the lowest point along this direction.

the algorithm
- step 0: choose a starting point and a precision parameter $\epsilon>0$
- step k+1:
  - find $\triangledown{f(x^k)}$
  - solve $a_k=\argmin_{a\geq{0}}{f(x^k-a\triangledown{f(x^k)})}$
  - update the current solution to $x^{k+1}=x^k-a\triangledown{f(x^k)}$
  - if $||\triangledown{f(x^{k+1})}||\lt\epsilon$ stop; otherwise increment $k$ and
    continue

> solving $a_k=\argmin_{a\geq{0}}{f(x^k-a\triangledown{f(x^k)})}$ is
> straightforward by replacing the current $X$ values into the function i.e.
> and $f(x_1(a), \dots, x_n(a))$, obtain a function that only has one variable
> $a$. knowing it is an upward curvature problem thus first order solution is
> optimal.

> the last step is finding a norm (assuming is L2) i.e.
> $||x||=\sqrt{(x_1^2+\dots+x_n^2)}$ when $x\in{\mathbb{R}^n}$

looking at the search route $x^0, \dots, x^n$ and obtaining $x^*$ the algorithm
search only one direction in each iteration. its always zigzag-ing because it
always move at maximum possible distance in one dorection everytime.

## newton's method

first-order method is intuitive however might be too slow. second-order might
be able to speed up and it relies on hessian to update the solution. let
$f:\mathbb{R}\rarr{\mathbb{R}}$ be differentiable, find $\bar{x}$ such that it
satisfy $f{\bar{x}}=0$.

for any $x^k$ let $f_L(x)=f(x^k)+f'(x^k)(x-x^k)$ to be the linear approximation
of $f$ at $x^k$. this is the tangent line of $f$ at $x^k$ or the first order
taylor expansion of $f$ at $x^k$. moving from $x^k$ to $x^{k+1}$ by setting
$f_L(x^{k+1})=f(x^k)+f'(x^k)(x^{k+1}-x^k)=0$. keep iterating until
$|x^{k+1}-x^k|\lt{\epsilon}$ or $|f(x^k)|\lt{\epsilon}$ for some predetermined
$\epsilon\gt{0}$

now let $f$ be twice differentiable and find $\bar{x}$ such that $f'(\bar{x})$=0$
. for any $x^k$ let $f'_L(x)=f'(x^k)+f''(x^k)(x-x^k)$ to be the linear
approximation of $f'$ at $x^k$. approach $\bar{x}$ and moving $x^k$ to $x^{k+1}$
by setting $f'_L(x^{k+1})=f'(x^k)+f''(x^k)(x^{k+1}-x^k)=0$. keep iterating
until $|x^{k+1}-x^k|\lt{\epsilon}$ or $f'(x^k)|\lt{\epsilon}$ for some
predetermined $\epsilon\gt{0}$

> note $f'(\bar{x})$ does not guarantee a global minimum, need to also proof
> that $f$ is convex

### another interpretation (newton's method for solving single variate NLP)

previous interpretation is from a linear perspective i.e. $f$'s linear
approximation with $f_L(x) and $f'_L(x)$. now from a quadratic approximation
point of view,

$$
f_Q(x)=f(x^k)+f'(x^k)(x-x^k)+\frac{1}{2}f''(x^k)(x-x^k)^2
$$

this can be viewed as the second order of taylar expansion of $f$ at $x^k$.
moving from $x^k$ to $x^(k+1)$ by moving to the global minimum of the quadratic
approximation,

$$
x^{(k+1)}=\argmin_{x\in{\mathbb{R}}}{f(x^k)+f'(x^k)(x-x^k)+\frac{1}{2}f''(x^k)(x-x^k)^2}
$$

by differentiating the above objective function w.r.t. to x yields,

$$
f'(x^k)+f''(x^k)(x^{(k+1)}-x^k)=0 \lrArr x^{(k+1)}=x^k-\frac{f'(x^k)}{f''(x^k)}
$$

the above might not be easy to interpret. what happens is let $x^k$ be some
value then rewrite the objective function. from that second order function,
find $x^(k+1)$ with its first order derivative when it is $0$. alternatively,

$$
\begin{align*}
\frac{d}{d\Delta{x}}(f(x)+f'(x)\Delta{x}+\frac{1}{2}f''(x)\Delta{x}^2)=0\\
f'(x)+f''(x)\Delta{x}=0\\
\end{align*}
$$

### newton's method for multivariate NLP

let $f:\mathbb{R}^n\rightarrow{\mathbb{R}}$ be twice differentiable. for any
$x^k$ let the quadratic approximation of $f$ at $x^k$ where $f'$ is now $\triangledown{x^k}$
(Hessian). moving from $x^k$ to $x^(k+1)$ towards the global minimum of the
quadratic approximation $\triangledown{f(x^k)}+\triangledown^2{f(x^k)}(x^{(k+1)}-x^k)$
i.e. $x^{(k+1)}=x^k-[\triangledown^2{f(x^k)}]^{-1}\triangledown{f(x^k)}$

> Hessian is a matrix thus $-1$ implies inverse

### summary for newton's method

- does not have step size issue
- potentially faster
  - able to find the optimal solution in one iteration for quadratic function
- potentially failed to converge

generally using GD or NM one must consider the following issues

- convergence guarantee
- convergence speed
- differentiability
  - sub-gradient
- constrained optimization

> note that GD and NM are interior point methods.