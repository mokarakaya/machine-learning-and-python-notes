# Encoder
- Encoder stack updates the input embeddings to produce representations
that encode some contextual information in the sequence.
e.g. word "apple" will be updated to more "company-like" than "fruit-like"
- Encoder block has three sub-blocks:
  - Multi-head self-attention layer.
  - A fully connected feed-forward layer.
  - Layer normalization (and skip connections)
- Multi-head self attention:
  - Computes relationships between words or tokens in a sequence.
  - Allows model to focus on relevant parts of the input.
  - Scaled dot product attention:
    - Each input embedding is projected into three different spaces:
      - Query (Q): Represents what the token is trying to find or focus on.
      - Key (K): Represents token's identity or features.
      - Value (V): Represents the token's actual content or contribution.
      - Attention score is the dot product of Q and K.
      - Attention weight is the softmax of scaled attention score.
      - Output is the weighted sum of values by attention weights.
  - Self attention allows parallel computing and captures long-range dependencies.
  - The input is split into multiple-heads:
    - to learn different relationships using different QKV projections.
  - Disadvantages:
    - Time complexity: O(n_2 * d):
      - n: sequence length
      - d: embedding dimension.
      - Sparse or linear attention to mitigate.
    - Sequence relies on positional encodings.
    - Inefficient in long sequences.
      - Longformer, Linformer and BigBird to mitigate.
    - Lack of interpretability.
    - Multi-head attention is overhead.
    - Heavy relies on tokenization.
- Feed-forward layer (position-wise feed-forward layer):
  - Has two layers.
  - Processes each embedding independently.
- Layer normalization:
  - Layer normalization normalizes each input in the batch to have:
    - zero mean and unity variance.
  - Skip connections pass a tensor to the next layer of the model
    - without processing and add it to the processed tensor.
  - We can place layer normalization in two ways:
    - Post layer normalization:
      - Requires learning-rate warm-up as gradients can diverge easily at the beginning.
    - Pre-layer normalization:
      - most common, more stable, does not need learning-rate warm up.
- Positional embeddings:
  - As transformers process input sequence as a whole rather than sequentially:
  - we add positional embeddings to provide sense of position of the tokens.
  - Token embeddings and positional embeddings are
    - concatenated and passed to the next layer.
  - Input to the positional embeddings is the sequence id of the token.
# Decoder
- Decoder has three main sub-blocks and two of them are attention blocks:
  - Masked multi-head self-attention layer.
  - Encoder-decoder attention layer.
  - Feed-forward layer.
- Masked multi-head self attention:
  - Masks the future tokens.
- Encoder-decoder attention layer:
  - Integrates information from the encoder by:
    - Q comes from the decoder's previous layer
    - K, V comes from the encoder's output.
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