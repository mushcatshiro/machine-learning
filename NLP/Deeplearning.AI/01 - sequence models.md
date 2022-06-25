[TOC]

# Sequence model

examples of sequence model

- speech recognition
- music generation
- sentiment classification
- DNA sequence analysis
- machine translation
- video activity recognition 
- name entity recognition

the input and output could have vary length, and some output may not be a sequence

## notation

x: Harry Potter and Hermione Granger invented a new spell.

(NER) y: 1, 1, 0, 1, 1, 0, 0, 0,  (not the best representation, sometimes we want it to be 0-11 form where indexes where it starts and ends)
$$
x^{<1>}, x^{<2>}...\, x^{<t>}...\,: y^{<1>}, y^{<2>}...\\
$$

where
$$
T_x = \text{total length of input length}
\\T_y = \text{total length of output length}
\\ x^{(i)<t>}: t^{th}\text{element of }i^{th} \text{ training example}
\\ T^{(i)}_x: i^{th} \text{ input sequence length}
$$


## represent words

vocabulary or dictionary
$$
\begin{bmatrix}
a\\
aaron\\
...\\
and\\
...\\
zulu
\end{bmatrix}\\
$$

dictionary size is usually larger, around 1 billion. we could use one hot encoding for each words, eg.
$$
a = \begin{bmatrix}
1\\
0\\
...\\
0
\end{bmatrix}
$$
for words not in dictionary we can create a token 'UNK', more on this later.

## RNN model

standard NN model doesn't work well due to

- inconsistency between input and output length (padding might help, but see 2nd point)
- doesn't share features learned across different positions of text
  - eg. the word harry in first sentence is x^(1) and its learned it importance but doesn't translate well into the next sentence where harry is not the first word
  - or in short, we want features learnt in one part to generalize well into other parts
- In CNN we have seen better representation will reduce number of parameter in model, this idea also applies to sequence model

![image-20201107152122224](E:\MDbook\NLP\Deeplearning.AI\image-20201107152122224.png)

problem with vanilla RNN is we can only look sequence comes before the current word, there are times that we need to know the words that comes next to make good prediction, a good solution would be a bi-directional RNN

- **he said, "teddy** roosevelt was a good president" (teddy is a name)
- **he said, "teddy** bear are on sale" (teddy is not a name)

also the activation value
$$
W_{ax}, W_{aa}, W_{ya}
$$
are shared throughout the model

### forward propagation

$$
a^{<0>} = \vec{0}\\
a^{<1>} = g(W_{aa} * a^{<0>} + W_{ax} * x^{<1>} + b_a)\\
a^{<t>} = g(W_{aa} * a^{<t-1>} + W_{ax} * x^{<t>} + b_a)\\
\hat{y}^{<1>} = g'(W_{ya} * a^{<1>} + b_y)\\
\hat{y}^{<t>} = g'(W_{ya} * a^{<t>} + b_y)\\
$$

where
$$
g(): relu\,or\,tanh\\
g'(): sigmoid\,or\,softmax
$$


we could simplify the generalize form into
$$
a^{<t>} = g(W_{a} [ a^{<t-1>} , x^{<t>}] + b_a)\\
\hat{y}^{<t>} = g'(W_{y} * a^{<t>} + b_y)\\
$$
where
$$
W_{a} = [W_{aa} | W_{ax}]
$$
and
$$
[ a^{<t-1>} , x^{<t>}] =
\begin{bmatrix}
a^{<t-1>}\\
---\\
x^{<t>}
\end{bmatrix}
$$

note
$$
a^{<t>}
$$
is feed to next RNN and also to softmax to get
$$
\hat{y}^{<t>}
$$

### back propagation through time

cross entropy loss (for each x^t)
$$
l^{<t>}(\hat{y}^{<t>}, {y}^{<t>}) = -{y}^{<t>}\log{\hat{y}^{<t>}} - (1-{y}^{<t>})\log(1-\hat{y}^{<t>})
$$
overall loss
$$
L^{<t>}(\hat{y}, {y}) = \sum_{t=1}^{T_x} (l^{<t>}(\hat{y}^{<t>}, {y}^{<t>}))
$$

## different types of RNNs

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

- one to one
- one to many eg. music generation [Generating Music using an LSTM Network](https://arxiv.org/ftp/arxiv/papers/1804/1804.07300.pdf)
- many to many (Tx = Ty)
- many to many (Tx != Ty) eg. encoder-decoder architecture
- many to one eg. sentiment analysis

![image-20201107161931472](E:\MDbook\NLP\Deeplearning.AI\image-20201107161931472.png)

## language model and sequence generation

what is language modelling? eg. for a speech recognition system,

> The apple and pair salad
>
> The apple and pear salad

the 2nd sentence is more likely to be the correct sentence and for a model to tell us its the 2nd sentence is by using a language model which tells what the probability is of either of these two sentences.

thus a language model is to input a sentence, represents it and estimates the probability of that particular sequence of words.

we start with a large corpus of text as training date, tokenize it, add a <EOS> token. (we need to decide if we want to tokenize all punctuation) if we are using the 10k most common english words as token, we may not be able to tokenize some rare words eg. Mau (a breed of cat), we can replace it with <UNK> instead.

### a RNN model

we initiate
$$
a^{<0>},x^{<1>} = \vec{0}
$$
compute a^1 by making a softmax prediction of 
$$
\hat{y}^{<1>}
$$
where for each
$$
P(corpus)
$$


where within the 10k token / words (plus UNK and EOS) which word is the word most likely to be the first word.

for 2nd RNN we provide the correct
$$
y^{<1>} = x^{<2>}
$$
as input, and predict
$$
\hat{y}^{<2>}
$$
where
$$
P(corpus | firstword)
$$
the cost function (softmax lost function)
$$
l^{<t>}(\hat{y}^{<t>}, {y}^{<t>}) = -{y}^{<t>}\log{\hat{y}^{<t>}}\\
L = \sum{l^{<t>}(\hat{y}^{<t>}, {y}^{<t>})}
$$

## Sampling novel sequences

for the language model we provide the correct word for each input x, but for sampling we instead feed the output of previous RNN as input. to stop we could either wait it output the <EOS> token or we could limit sampling words. to deal with <UNK> we could just simply resample.

for a character-level language model we could instead change the vocab from 10K common english words to a-z plus space / punctuation, numbers, capital character. also we need to train with characters instead of words. with this we won't have the problem of unknown character. but our sequence will be much longer causing it to lose long range dependencies, and gets harder to train.

## vanishing gradients with RNN

for sentence we could have long dependencies eg.

> the cat which already ate x, y, z, was full
>
> the cats which already ate x, y, z, were full

singular and plural early in the sentence will affect the word choices later in the sentence. for long sentence, vanilla RNN is not able to capture the relation due to vanishing gradient during front and back propagation (harder to influence something early).

### exploding gradient

its easier to detect with lots of NaN, and can be easily solved with gradient clipping

## Gated Recurrent Unit (GRU)

to solve vanishing gradient problem.
$$
c = memory\,cell\\
c^{<t>} = a^{<t>} \text{(for GRU, in LSTM its different)}\\
\tilde{c}^{<t>} = \tanh{(W_c[c^{<t-1>}, x^{<t>}]+b_c)}\\
\Gamma_u = \sigma {(W_u[c^{<t-1>}, x^{<t>}]+b_u)}\\
c^{<t>} = \Gamma_u * \tilde{c}^{<t>} + (1 - \Gamma_u) * c^{<t-1>}\\
\text{* here is element-wise multiplication due to } c^{<t>},\tilde{c}^{<t>}, \Gamma_u \text{ are all same dimension}
$$
update gate uses sigmoid which most of the time the expected output value is 0 or 1. Gamma u can be approximate to zero thus avoiding vanishing gradient problem.

### a full GRU

consist of both update gate and relevance gate. 
$$
\tilde{c}^{<t>} = \tanh{(W_c[\Gamma_r * c^{<t-1>}, x^{<t>}]+b_c)}\\
\Gamma_u = \sigma {(W_u[c^{<t-1>}, x^{<t>}]+b_u)}\\
\Gamma_r = \sigma {(W_r[c^{<t-1>}, x^{<t>}]+b_r)}\\
c^{<t>} = \Gamma_u * \tilde{c}^{<t>} + (1 - \Gamma_u) * c^{<t-1>}\\
$$

## LSTM

![image-20201107233431695](E:\MDbook\NLP\Deeplearning.AI\image-20201107233431695.png)
$$
\tilde{c}^{<t>} = \tanh{(W_c[a^{<t-1>}, x^{<t>}]+b_c)}\\
\Gamma_u = \sigma {(W_u[a^{<t-1>}, x^{<t>}]+b_u)}\\
\Gamma_f = \sigma {(W_f[a^{<t-1>}, x^{<t>}]+b_f)}\\
\Gamma_o = \sigma {(W_o[a^{<t-1>}, x^{<t>}]+b_o)}\\
c^{<t>} = \Gamma_u * \tilde{c}^{<t>} + \Gamma_f * c^{<t-1>}\\
a^{<t>} = \Gamma_o * \tanh{(c^{<t>})}
$$
a common modification would be adding an additional c^<t-1> to Gamma O, which is also known as a peephole connection.

### LSTM or GRU

GRU is easier to train, can go deeper (less gates) / scale well, but there is no one superior option, it depends on the problem.

## Bidirectional RNN

instead of having a single chain of RNNs we will have two, one traverses from 0 to Tx and another from Tx to 0. thus we have two forward propagation before making predictions of each yhat
$$
\hat{y}^{<t>} = g'(W_{y} [a^{<t>}_{lr}, a^{<t>}_{rl}] + b_y)\\
$$


- its essentially using information from future and past to predict now
- it could potentially predict something in between / the middle
- it requires to compute entire sequence before making predictions, some BRNN can help to address this problem for real time applications

## deep RNN

by stacking RNN on top of each other its less seen and usually 3 layers is considered deep.

general formula
$$
a^{[l]<t>}
$$
an example,
$$
\text{eg. }a^{[2]<3>} = g(W_{a}^{[2]} [ a^{[2]<2>} , x^{[1]<3>}] + b_a)\\
$$
l is used to represent layer number similar to previous FC network. we could also stack FC network on top of the RNNs without horizontal connection.