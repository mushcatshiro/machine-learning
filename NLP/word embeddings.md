# word embeddings

word embeddings in short is to represent words as numbers, or more specifically vectors. by representing words, it includes the semantics to ensure better inference and this is heavily dependent on the strategy that converts string to vector.

## simple strategies

### One hot encodings and variation

by counting distinct words, we generate a $(n, 1)$ shaped vector with zeros, and for each word we assign the value $1$ to the corresponding row $n$. such approach is simple with a few drawbacks

- all words are equidistance/semantics are not captured
- highly sparsed matrix

to address the drawbacks, one could instead assign words to an index number and turn a sentence into an array of dense vector. still, there are drawbacks

- should happy be assigned to 1, sad to 2 and joy to 1000, does it mean that happy is much closely related to sad than joy?
  - feature weight cannot be learnt properly/meaningfully
  - the randomness of index assignment

## a better approach

by defining $n$ dimension, 8 to 1024 or higher based on the dataset size but generally positive correlation, we algorithmically learn and represent relationship between words. the result is a dense lookup table (matrix) known as word embedding. such approach is based on the distributional hypothesis, which words appearing in similar context are related to each other semantically. in summary word embeddings are a representation of the **semantics** of a word.

### pytorch n-gram

```python
CONTEXT_SIZE = 2
EMBEDDING_DIM = 10
test_sentence = "".split()
# we should tokenize the input, but we will ignore that for now
# build a list of tuples.
# Each tuple is ([ word_i-CONTEXT_SIZE, ..., word_i-1 ], target word)
ngrams = [
    (
        [test_sentence[i - j - 1] for j in range(CONTEXT_SIZE)],
        test_sentence[i]
    )
    for i in range(CONTEXT_SIZE, len(test_sentence))
]

vocab = set(test_sentence)
word_to_ix = {word: i for i, word in enumerate(vocab)}


class NGramLanguageModeler(nn.Module):

    def __init__(self, vocab_size, embedding_dim, context_size):
        super(NGramLanguageModeler, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, vocab_size)

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((1, -1))
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        log_probs = F.log_softmax(out, dim=1)
        return log_probs

losses = []
loss_function = nn.NLLLoss()
model = NGramLanguageModeler(len(vocab), EMBEDDING_DIM, CONTEXT_SIZE)
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(10):
    total_loss = 0
    for context, target in ngrams:

        # Step 1. Prepare the inputs to be passed to the model (i.e, turn the words
        # into integer indices and wrap them in tensors)
        context_idxs = torch.tensor([word_to_ix[w] for w in context], dtype=torch.long)

        # Step 2. Recall that torch *accumulates* gradients. Before passing in a
        # new instance, you need to zero out the gradients from the old
        # instance
        model.zero_grad()

        # Step 3. Run the forward pass, getting log probabilities over next
        # words
        log_probs = model(context_idxs)

        # Step 4. Compute your loss function. (Again, Torch wants the target
        # word wrapped in a tensor)
        loss = loss_function(log_probs, torch.tensor([word_to_ix[target]], dtype=torch.long))

        # Step 5. Do the backward pass and update the gradient
        loss.backward()
        optimizer.step()

        # Get the Python number from a 1-element Tensor by calling tensor.item()
        total_loss += loss.item()
    losses.append(total_loss)

# To get the embedding of a particular word, e.g. "beauty"
print(model.embeddings.weight[word_to_ix["beauty"]])
```

$\subset$

## referrences

- [Tensorflow Word Embeddings](https://www.tensorflow.org/text/guide/word_embeddings#representing_text_as_numbers)
- [Pytorch Word Embeddings](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)