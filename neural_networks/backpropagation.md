# Backpropagation
- Forward pass:
  - Forward pass calculates:
    - z = w*x + b
    - activation_function(z)
- Calculate loss gradient:
  - square(y_pred - y_true) -> average of all items in batch.
  - gradient of loss with respect to the networks output.
- Propagate the error backward:
  - Compute error in layer n+1
  - Compute gradients of W_n and b_n, we need:
    - W_n+1, b_n+1
    - gradient from n+1
    - derivative of the activation function from layer n
  - Use gradients to update weights and biases.