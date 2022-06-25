[TOC]

# tricks

## overfitting the first batch (pytorch)

if we couldn't overfit a single batch, we might need to rethink if its worth to continue subsequent training

````python
train_loader = DataLoader(dataset=test_dataset, batch=batch_size, shuffle=True)
data, targets = next(iter(train_loader))

# train and check if we can overfit
````

## toggle train / eval (pytorch)

we could get worse performance without switching eval mode, usually its because our model contains dropout layer or batch norm

````python
model.eval()
check_accuracy()
# we could then use model.train() to continue training
````

## zero_grad (pytorch)

````python
for batch_idx, (data, targets) in enumerate(training_date):
    data = data.to(device=device)
    targets = targets.to(device=device)
    data = data.reshape(data.shape[0], -1)
    
    # forward
    scores = model(data)
    loss = criterion(scores, targets)
    
    # backward
    optimizer.zero_grad()
    loss.backward()
    
    # gradient descent or adam step
    optimizer.step()
````

## softmax & cross entropy loss

cross entropy loss is essentially softmax + negative log likely hood. if we use both together its softmax on softmax which is not something desirable

## bias with batch norm

to check on documentation

## using view as premute (pytorch)

````python
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
print(x.view(3, 2))
print(x.permute(1, 0))

# tensor[[1, 2, 3], [4, 5, 6]]
# tensor[[1, 2], [3, 4], [5, 6]] <- not what we want (transpose)
# tensor[[1, 4], [2, 5], [3, 6]] <- what we want
````

## bad data augmentation

data augmentation is good but not all are good, eg mnist number dataset if we flipped the number 9 vertically and horizontally, then it should become 6 which doesn't match to the target output.

## not shuffling the data

always shuffle your data, unless we are dealing with time series data where order is important?

```python
train_data = DataLoader("parameters", shuffle=True)
```

## not normalizing the data

unless we are using batch normalization else it would suffer from some performance impact.

## not clipping gradients in (RNN and its variations)