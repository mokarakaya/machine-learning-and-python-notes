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
  - Compute gradients of W_n+1 and b_n+1
    - for gradient of W_n+1 we need:
      - derivative of the activation function from layer n
      - error from the layer n+1
  - Use gradients to update weights and biases.
  - to calculate error of layer n, we need:
    - error from l2
    - w_2
    - derivative of z_1

