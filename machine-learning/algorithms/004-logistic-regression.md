- **Pros**: Computationally inexpensive, easy to implement, knowledge representation easy to interpret
- **Cons**: Prone to underfitting, may have low accuracy


# Gradient Descent

- `y^ = wT x`

- `w = w – α ▽_w f(w)`


```
Calculate the gradient of the entire dataset by data.transpose() * error
Update the weights vector by alpha * gradient
Return the weights vector
```

- Batch gradient descent uses the whole data set to calculate the gradient. Stochastic gradient uses a single instance. Minibatch uses a small subset of the data set.

- Calculating the gradient by using a single instance may be noisy, but it may also help to avoid local-minima.

- A good balance is when the minibatch size is small enough to avoid some of the local minima, but large enough that it is not noisy.

# How to Predict Missing Values

- Use the feature’s mean value from all the available data.
- Fill in the unknown with a special value like -1.
- Ignore the instance.
- Use a mean value from similar items.
- Use another machine learning algorithm to predict the value.
