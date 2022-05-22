# Look at the Big Picture
## Frame the Problem
- Write down the business objective.
- Imagine what the solution looks like.
- Understand the expert knowledge, and rules.
- Look at the current solution.

## Select a Performance Measure
- This depends on if the problem is a classification or regression problem.
- If there are many outliers we can consider MAE or MAPE (Mean Absolute Percentage Error).
- Does the performance measure align with the business objectives?

## Check the Assumptions
- Do we have actual values or categories for each feature. What are the possible categories?

# Get the Data

## Create the Workspace
- We can use `anaconda` or `virtualenv`.

## Download the Data
- Legal obligations, authorization.

### Loading Large Data
- A way to load large data is to split it into chunks by using `Pandas`

```
chunk_size = 10000
for train_df in pd.read_csv('data/train.csv', chunksize=chunk_size):

```

- `Dask` is also another alternative to read large files.

```
paper_dk = dask.dataframe.read_csv('/dev/shm/paper_details.csv',blocksize=4000000)
```
- We can train neural networks by using Minibatch Stochastic Gradient Descent. So, we will not need all data at time t.
- Partial fit also available for some of the algorithms e.g. SVM.


## Look at the data structure
- `df.head()`, `df.info()`, `df.describe()`
- We can also create histograms for numerical features.

```
import matplotlib.pyplot as plt
df.hist(bins=50, figsize=(20,15))
plt.show()
```

## Create a Test Set  
- Create a test set and never look at it.

# Discover and Visualize the Data to Gain Insights

- Check missing attributes.
- Check outliers and distributions.

## Looking for Correlations
- The line below will print the correlation values between feature1 and the other features.

- `covariance= avg((xij - mean_j) * (x_ik - mean_k))`

- `correlation= covariance(x, y) / (std_x * std_y)`

- Covariance is similar to correlation. Covariance finds the direction of the relationship between vectors but it does not indicate the strength of the relationship. Both of them can find the direction of the relationship.

```
corr_matrix = df.corr()
corr_matrix["feature1"].sort_values(ascending=False)
```

- We can also plot x,y graphs and histograms for each given feature. The lines below will plot 3 histograms for each feature, and 6 x,y graphs for each feature pair.

```
from pandas.plotting import scatter_matrix

attributes = ["feature1", "feature2", "feature3"]
scatter_matrix(housing[attributes], figsize=(12, 8))
```

## Experimenting with Attribute Combinations

- We can create experimental features by using the existing features e.g `feature1 * feature1`, `feature1 * feature2`, `feature1 / feature2` etc.
- Then we can check correlations again.
- We can also create features by using the expert knowledge.

# Prepare Data for Machine Learning Algorithms

## Data Cleaning

- If there are missing values for a row or column. We can;
  - Remove the row or column.
  - Set zero, mean, median, etc.

```
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")`
```

## Handling Text and Categorical Attributes

- The example below converts categories into one-hot vectors.

```
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
column_1hot = encoder.fit_transform(column)
```


## Feature Scaling

- `Min-max Scaling` (also called normalization): `(x - min) / (max - min)`
We can use `sklearn.MinMaxScaler`

- `Standardization`: `(x - mean) / standard_deviation` Standardization is less effected by outliers than min-max scaling. We can use `sklearn.StandardScaler`

## Transformation Pipelines

- We can use `from sklearn.pipeline import Pipeline` to create pipelines for transforming data, training, and evaluation.

- `from sklearn.compose import ColumnTransformer` transforms data. Parameters are name, transformation object (e.g. OneHotEncoder), and name of the attributes.

# Select and Train a Model

## Training and Evaluating on the Training Set
- Example classes: `from sklearn.linear_model import LinearRegression`, `from sklearn.tree import DecisionTreeRegressor`

## Cross-Validation
- `from sklearn.model_selection import cross_val_score`

# Fine-Tune Your Model

## Grid-Search

- `from sklearn.model_selection import GridSearchCV`
- Another alternative is Randomized Search.

## Ensemble Methods
- We can combine some of the good predictors.
- Bagging can decrease variance in an overfit model. The algorithms are built separatelly, and then the results are combined.
- Boosting can decrease bias in an underfit model. Focuses on the misclassified samples by reweighting the samples. Highly weighted samples will be used in training more.

### Bagging

- Similar learners use different samples of data and then we get the average of the prediction. We can train models in parallel.
- Helps to `reduce the variance error`.

### Boosting
- This is a sequential approach, and we first train the model. Then, we identify instances with high error. In the next iteration we increase the weight of these instances. So, these instances will be in training set with a higher probability.
- This method primarily focus on reducing `bias`.
