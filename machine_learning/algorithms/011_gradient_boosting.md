# Gradient Boosting
- Gradient boosting is an ensemble model where we create 
weak learners (small trees) sequential where each tree focuses on 
fixing the errors of the previous tree.
- y_t = y_t-1 + n f_t(x) where:
  - y_t is the current prediction.
  - y_t_1 is the prediction up-to the current tree.
  - n learning rate
  - f_t(x) is the prediction of the current tree.
- We can apply L1, L2 regularization in gradient boosting:
  - Each leaf has a weight to determine its contribution to the final prediction.
- LightGBM:
  - Leaf-Wise Growth
    - We find the best split among the leaves.
    - We may create an unbalanced tree.
    - Faster on large datasets.
    - Better performance on large datasets.
    - More prone to overfitting.
- XGBoost:
  - Level-Wise Growth
    - We build trees level by level.
    - We create a balanced tree.
    - Slower on large datasets
    - Better performance on datasets with high variance.
    - Better at avoiding overfitting.