[TOC]

# bayesian statistics

frequentist and bayesian.

the frequentist approach

- observe the random generated data
- made assumption on the generating process (gaussian, smooth density, linear regression and etc)
- the generating process was associated to some object of interest (parameter, density etc)
- this object was **unknown but fixed** and to find it we either estimated it or test a hypothesis on it

the bayesian approach

- observe the random generated data
- under some assumption (parametric distribution) this process is associated with some fixed object
- we have a prior belief about it
- using the data we want to update that belief and transform it into a posterior belief

for each possible parameters $\theta \in H$ we will encounter different spaces including $\R, [0, 1], [0, \infty]$ etc. for each space we will have some "tools" for it.

take $[0, 1]$ as an example where **Beta distribution** is as follows,
$$
X \sim \beta(a, b) \left\{ 
\begin{array}{ll}
\text{ if density } f(x) = cx^{a-1}(1 - x)^{b-1} & x \in [0, 1]\\
0 &  x \notin (0, 1)
\end{array}
\right. \\
\text{where c is a normalizing constant}
$$
the two parameters allows us to form a significant amount of distribution (unimodal, mixers exists as another topic where multiple factors exists and aggregates into the dataset). for the two parameter, one is call scale another is shape.

___

question to think

1. do we assume that each new observation has equal weight when we updating the belief? i.e. 2nd observation will update much significantly than the 100001 observation, or it is still equal weight?

