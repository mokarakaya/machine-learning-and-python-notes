# Categorical Features
- An example: `names=['a', 'b', 'a', 'c']`
- One hot encoding is a good alternative to convert categories into numbers.
- We can use `sklearn.feature_extractio.DictVectorizer`, `sklearn.preprocessing.OneHotEncoder`, `pandas.get_dummies` to get one-hot-encoded data.
- When there are too many categories, we can use `sklearn.feature_extraction.FeatureHasher` or `embeddings` as an alternative.

# Text Features
- `sample = ['problem of evil', 'evil queen', 'horizon problem']`
  - `sklearn.feature_extraction.text import CountVectorizer` will create a 3x5 sparse matrix to represent data. One feature for each word, and the value is 1 if the instance has the word. We can also set the number of occurrences instead of 1 and 0.

- `TfidfVectorizer` is a better choice since it assigns weights instead of 1 and 0.

# Image Features
- A simple solution is to use each Pixel as a feature. But it may not be optimal depending on the application.

# Derived Features
- We can use `sklearn.preprocessing.PolynomialFeatures` to create new features out of the existing ones. E.g x^2 from x. This may help especially for linear models e.g. linear regression. Large values may decrease the performance e.g. x^30.
- We can also create new features by using formulas. For example if an expert knows that x/y is an important feature where x, and y are existing features, we can introduce x/y as a new feature. This will save some effort for algorithm to figure out the relation (including neural networks.).

# Feature Pipelines

```
model = make_pipeline(Imputer(strategy='mean'),
                              PolynomialFeatures(degree=2),
                              LinearRegression())
```
