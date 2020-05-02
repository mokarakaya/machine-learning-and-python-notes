- **Pros**: Works with a small amount of data, handles multiple classes
- **Cons**: Sensitive to how the input data is prepared

# Conditional Probability

- `P(gray|bucketB) = P(gray and bucketB)/P(bucketB)`

# Bayes’ Rule

- `p(c|x) = p(x|c) p(c) / p(x)`

# Independent Features
- One feature or word is just as likely by itself as it is next to other words. We’re assuming that the word bacon is as likely to appear next to unhealthy as it is next to delicious. We know this assumption isn’t true; bacon almost always appears near delicious but very seldom near unhealthy. This is what is meant by naïve in the naïve Bayes classifier.
- Naive bayes works better when the features are independent.

# Training

```
Count the number of documents in each class for every training document:

for each class:

if a token appears in the document → increment the count for that token

increment the count for tokens

for each class:

for each token:

divide the token count by the total token count to get conditional probabilities return conditional probabilities for each class
```
- training =` [a, b, c, 0], [a,d,e, 1]`
- p0Vec = `[1,1,1,0,0]`
- p1Vec = `[1,0,0,1,1]`
- probabilities for each class = `[0.5, 0.5]`

# Classification

```
for each class i:
  P_i = sum(instance * piVec) + log(pi)
return the class with highest P
```

# Bag of Words Document Model

- Previous calculation is called set-of-words model. It calculates the piVec if the word occurs in the instance or not. Another way it to calculate the number of words occurs in the sentence which is called bag-of-word model.

- training =` [a, a, b, 0], [a, c, c, 1]`
- p0Vec = `[2,1,0]`
- p1Vec = `[1,0,2]`

# Estimating Conditional Probabilities for Continuous Attributes
- There are two ways.
  - Create categories for numbers e.g. high, low, etc.
  - Gaussian distribution is usually chosen to represent the class-conditional probability for continuous attributes. We need to calculate mean and standard deviation for each label.

# Optimization
- Remove non-words (punctuation, numbers) if needed, and lower-case all words.
- Remove stop-words.
- Remove if the word is frequently used in all classes.
