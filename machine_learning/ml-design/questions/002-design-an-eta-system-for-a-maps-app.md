# Given
- The map contains all necessary information about roads:
    - for each road segment,
        - distance
        - speed_limit
        - free_flow_speed (the fastest that cars typically travel)
        - priority_class (e.g. major highway, local road, etc.)
- The historical travel data:
  - for each (segment, 2m_interval),
    - num_cars
    - avg_speed
- The shortest paths functionality finds the shortest path, given a weighted graph.
- No additional labeling is required

# Define the problem
- ML IO:
  - from/to coordinates, timestamp.
  - Can we use from timezone?
  - How much data do we have?
    - All roads in the world.
    - Historical data in last 5 years.
  - Is the raw data well-structured?
    - We may have missing historical data?
    - We may have missing road segments.
  - Will we need model or data parallelization during training?
    - We may need data parallelization or sampling.
    - Can we train model per state/country/continent?
      - Need to take care of segments between state/county/continent.
  - How do we use the output?
    - Directly show to the user.
- ML Objective:
  - Tranining objective
    - Minimize error.
  - Are there business level objectives?
    - No.
  - Do we favor accuracy or low latency?
    - Balanced. 
  - Number of predictions per day?
    - Millions.
```
def predict(from, to, timestamp):
    minute, hour, day, month = get_timestamp_features(timestamp)
    segments = get_shortest_path(from, to)
    etas = []
    for segment in segments:
        segment_data = get_segment_data(segment.id)
        historical_data = get_historical_data(segment.id, minute, hour, day, month)
        eta = model.predict(segment_data, historical_data)
        minute, hour, day, month = get_timestamp_features(timestamp + eta)
        etas.append(eta)
    return sum(etas)
```
- ML Category:
  - Regression.
# Design the data processing pipeline
- Training offline and inference online.
- Features:
  - segment_data:
    - distance. cont.
    - speed_limit. cont.
    - free_flow_speed. cont.
    - priority_class. cat
  - standardize the cont values to avoid anomalies.
  - one hot encode priority class.
  - historical_data:
    - num_cars
    - avg_speed
  - Balance the dataset for each segment.
    - Remove duplicates and near duplicates.
    - maybe over-sample rare segments.
  - Y:
    - `eta = distance / avg_speed` 
# Create a model architecture
- Linear regression.
  - Should give another descent baseline.
- XGBoost
  - Generally better with column based features.
- Neural network
  - Should be able to figure out complex relations.
  - Special days in other calendars.
  - Events that don't happen on the same day every year.
- We can data parallelize all three models.
- We can't apply L1 regularization on XGBoost.
- Baseline
  - Average of the same day etas in previous year/month/week.
# Train and evaluate the model
- Minimize error with least squares optimization function.
- Monitor loss during training.
- We can overfit with a small data to check implementation.
- Overcome overfitting with L2 regularization.
- Find useless features with L1 regularization.
# Deploy and monitor the model
- Create features similar to training
  - The other systems should be fast enough for online predictions.
- Shadow deployment if we already have a model on prod.
- Check the new model is better than the existing one.
- Monitor by region, weekday/weekend.
  - To find if the model is not good at particular feature.
# Wrap up 
- 