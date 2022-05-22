# Classification Metrics
## Per-Class Accuracy
- Average accuracy of classes.
- When classes are imbalanced, we should look at the per-class accuracy, both the average and the individual per-class accuracy numbers.
- Confusion matrix also helps to visualize accuracy.

## Log-loss
-  <img style="webkit-filter: invert(1);filter:invert(1);width: 70%" src="images/math4.svg">
<!--https://render.githubusercontent.com/render/math?math=log-loss=-\dfrac{1}{N}\sum_{i=1}^Ny_{i}logp_{i}%2B(1-y_{i})log(1-p_i) -->
- We can use log-loss when the classifier returns probability instead of binary (0,1).

## AUC
- AUC is the area under the curve when we plot TP, FP rate graph.

## Precision-Recall
- `Precision = tp / tp + fp`
- `Recall = tp / tp + fn`
- tp + fp = retrieved documents
- tp + fn = relevant documents
- While recall expresses the ability to find all relevant instances in a dataset, precision expresses the proportion of the data points our model says was relevant actually were relevant.

## F1 Score
- `F1 = 2 *  (precision * recall) / (precision + recall)`


# Regression Metrics
## MAPE (Mean Absolute Percentage Error)
- RMSE is very commonly used, but it may be misleading if we have outliers in our test set.
- `MAPE = median(|y - y^| / y`)
