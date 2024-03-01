# Define the problem
- ML I/O
  - input: 
    - User(age, location etc), clicks, listen time.
    - Size of the data?
    - Is the raw data well-structured. 
      - Is the data noisy.
      - What pre-processing we need.
    - Computational requirements:
      - What computational resources do we have?
        - For training.
        - For serving.
      - Do we need model or data parallelization?
    - PII
      - Privacy requirements.
      - Copyright restrictions.
  - output: recommended songs
- ML Objective:
  - Increase clicks in recommended items.
  - Increase listen time, engagement.
  - Accuracy vs performance. 
    - When the predictions will be generated/used.
  - Traffic/bandwidth:
    - How many predictions do we expect per day/second?
    - How many users do we expect per day/second?
- ML Category:
  - Recommendation, ranking
# Design the data processing pipeline

# Create a model architecture
# Train and evaluate the model
# Deploy the model
# Wrap up 