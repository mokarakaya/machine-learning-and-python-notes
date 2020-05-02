# Approaches to Anomaly Detection

## Model-Based Techniques
- A model can be clusters, linear regression, etc. If clusters, the anomaly is an instance which does not strongly belong to any classes.

## Proximity-Based Techniques
- We use distance-based outlier detection.

## Density-Based Techniques
- We use density of the data, and this approach is similar to proximity-based approaches since we also use distance metrics.

# Detecting Outliers in a Univariate Normal Distribution
- We can create a Gaussian distribution from the data and examine data with low probability as candidate anomalies. To do that we can transform x into z (z-score) where `z = (x - mean) / std`.

# Outliers in a Multivariate Normal Distribution
- We can get distance between x and mean of the data. An example distance metric for this purpose is Mahalonobis distance
- `mahalonobis(x, x_mean) = (x - x_mean) S^-1 (x - x_mean)^T`

- Statistical approaches may work poorly on multi-dimensional data.

# K-nearest Neighbors
- We can mark items as outliers if their distance to their k-nearest neighbors is high. This approach is very sensitive to input `k`. The complexity is O(m^2) and it is expensive for large data sets.

# Clustering-Based Techniques
- First approach is to discard small clusters which are far from other clusters. This approach is sensitive to the number of clusters and the distance threshold.
- Another approach is to cluster the items first, and then check each items distance to its cluster center.

# Evaluation
- AUC is one of the most common evaluation metrics for anomaly detection. We can also check confusion matrix.

https://towardsdatascience.com/understanding-anomaly-detection-in-python-using-gaussian-mixture-model-e26e5d06094b
