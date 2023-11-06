# Blue
    `Geometric mean of Precision of ngrams * Brevity Penalty`
- Brevity Penalty: `exp(1 - reference_length / candidate_length)`
- Brevity Penalty is 1 if the prediction length is equal to 
or longer than the reference length.
- The disadvantage of BLEU is that it does not consider importance of the
words and meaning.

# ROUGE
    `Sum of Recall of ngrams`
- Rough has similar problems as BLEU.

# BERTScore
- BERTScore is an automatic evaluation metric for text 
generation that computes a similarity score for each token 
in the candidate sentence with each token in the reference sentence.

# Perplexity
    perplexity = e**(sum(losses) / num_tokenized_tokens)
- Given a model and an input text sequence, perplexity measures how likely the 
model is to generate the input text sequence.
- As a metric, it can be used to evaluate how well 
the model has learned the distribution of the text it was trained on.

