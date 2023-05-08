# overview

to address a few questions

- how a solver solve a problem?
- why IP is more complex than LP
- why linearization is important
- what are the alternatives to MS excel solver
- what are the alternatives if no solver is good enough

> algorithms, advanced solvers and heuristic.

## algorithms

- simplex
- branch and bound
- gradient descent and newton method

### heuristic

when scale is large and complexity is high, it is possible that solver is not
enough. algorithms have to be designed to solve problem at hand - these
algorithms are known as heuristic algorithms. it finds a near optimal solution
in reasonable amount of time.

## Prerequisite - Linear Algebra

solving SoLE; using gaussian elimination to solve $Ax=b$; using gauss-jordan
elimination to solve $A^{-1}$ and figuring out linear dependence and
independence.

### the column view

$$
x\begin{bmatrix}1\\3\end{bmatrix}+y\begin{bmatrix}-2\\1\end{bmatrix}=
\begin{bmatrix}5\\4\end{bmatrix}
$$

imagine two lines from origin connected to the xy vectors, by expanding and
shrinking the lines, attemps to form the result vector on the RHS of equation.

### the row view

from the given $n$ dimension space, find a $n-1$ dimension plane/hyperplane's
intersection

### singularity

a SoLE is known as singular if there is no unique solution; in row view, it is
achieved by not having exacgtly one (hyper)planes intersection; in column view,
it implies the $n$ dimensional vectors do not span a complete $n$ dimensional
space (recall basic property of unit vector spanning entire subspace).

### gaussian elimination

core idea of GE is to reduce the "flexibility" in equation i.e. by finding an
equation within the SoLE that has only one variable to "solve" for that
variable. the resulting upper triangle (first variable in each row is known as
pivot) allows to figure out each variables's coefficient.

a singular system can either have no solution of infinite solutions. this is
determined by checking if the variables are consistent i.e. coefficent *
variable is actually same for the "tied" equations.

computational complexity is $O(n^3), \sum_{i=1}^{n}(n-i)^2-(n-1)=\frac{n(n+1)(2n+1)}{6}$ 

### inversing matrix

must be a square matrix and nonsingular and the computational complexity is
also $O(n^3)$

### linear dependence

linear dependent if pivot is less then $n$