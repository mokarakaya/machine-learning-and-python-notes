# Given
“At our company, preventing bots and malicious
actors from creating accounts and making posts. 
To solve this problem, we would like to train a model
to flag accounts as potential bots for manual review. 
Since bots are rarer than real humans, 
our initial training dataset consists 
of a set of account meta information, 
where a majority of the dataset is comprised of humans.”
# Define the problem
- ML I/O:
  - How imbalance the dataset is:
    - If around 30% it could be fine.
    - If around 5%, we need handle imbalance dataset.
  - Size of the dataset:
    - Small: oversample.
      - Disadvantage: the samples should not come from the same distribution.
    - Large: undersample.
    - Get more bot samples.
# Design the data processing pipeline
# Create a model architecture
- Models:
  - Logistic regression.
    - Cross entropy:
      - weights on majority/minority classes.
      - can also help to balance precision/recall.
  - Binary decision tree.
    - more interpretable.
    - not probabilistic.
  - Ensemble models
    - We don't need to select one to another.
    - How to select weights between models
      - hyperparameter tuning.
  - Depending on the size of the data we may train model per region.
# Train the model
- Training/test split:
  - make sure we have the same portion of labels in each set. 
    - stratified training test split
    - clustering.
      - two make sure we have samples from regions
      - more important to cluster on the minority class.
# Evaluate the model
- confusion matrix
  - TP: bots predicted as bot
- F1
- AUC.
# Deploy and monitor the model
- Fairness across different groups.
- Type of bots changing in time.
  - Data drift.
  - Distribution shift over time on prod.
    - between the inputs in training and prod over time.
    - between the predictions in training and prod over time.
      - Depends on labelling strategy.
- Collect data needed to address the shortcomings found through the monitoring
- Find shortcomings of the model with monitoring
  - Collect data needed to address it.
  - Finetune or combine datasets and retrain.
# Wrap up 
- Evaluation
  - Sensitivity/robustness:
    - How much the predictions change based on small changes.