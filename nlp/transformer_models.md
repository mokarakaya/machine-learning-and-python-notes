# Encoder
## Bert
- Bert model is trained on two tasks:
  - Masked Language Modeling (MLM):
    - Some words are masked in a sentence and model predicts the masked word.
  - Next Sentence Prediction (NSP)
    - Given two sentences, model predicts if one sentence can be continued with the other.
- It's bi-directional because every token in the sequence is allowed to attend the input.
- The output of the encoder model is a rich representation of words so it can be used for:
  - text classification, NER, embeddings etc.

# Decoder
## GPT