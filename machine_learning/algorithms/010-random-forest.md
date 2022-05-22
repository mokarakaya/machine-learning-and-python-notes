- Random forests ensemble many decision trees by using bagging.
- We can create different decision trees by randomly sampling the dataset, or randomly using a subset of the features.
- It can overcome overfitting since it combines the results of many trees. 
- We lose interpretability by using random-forests.


```

Subset the original data so that the decision tree is built on only a sample of the original dataset.

Subset the independent variables (features) too while building the decision tree.

Build a decision tree based on the subset data where the subset of rows as well as columns is used as the dataset.

Predict on the test or validation dataset.

Repeat steps 1 through 3 n number of times, where n is the number of trees built.

The final prediction on the test dataset is the average of predictions of all n trees.
```
