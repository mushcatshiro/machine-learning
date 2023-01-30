# data manipulation

the most commonly used data structure in machine learning is tensors, including
scalar, vector, and matrices.

## working with pytorch's basic data structure

```python
import torch

x = torch.arange(12)
x
# tensor([0, 1, 2, ...])
x.shape
# number of elements; output as scalar
x.numel()
x.reshape(3, 4)
# [[0, 1, 2, 3], [4, ...], ...]
# bewteen tensors +,-,*,/,** are all element wise operations
y = torch.zeros(3, 4)
x == y
# returns a tensor of t/f values
# its possible to add between tensor of same dimension but different shape
# with broadcasting mechanism

before = id(y)
y = y + x
id(y) == before
# false
before = id(y)
y[:] += x
id(y) == before
# true
```

## data preprocessing

for string type/categorical type missing data we can do the following to get a
extra column named "ColName_nan". conceptually its creating ohe.

```python
inputs = pd.get_dummies(inputs, dummy_na=True)
```