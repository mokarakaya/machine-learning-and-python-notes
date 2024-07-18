# Given
For a given search query with following parameters:
- stay_start_date
- stay_end_date

Calculate number of days to be sold out for each search result.

# Define the problem
- This can be solved as either a time series prediction problem or a regression problem.
- We prefer to solve it as a regression problem because:
  - We can generalize the general behavior of the users better.
  - We can make predictions even if we don't have enough data for a particular room.
- `y`=number of days to be sold out before the stay date.
  - if stay_date:15/07 and we predict the room to be sold out on 10/07
  - the model should return 5.
  - the model is not dependent to the start date.
  - We can calculate the real number days to return after model prediction.
  - if the query date is 01/07 we return (number_of_days_to_stay - y)
- We predict stay_date for each day between stay_start_date and stay_end_date.
- Then we return the minimum.
- This means if we narrow the total stay date y may get higher.
- We return this for each search result, therefore it should be fast.
- RMSE.
- Engagement. Do the users book more often. A/B test
- Inputs:
  - Hotel data
    - location
    - hotel
  - Room data
    - number of rooms
    - room_type
  - Context
    - stay_date (month, day)
    - number of available rooms
    - number of bookings in last 7 days
    - number of bookings in last 30 days
- We maintain an online feature store to keep:
  - number of available rooms
  - Bookings in last n days.
  - We should receive each booking event
# Design the data processing pipeline
# Create a model architecture
# Train the model
# Evaluate the model
# Deploy and monitor the model
# Wrap up 