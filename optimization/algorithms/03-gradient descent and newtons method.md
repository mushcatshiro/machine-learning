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
vector see gradient example from the previous section and $n=2$. gradient is
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

> step solving $a_k=\argmin_{a\geq{0}}{f(x^k-a\triangledown{f(x^k)})}$ can be
> replaced by other approximations method because the solving $\argmin{f(x)}$
> of the original equation might be too difficult. currently deep learning
> frameworks uses learning rate to control (to validate). alternatively can
> checkout line search.

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
$|x^{k+1}-x^k|\lt{\epsilon}$ or $f(x^k)|\lt{\epsilon}$ for some predetermined
$\epsilon\gt{0}$

now let $f$ be twice differentiable and find $\bar{x}$ such that $f'(\bar{x})$=0$
. for any $x^k$ let $f'_L(x)=f'(x^k)+f''(x^k)(x-x^k)$ to be the linear
approximation of $f'$ at $x^k$. approach $\bar{x}$ and moving $x^k$ to $x^{k+1}$
by setting $f'_L(x^{k+1})=f'(x^k)+f''(x^k)(x^{k+1}-x^k)=0$. keep iterating
until $|x^{k+1}-x^k|\lt{\epsilon}$ or $f'(x^k)|\lt{\epsilon}$ for some
predetermined $\epsilon\gt{0}$

> note $f'(\bar{x})$ does not guarantee a global minimum, need to also proof
> that $f$ is convex

### another interpretation

> both gradient descent and netwon's method searches for a local optimum,
> however if newton's method converge it is also the global optimum.

> know that for iterative methods like GD and NM, the step size (how far to move
> away from the existing location) and direction are the core components.
