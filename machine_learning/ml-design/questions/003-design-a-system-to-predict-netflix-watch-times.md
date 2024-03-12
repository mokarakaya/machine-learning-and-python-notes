# Given
- Design a system to predict the Netflix 
watch time for a particular TV show,
or movie for a specific user.
- Should be customizable and accurate
so that it can work for both new
and long time users.
# Define the problem
- ML I/O
  - How much data do we have?
    - 10M datapoints from representative sample pool
  - What kind of data do we have?
    - Demographic.
    - show/movie, watch times, timestamp.
    - metadata about a show/movie.
- ML Objective:
- ML Category:
  - Regression
# Design the data processing pipeline
- 
# Create a model architecture
- Single model for all users.
  - Advantage: we learn from all data.
  - Disadvantage: performance on small groups.
- Specific models on different demographics
  - Advantage: 
  - Disadvantage: Risks overfitting.
- Two models
  - Global model:   
    - Predict mean watch time.
  - Residual model:
    - Predict how much we differ from mean.
- 
# Train the model
# Evaluate the model
# Deploy and monitor the model
# Wrap up 