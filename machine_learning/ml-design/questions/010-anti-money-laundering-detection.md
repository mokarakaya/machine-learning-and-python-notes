# Given
- We want to design an anti-money-laundering detection system.
- The system labels transactions as low, medium, high.
# Define the problem
- We can solve this problem as a multi class classification model.
- As the high labels will be low we can:
  - Oversample:
    - random:
      - good for small datasets and easy to implement. 
      - may lead to overfitting as it duplicates without adding new information.
    - smote (synthetic minority over-sampling)
      - 
  - Undersample:
    - 
  - Use class weights
# Design the data processing pipeline
# Create a model architecture
# Train the model
# Evaluate the model
# Deploy and monitor the model
# Wrap up 