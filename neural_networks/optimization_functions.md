

# Optimization Functions

## Gradient Descent
- Calculates the gradients on whole dataset.
- May trap at local minima.
- Can take long to reach optimal.

# Stochastic Gradient Descent
- Updates gradients for each input.
- Converges in less time.
- High variance in model parameters.
- Can keep updating weights after reaching global minima.

# Minibatch Gradient Descent
-

# Momentum
- Uses changes on weights at the previous update to accelerate the 
convergence towards the relevant 
direction and reduces the fluctuation to the irrelevant direction.
- Reduces the oscillations and high variance of the parameters.
- Converges faster than gradient descent.
- One more hyper-parameter is added which needs to be selected manually and accurately.

# Adagrad
- Updates learning rate after each iteration and for each parameter.
- It makes big updates for less frequent parameters and a small step for 
frequent parameters
- Computationally expensive as a need to calculate the second order derivative.
- The learning rate is always decreasing results in slow training.

# AdaDelta

- Removes the decaying learning Rate problem in Adagrad.
- Instead of accumulating all previously squared gradients, 
Adadelta limits the window of accumulated past gradients to some fixed size w. 
In this exponentially moving average is used rather than the sum of all the gradients.

# Adam
- Maintains two moving averages:
  - First Moment Estimate: Average of past gradients. (Similar to momentum)
    - Remembers the direction of the past gradients.
    - momentum increase if the direction is often the same.
  - Second Moment Estimate: Average of the squared gradients. (Similar to RMSProp)
    - Remembers the magnitude of the gradients.
    - If the gradient is large, the learning rate is reduced.