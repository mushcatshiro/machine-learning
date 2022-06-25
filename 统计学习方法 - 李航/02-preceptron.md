[TOC]

# Perceptrons

novikoff theorem proof

$$
{\|\hat{w}_{opt}\|} = 1
$$

norm of optimal plane (or hyperplane that separates the dataset), we can image the sample space shrink to unit vector, or radius equal to 1. this actually applies to not just w hat, to x its also the same
$$
x_i' = \frac{x_i}  {max_j \|{x_j}\| }
$$

$$
\gamma \
\text{is margin}
$$

margin is the points that are closest to the hyperplane. its common thing in ML to look at. large margin is desired and we have a set of large margin classifier / algorithm.
$$
w^T \cdot w_{opt} = w^T \cdot w_{opt} + \gamma
$$
