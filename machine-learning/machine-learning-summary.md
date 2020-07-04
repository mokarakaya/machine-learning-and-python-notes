# Feature Engineering
- `Categorical Features`: one hot, embeddings.
- `Text Features`: CountVectorizer, TfidfVectorizer
- `Derived Features`: PolynomialFeatures

# Bias - Variance Trade off
- High Bias -> Underfitting
- High Variance -> Overfitting
- `Low bias - high variance`: The predictions are distributed everywhere except the target.
- `High bias - low variance`: The predictions are grouped on a spot but not to the target.
- `High bias - high variance`: The prediction are distributed on one part of the table.
- `Low bias - low variance (Perfect world)`: The predictions are on the target.
# Evaluation
- `Classification Metrics`: per-class accuracy, log-loss, AUC (tp, fp), precision (tp/ tp+fp), recall (tp/tp+fn). Recall expresses the ability to find all relevant instances.
# Looking for Correlations
- Covariance does not indicate the strength of the relationship. Correlation does.
# Ensemble Methods
- Bagging decreases variance in a overfit model
- Boosting decreases bias in an underfit model.
# Anomaly Detection
- `Knn`: Sensitive to `k`, Complexity is O(m^2)
- `Distibution`: Works poorly on multi-dimensional distributions.
- `Clustering`: Calculate the distance and divide it with the median distance of the cluster instances.
- Evaluate with AUC.
# CD4ML
- Three dimensions: data, model, code.
- Model can be served in an embedded model with `MLeap`
- `Facets` can help to visualize slices in data. Model may not be working well when values of the feature x is low.
- `Mlflow` experiment tracking tool with an api, and web interface.
- `Shadow models`: deploy a new model without removing the original, and see the performance of the new model by replicating the request. User does not interact with the shadow model.
