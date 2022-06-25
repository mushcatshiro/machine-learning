# natural language processing in action

## chapter 2 work tokenization

for natural language besides those expressed explictly there is also a set of implicit meaning to it. NLP does not deal with that, yet.

stemming and lematization

tokenization can be think of as a form of document segmentation. starting from scratch one can one-hot label the corpus where the column name are the distinct words and the row index are the sentance's sequence. however this results in a very sparse matrix and requires significanlty large disk space.

```bash
# assume 1M tokens 3k document with each 3.5k sentance and 15 words eachh
>> 3000 * 3000 * 15 * 1_000_000
# ~157.5 terabytes
```

knowing that its impractical, it is clear that compression is needed to move forward. instead of perfect recall, capturing most of the meaning in a document is preferred. bag of words. by chunking documents into sentances and ignoring word order and grammar, one gets a bag of words, or word frequency vector. the general idea is to change the row into e.g. sentence to indicate presence of words available in the columns.

```json
{
    "A": 1,
    "cat": 2,
    # ...
}
```

to figure out similarities dot product is used. using the data structure described from the paragraph earlier, dot products helps one to find out similarities between rows.

### tokenizers

- spacy
- NLTK
- stanford coreNLP (java)

words like "doesn't" is better off splitted into "does" and "n't" to allow syntax tree parser to have a consistent predictable set of tokens with known grammer rules as its input.

sentance like "i scream, you scream, we all scream for ice cream." can be confusing for the machine when it look at each word separately ie ("ice" and "cream"). thus the introduction of n-grams.

#### n-grams

n-grams is a sequence that contains up to $n$ elements. by extending bag of words with n-grams one can retain more information of each sentance. besides incorporating n-gram's concept into BoW, it is also important to know how to recognize which of the n-grams contains more information than others. this helps to reduce the number of n-grams required to be stored. rare n-grams usually is not helpful for classification problems as they do not carry correlation with other words. however bi-grams like "at the" that appears more frequently does not yield much predictive power and results in losing the utility for discriminating meaning between documents (ie it appears 10% in one document and 15% in another document, however it does not imply that these two documents are related).

```json
{
    "A cat": 1,
    "cat was": 1,
    # ...
}
```

#### stop words

stop words might carry little to no information however it provides relational infomation as part of n-gram e.g. "reported to the CEO" and "reported as the CEO" has different meaning yet if stop words are removed they essentially are left with "reported CEO". retaining stop words however increases the length required of the n-grams to make use of these connections.

with that being said, stop words might not necessarily have a significant impact. for a 20k vocabulary document, removing 100 stop words does not significantly improve the speed of processing. for n-grams (n>2) the saving is miniscule and is subjected to the risk of losing information. if computational or memory is not sufficient, there are better ways to identify what words to be removed from the document (TF-IDF). this will be discussed in chapter 3.

#### vocabulary normalizing

- case folding (make all vocabulary into lower case) with the backdraw of changing meaning of words that have different meaning ie "doctor" and "Doctor". this can be a problem for NER task. a slightly better approach is to only normalize first word of each sentance.

> many NLP pipelines do not bother to do case folding. however for IR search enginer case folding can help to reduce overfitting and improve recall.

- stemming reduces the size of vocab while limiting the loss of information and meaning as long as subtle difference between e.g. "house" and "houses" can be ignored. similar to case folding it also reduces the accuracy. (Porter and Snowball stemmer)

- lemmatization is an extensive normalization that transforms words into their semantic root. it can help with the association of several words even if their spelling is different. lemmatization takes account into a word's meaning by using a knowledge base and/or part of speech (POS) tagging.

> a recurring theme here is normalizing improves recall and reduces accuracy.

> lemmatizer before stemmer. this reduces dimensionality and inprove recall. the other way round does not work.

> lemmatizer is more computationally demanding than stemmer but provides a better result as it is more likely to retain more useful information.

### sentiment

one of the **key NLP tasks** - sentiment analysis. there are two approach, rule-based heuristics and ML model e.g. naive bayes. an example of heuristics is the VADER algorithm.

#### naive bayes

```python
import pandas as pd
from collections import Counter
from nltk.tokenize import casual_tokenize
pd.set_option('display.width', 75)
bags_of_words = []
for text in movies.text:
    bags_of_words.append(Counter(casual_tokenize(text)))
df_bows = pd.DataFrame.from_records(bags_of_words)
df_bows = df_bows.fillna(0).astype(int)

from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB()
nb = nb.fit(df_bows, movies.sentiment > 0)
movies['predicted_sentiment'] = nb.predict_proba(df_bows) * 8 - 4
movies['error'] = (movies.predicted_sentiment - movies.sentiment).abs()
movies.error.mean().round(1)
2.4
movies['sentiment_ispositive'] = (movies.sentiment > 0).astype(int)
movies['predicted_ispositiv'] = (movies.predicted_sentiment > 0).astype(int)
movies['''sentiment predicted_sentiment sentiment_ispositive predicted_ispositive'''.split()].head(8)
(movies.predicted_ispositive == movies.sentiment_ispositive).sum() / len(movies)
```

the model trained above have a difficult time in generalization as the tokens are limited and naive bayes is not good in identifying negation e.g. "not bad". n-grams can be helpful for negations.

## chapter 3 TF-IDF vectors

in the previous chapter, one is able to get words' statistic and/or doing keyword search. however what's more important is to know which word is more important to a particular document and across the corpus as a whole. the importance value is then used to find relavant document in the corpus.

### BoW

normalizing the word counts/term frequency makes the comparison between corpus of different size meaningful.

### Vectorizing

basic BoW with python's dict can be improved by vectorization.

```python
document_vector = []
doc_length = len(tokens)
for key, value in kite_counts.most_common():
    document_vector.append(value / doc_length)
```

by generating document vector for a set of documents such that all unique characters are the columns. in this document vector space, one can use cosine similarity to check document similarity. note that cosine theta equals to zero should be inferred as there is no same words used in the documents however does not imply that the documents are discussion different subject. also the range should be in 0 ~ 1, frequency cant be negative.

### Zipf's law

> Zipf's law stats that given a corpus of natural language utterances, the frequency of any words is inversely proportional to its rank in the frequency table.

### topic modeling

IDF is the based on Zipf's law to help in topic analysis. however one should use log to normalize the result. this ensures that TF-IDF scores are more uniformly distributed.

$$
TF(t, d) = count(t)/count(d)
\\
IDF(t, D) = log(\text{number of documents}/\text{number of documents containing t})
\\
TF-IDF = TF(t, d) * IDF(t, D)
$$

in some cases, all calculation is done in log slace thus the multiplications and divisions becomes additions and subtractions.

### relavance ranking

now one can have a matrix with the columns of each unique words in document and each rows representing one document where each column is filled with the respective word's TF-IDF value. using cosine similarity again one can search for similar documents in corpus. again note that cosine similarity does not tell if the magnitude is similar just angle. this search is at $O(n)$ which can be improved on by using an inverted index to attain constant time $O(1)$.

> check python package Whoosh for inverted index implementation

in the search one should drop keys that is not found in the lexicon to avoid divide by zero error. a better approach is to $+1$ to the denominator of every IDF calculation to ensure no denominators is zero. this is called *additive smooting* or Laplace smoothing.

TF-IDF have been the mainstream approahc of information retrieval thus much effort was put into optimizing the IDF part to improve search results.

#### IDF Alternatives

- TF-IDF
- TF-ICF
- Okapi BM25
- ATC
- LTU
- MI
- PosMI
- T-Test
- $x^2$
- Lin98a/Lin98b
- Gerf94

> yeah it is really named x^2, more in chap4

## chapter 4 semantic analysis

TF-IDF importance score works on words and n-grams. n-gram's importance score works well with text search. such approach is also known as *latent semantic analysis* which represents meaning of word combination. this allows searches without exact words and identify word(s) that best represent the subject of a document (text summarize).

problem with raw TF-IDF is sentance that bears the same meaning that uses different words will be represented differently. normalization techniques (lemmatization and stemming) might not improve the performance and potentially group antonyms together.

also math operation on TF-IDF vectors are essentially giving sums/differences about the **word frequency** used in the documents. they are not associated with the meaning of the document. vector reasoning by multiplying TF-IDF matrix and TF-IDF vectors generally does not work as these high dimensional vectors are too sparse to be useful.

in order to extract additional from the document, the combination of words in a particular document is much suitable to represent as its meaning and it is also refers as the topic vector. it is expansible, ie can range from one dimension to thousands of dimensions. summing and subtracting now is useful for clustering documents or semantic search. supposed each document will have one topic vector attached to it. reprocessing the entire corpus for new topic vector for a document is not needed. one can work from the topic vector for each word in the vocabulary/lexicon and use these to compute the topic vector.

> note some algorithm eg LDA requires reprocessing of the entire corpus

english is a fuzzy language where words have multiple meanings (also known as polysemy).