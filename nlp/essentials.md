# Text Normalization
- Four main steps in text normalization are case normalization, tokenization and stop word removal, Parts-of-Speech (POS) tagging, and stemming.

# Stop word removal
- Stop word removal involves removing common words such as articles (the, an) and conjunctions (and, but), among others.
- Consider the fragment "flights to Paris." In this case, to provides valuable information, and its removal may change the meaning of the fragment.

```

import stopwordsiso as stopwords
sorted(stopwords.stopwords('en'))

```

# POS (Part-of-speech) tagging

- Some tags are listed [here](https://universaldependencies.org/docs/tagset-conversion/en-penn-uposf.html).

- [StandfordNLP](https://stanfordnlp.github.io/stanza/pos.html) (stanza) has support for POS.

```
!pip install stanfordnlp

import stanfordnlp as snlp

snlp.download('en')
en = snlp.Pipeline(lang='en')
txt = "Yo you around? A friend of mine's lookin."
pos = en(txt)
```
# Stemming and lemmatization
- The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. For instance:
  - am, are, is: be
  - car, cars, car's, cars': car
- Stemming usually refers to a crude heuristic process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes. See [Porter's Algorithm](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.848.7219&rep=rep1&type=pdf).
- Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma.


