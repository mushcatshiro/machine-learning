# linear algebra

## scalar operation

- $c = a + b$
- $c = a*b$
- $c = sin(a)$
- $|a| = \begin{cases} a, &\text{if}\ a>0\\ -a, &\text{otherwise}\end{cases}$
- $|a+b| \leq{|a|+|b|}$
- $|a\cdot{b}| = |a|\cdot{|b|}$

## vector operation

- $c = a + b, \text{where } c_i=a_i+b_i$
- $c = \alpha\cdot{b}, \text{where } c_i = \alpha{b_i}$
- $c = sin(a), \text{where } c_i=sin(a_i)$
- $||a||_2 = \Bigr[\sum\limits^{m}_{i=1}{a^{2}_{i}}\Bigr]^{1/2}, ||a||\geq{0}\forall{a}$
- $||a+b|| \leq{||a||+||b||}$
- $||a\cdot{b}|| = |a|\cdot{||b||}$

## matrix operation

- $c = a + b, \text{where } C_{ij}=A_{ij}+B_{ij}$
- $c = \alpha\cdot{b}, \text{where } C_{ij} = \alpha{B_{ij}}$
- $c = sin(a), \text{where } C_{ij}=sin(A_{ij})$

### matrix multiplication

$$
A_{32} = B_{34}\cdot{C_{42}}
$$

geometrically matrix multiplication is trying to distort the given vector space.
in matrix operation, distances calculation is also known as "norm". there are
lots of norm but most commonly used are L0, L1, L2 and Linf norm. in deep learning
there isn't much use of positive definite matrix, which is the opposite to statistical
learning. eigenvalues are those which post matrix multiplication changes in magnitude
but not direction.