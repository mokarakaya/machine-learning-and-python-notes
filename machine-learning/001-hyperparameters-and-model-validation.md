# k-fold Cross Validation
```
create k splits
for each split
  train model(dataset - split)
  calculate error (split)
get average error
```
- Each split is called validation set.
- leave-one-out cross validation is a special cross validation where we have only one instance in the validation set. This is useful when the data set is small but consumes more time.

# Selecting the best model

- There are several ways to improve an underperforming model. In order to increase the performance we need to understand why it is underperforming. But these are some of the possible solutions:
  - Use a more complicated/more flexible model

  - Use a less complicated/less flexible model

  - Gather more training samples

  - Gather more data to add features to each sample

# Bias-Variance Tradeoff
- Underfitting -> high bias

- Overfitting -> high variance

- For high-bias models, the performance of the model on the validation set is similar to the performance on the training set.

- For high-variance models, the performance of the model on the validation set is far worse than the performance on the training set.

# Hyperparameter Optimization

## Grid-Search

- Grid search gets possible values of hyperparameters and tries all possible combinations. Then, it returns the parameters which achieves the best score.

## Random Search

- Random search gets all possible values similar to grid-search. But it randomly tries some of the possible values. Number of tries, or time are possible attributes for the algorithm.
