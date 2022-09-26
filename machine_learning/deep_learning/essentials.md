# Activation Functions

- It's important to choose the right activation function;
  - It may cause vanishing gradient problem.
  - Derivative of the function is important for backpropagation.


- `Sigmoid`: 
  - Ranges between 0 and 1.
  - May cause vanishing gradient problem and has slow convergence.
  - Relu generally outperforms sigmoid.
  
- `Tanh (hyperbolic tangent function)`
  - Ranges between -1 and 1.
  - Preferred over sigmoid.
  - May cause vanishing gradient problem.

- `ReLU (Rectified Linear Unit)`:
  - More efficient than tanh and sigmoid. Converges six times faster.
  - Avoids vanishing gradient problem.
  - As output is not in probability space it can only be used in hidden layers. 
  We can not use it in the output layer. 
  - We should prefer softmax in the output layer for classification.
  - We should prefer linear function in the output layer for regression.
  - May cause dead neuron problem.  
  The weights to be updated such that a neuron will never be active on any other future data points.

- `Leaky ReLU and maxout`:
  - Leaky ReLU solves the dead neuron problem by introducing 
  a small slope α on the negative side, such as 0.01
  - Maxout is a general form of Leaky ReLU.

- `Softmax`
  - Generally used in the output layer for a classification problem.
  - Each class gets a value in the probability space and the sum is 1.


