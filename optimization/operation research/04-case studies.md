# Case Studies

allocating just enough people for call center. holiday arrangements, rest in
between working days/hours and starting/ending time. to put it simply, its a
personnel scheduling problem.

> research are usually presented in the following sequence. background/
> motivation, research objective, problem statement, model formulation and
> results.

## CSR scheduling

Customer Service Represntatives to take turns serving customers. to meet the
desired service level, historical incoming calls is analyzed to calculate the
ideal number of CSR in all time period. service level can be defined as
response rate. with the historical data it is still challenging given,

- work hours should be continuous in each day
- some people are needed or not allowed in some period, e.g. at least one
  manager per shift, pregnant women should not work at night
- fairness e.g. one CSR should only work at night at most once a week (OT)

it is an integer programming problem i.e. selection problem.

what exactly is the decision to make?

- letting each CSR know when to have days off
- each work day of each CSR, when to start, end work and taking breaks
- shifts are presets with a special shift 0 that indicates day off

basically it is to assign one shift to teach CSR for each day. once the CSR
needed for a time period is known, the number of CSR on duty on that period is
calculated to minimize the shortage at that period $\max{\{A-B, 0\}}$ where $A$
is the number of CSR needed for time period and $B$ is the number of CSR on
duty.

### hard constraints

- each CSR should be assigned to exactly one shift per day
- a CSR may require a specific shift on a certain day e.g. choosing day off in
  advance
- each CSR should be assigned to at most one night shift per week
- at most 3 CSR may have day off on each monday
- a CSR can at most take 2 night shift on Thursday in a month
- at least one manager in every night shift
- CSR with more than 2 years of experience in the call center should account
  for more than 50% of the total on-duty CSR in a night shift

### soft constraints

i.e. can be violated if needed but hopefully are satisfied

- fairness among periods i.e. similar extra on-duty CSR for every period
  rather than having 5 extra CSR in shift 1 and only 1 extra CSR in shift 2, it
  is better to have 3 both
- fairness among CSRs i.e. similar number of night shift for every CSR rather
  than letting CSR A having 4 night shift and CSR B having 2, it is better to
  have 3 each

## formulating the model

form a mathematical model from the hard and soft contraints or conceptual model
. and from mathematical model, computational models can be obtained.

let $I,K,K,T$ be the sets of CSRs, days in which the call center is open,
shifts and periods in a day. let $i\in{I}$ denote the $i$th CSR, $j\in{J}$
denote the $j$th day, $k\in{K}$ denote the $k$th shift and $t\in{T}$ denote the
$t$th period. $i,k,k,t$ are the incides. the core decision variable,

$$
x_{ijk}=\begin{cases}
1 & \text{if CSR i is assigned to shift k in day j}\\
0 & \text{otherwise}
\end{cases},i\in{I},j\in{J},k\in{K}
$$

one derived decision variable

$$
y_{jt}=\text{the number of CSR shortage in period t of day j},t\in{T},j\in{J}
$$

objective function should include major objective (minimizing total lack of
CSRs) and two soft constraints (fairness). let $w_1$ be the maximum number of
extra on-duty CSRs among all period and $w_2$ be the maximum number of night
shift among all CSRs. a **weighted average** form is often deployed

$$
\min P_0\sum_{j\in{J}}\sum_{t\in{T}}y_{jt}+P_1w_1+P_2w_2
$$

where $P_0,P_1,P_2$ are weights to be determined by the manager.

### constraints

1. for each CSR and each day, they can only be assigned to one shift
2. there should be some constraint to calculate total shortage (linking
  $x_{ijk}$ to $y_{jy}$)
3. there should be some constraints to calculate the maximum number of extra
  on-duty CSR among periods (linking $x_{ijk}$ to $w_1$)
4. there should be some constraints to calculate the maximum number of night
  shifts among CSR (linking $x_{ijk}$ to $w_2$)

for 1,

$$
\sum_{k\in{K}x_{ijk}}=1 \quad \forall{i}\in{I},j\in{J}
$$

for 2,

$$
y_{jt}\geq{D_{jt}}-\sum_{k\in{K}}{A_{kt}}\sum_{i\in{I}}{x_{ijk}} \quad \forall{j}\in{J},t\in{T}\\
y_{jt}\geq{0} \quad \forall{j}\in{J},t\in{T}\\
$$

$D_{jt}$ is the number of CSRs needed in period $t$ of day $j$
$A_{kt}$ is $1$ is shift $k$ convers period $t$ or $0$ otherwise

> note that it is actually a linearization of $\min\sum\sum\max{\{A-B,0\}}$
> using the trick mentioned in NLP

for 3,

$$
w_1\geq{\sum_{k\in{K}}A_{kt}\sum_{i\in{I}}x_{ijk}-D_{jt}}\quad\forall{j}\in{J},t\in{T}\\
w_1\geq{0}\quad\forall{j}\in{J},t\in{T}
$$

for 4,

$$
w_2\geq{\sum_{j\in{J}}\sum_{k\in{K^N}}x_{ijk}}\quad\forall{i}\in{I}\\
w_2\geq{0}\quad\forall{i}\in{I}
$$

let $K^N$ be the set of night shifts

> for all statements are tedious however necessary to indicate boundaries else
> the formulations IS wrong.

results are satisfactory. from the model learnt operational decisions and
stratagic decisions can be made by having the following questions answered,

- whether to recruit more CSRs
- impact of adjusting shift setting
- impact of adjusting policies

## quiz

### q1

the CSR scheduling problem discussed in this week exhibits which of the
following characteristics?

- [x] allocation
- [x] selection
- [ ] balancing
- [ ] sequencing
- [ ] all of the above

### q2

Which of the following statements best describes the main decision to make in
the CSR scheduling problem discussed in this week?

- [ ] For each CSR, determine her/his number of days off in the coming month
- [ ] For each day, determine the number of CSRs that should go to work
- [ ] For each day, determine the number of CSRs in each shift
- [x] For each CSR for each day, determine her/his shift
- [ ] None of the above

### q3

What is the difference between a hard constraint and a soft constraint?

- [ ] A hard constraint can be formulated with mathematical expressions while a
      soft one cannot
- [ ] A hard constraint does not have a decision variable in it while a soft
      one does
- [x] A hard constraint must be satisfied while a soft one is not
- [ ] None of the above
- [ ] All of the above

### q4

Recall that in the CSR scheduling problem discussed in this week, we want to
minimize the maximum number of night shifts among all CSRs is considered.
Suppose that now instead we want to minimize the maximum number of night-shift
CSRs among all work days (let $w_3$ be such a number ), which of the following
are the correct set of constraints to calculate the number?

- [x] $w_3\geq{0},w_3\geq{\sum_{i\in{I}}\sum_{k\in{K^N}}}x_{ijk}\forall{j\in{J}}$
- [ ] $w_3\geq{0},w_3\geq{\sum_{i\in{I}}\sum_{k\in{K^N}}}\sum_{i\in{I}}x_{ijk}$
- [ ] $w_3\geq{0},w_3\geq{\sum_{i\in{I}}\sum_{k\in{K^N}}}x_{ijk}\forall{k\in{k^N}}$
- [ ] $w_3\geq{0},w_3\geq{\sum_{k\in{K^N}}}x_{ijk}\forall{j\in{J}},i\in{I}$
- [ ] None of the above

### q5

The technique for solving the CSR scheduling problem discussed in this week is
the most appropriate for solving which of the following problem?

- [ ] Determining the daily production quantities of all products for a
      manufacturer
- [ ] Determining the allocation of investment budget among stocks
- [ ] Determining the salary for each employee
- [x] Determining how to assign multiple jobs to multiple workers in multiple
      days
- [ ]Determining the restaurant for the dating in the coming Christmas eve