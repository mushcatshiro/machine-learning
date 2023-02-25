# section summary

clopening: a company assigns an employee to work late at night to close a store
and get up early to prepare for opening the store. worker hates it

## quiz

### q1

You may produce seven products by consuming three materials. The unit sales
price and material consumption of each product are listed in Table 1. For each
day, the supply of these three materials are limited. The supply limits are
listed in Table 2. For each day, you need to determine the production quantity
for each product. Formulate a linear integer program that generates a feasible
production plan to maximize the total profit (which is also the total revenue,
as there is no cost in this problem). Then write a computer program (e.g.,
using MS Excel solver) to solve this instance and obtain an optimal plan. Do
not set the production quantities to be integer; leave them fractional. After
you find an optimal solution and its objective value, write down the integer
part of the objective value as your solution (i.e., rounding down that value
to the closest integer)

| Product | Price | Material 1 | Material 2 | Material 3 |
|---------|-------|------------|------------|------------|
| 1 | 100 | 0 | 3 | 10 |
| 2 | 120 | 5 | 10 | 10 |
| 3 | 135 | 5 | 3 | 9 |
| 4 | 90 | 4 | 6 | 3 |
| 5 | 125 | 8 | 2 | 8 |
| 6 | 110 | 5 | 2 | 10 |
| 7 | 105 | 3 | 2 | 7 |

table 1

| material | supply limit |
|----------|--------------|
| 1 | 100 |
| 2 | 150 |
| 3 | 200 |

table 2

### q2

Consider a set of data $(x_i,y_i),i=1,...,n$ provided in table 3. if we believe
$x_i$ and $y_i$ has linear relationship, we may apply simple linear regression
to fit these data to a linear model. more precisely, we try to find $\alpha$
and $\beta$ such that the straight line $y=\alpha+\beta{x}$ minimuzes the sum
of squared errors for all the data points. While almost all statistical
software and packages provide tools for one to solve the above linear
regression problem, we may also consider it as a nonlinear program and solve it
with an optimization solver (e.g., MS Excel solver). For the data provided in
the following table, solve the linear regression problem. Write down the
optimal $\beta$ ou find by rounding it to the first digit after the decimal
point (e.g., 9.011, 1.229, and 3.245 should be rounded to 9.01, 1.23, and 3.25
to be written down)

$$
\min_{\alpha,\beta}\sum_{i=1}^{n}[y_i-(\alpha+\beta{x_i})]^2
$$

| x | y |
|---|---|
| 38 | 137 |
| 56 | 201 |
| 50 | 152 |
| 52 | 107 |
| 37 | 150 |
| 60 | 173 |
| 67 | 194 |
| 54 | 166 |
| 59 | 154 |
| 43 | 137 |
| 30 | 38 |
| 53 | 193 |
| 59 | 154 |
| 40 | 175 |
| 65 | 247 |

## reference

- O'Neal, C. (2017) Weapons of Math Descturction: How Big Data Increases
  Inequality and Threatens Democracy