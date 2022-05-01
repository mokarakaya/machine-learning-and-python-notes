# Embeddings

- Embeddings are low-dimensional, learned continuous vector representations of discrete variables.
- Embeddings are used to represent words, phrases, and other entities in a continuous space.

## Advantages
- One-hot encoding does not fit well for high cardinality variables.
- Similar inputs are not placed closer to each other.

## Disadvantages
- Hard to compute.
- Less interpretable.

## How to create embeddings.
- Common way to set up a supervised machine learning problem.
As an example; next movie recommendation. The embeddings will represent movies, and similar movies will be closer to each other.

## Common Embedding Models
- PCA and SVD can be used to create embeddings.

### Word2Vec
- Word2Vec algorithm was published by Tomas Mikolov and collaborators from Google in 2013.
- The original paper had two algorithms proposed in it: `continuous bag-of-words` and `continuous skip-gram`.
- The algorithm uses nearby words for a given word and trains a vector for each word.
  - As example; "Bake until the cookie is golden brown all over." 
  If the input is cookie and n=2 the output is true for all "until, the, is golden". It is false for other words e.g. kangoroo
  - This can be a multi-label neural network classification with a one-to-many as the output layer. 
  The weights become the embedding for each word once training is complete.
- The hidden weights are returned as embeddings.
- Embeddings can be used to form analogies e.g. the vector from king to man is very similar to the one from queen to woman.
- The problem with Word2Vec is that words do not have contexts e.g. "play" can be a noun or a verb but their embeddings will be same.

### BERT (Bidirectional Encoder Representations of Transformers)
- <:TODO>


## Embedding Operations
- <:TODO>
- **Averaging**: 

## Pretrained embeddings

- Some packages like `Gensim` provide pre-trained embeddings.
- Huggingface has pre-trained embeddings for words and sentences.

```
!pip install gensim

from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
model_w2v = api.load("word2vec-google-news-300")

king = model_w2v['king']
man = model_w2v['man']
woman = model_w2v['woman']
queen = king - man + woman  
model_w2v.similar_by_vector(queen)

```

- Re-use pre-trained embeddings
  - **Static**: We freeze pre-trained embeddings in the model.
  - **Updated**: We update pre-trained embeddings during training.

# Resources 
- https://www.featureform.com/post/the-definitive-guide-to-embeddings
- https://medium.com/towards-data-science/neural-network-embeddings-explained-4d028e6f0526
- https://machinelearningmastery.com/what-are-word-embeddings/