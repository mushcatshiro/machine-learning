# Distributed Representations of Sentences and Documents

## problems associated with BoW are

losing of word orders which is improved upon with N-grams; semantics of words being ignored as all words are equi-distance. the paper proposed using *paragraph vector* that learns fixed length vector on variable length text. by combining BoW and N-grams into BoNgrams it still suffers from sparsity (q1 how does the paper introduce dimension compression/reduction?). at prediction time, paragraph vector are generated (q2 longer inference time?) through training until convergence based on the fixed word vectors.

the paragraph vector acts as a memory that remembers what is missing form the current context (q3 does that means PV-DM just memorizing text in paragraph?). also based on the paper Fig.2, knowing paragraph vector is likely to have a different size that the word vectors, how the neural network handles this difference? the paper mentioned that PV-DM and PV-DBOW can be used together?

## on IR

method: sample three paragraph, two from same document and one from a different corpus to see if distance between the paragraphs make sense.

## math

improved from word2vec's $y=b+Uh(w_{t-k},...,w_{t+k};W)$ into $y=b+Uh(w_{t-k},...,w_{t+k};W,D)$ where $W$ is the word vector and $D$ is the document vector


## hints on algorithm implementation

- using SGD and BPP
- paragraph vectors are unique among paragraphs but word vector are shared
- hierarchical softmax using binary Huffman tree (speedup trick to access common quickly)

## references

- [genism doc2vec implementation](https://radimrehurek.com/gensim/models/doc2vec.html)