# Loss Function
- Classification: cross-entropy.
- Regression: MSE.


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
- Uses changes on weights at the previous update to accelerate the convergence towards the relevant direction and reduces the fluctuation to the irrelevant direction.
- Reduces the oscillations and high variance of the parameters.
- Converges faster than gradient descent.
- One more hyper-parameter is added which needs to be selected manually and accurately.

# Adagrad
- Updates learning rate after each iteration and for each parameter.
- It makes big updates for less frequent parameters and a small step for frequent parameters
- Computationally expensive as a need to calculate the second order derivative.
- The learning rate is always decreasing results in slow training.

# AdaDelta

- Removes the decaying learning Rate problem in Adagrad.
- Instead of accumulating all previously squared gradients, Adadelta limits the window of accumulated past gradients to some fixed size w. In this exponentially moving average is used rather than the sum of all the gradients.

# Adam
- The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients.
- Instead of adapting the parameter learning rates based on the average first moment (the mean) as in RMSProp, Adam also makes use of the average of the second moments of the gradients (the uncentered variance).
- Specifically, the algorithm calculates an exponential moving average of the gradient and the squared gradient, and the parameters beta1 and beta2 control the decay rates of these moving averages.
