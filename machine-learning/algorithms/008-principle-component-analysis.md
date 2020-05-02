- **Pros**: Reduces complexity of data, identifies most important features

- **Cons**: May not be needed, could throw away useful information

# PCA
- Principal Component Analysis (PCA) is used to explain the variance-covariance structure of a set of variables through linear combinations. It is often used as a dimensionality-reduction technique.

```
Remove the mean

Compute the covariance matrix

Find the eigenvalues and eigenvectors of the covariance matrix

Sort the eigenvalues from largest to smallest

Take the top N eigenvectors

Transform the data into the new space created by the top N eigenvectors
```

## Linear Transformation

- Linear Transformation has two rules.
  - `T(a + b) = T(a) + T(b)`
  - `T(c a) = c T(a)`
  - where T is the transformation function, and a, b are vector and c is a number.

## Eigenvectors and eigenvalues

- `A v = \lambda v`:
  - `A` is nxn matrix
  - `v` is nx1 vector (eigenvector)
  - `\lambda` is a scalar. (eigenvalue)

- We can rewrite the problem as: `(A - \lambda I ) v = 0`
- Since `v` is non-zero matrix: `|A - \lambda  I| = 0`
- Then we can find possible `\lambda` values.
- [Here](https://lpsa.swarthmore.edu/MtrxVibe/EigMat/MatrixEigen.html) is an example how to calculate eigenvectors and values.
- Eigenvectors are nonzero vectors that changes at most by a scalar during linear transformation.
- The eigenvector associated with the largest eigenvalue indicates the direction in which the data has the most variance.

## Covariance matrix
- Covariance matrix is a `n X n` matrix where n is the number of features.
- If there are two features X, Y. [0,0] is the variance of X, [0,1] and [1,0] are covariance between X and Y. These two values are equal to each other. [1,1] is the variance of Y. An example to calculate covariance matrix is [here](https://jamesmccaffrey.wordpress.com/2017/11/03/example-of-calculating-a-covariance-matrix/).
