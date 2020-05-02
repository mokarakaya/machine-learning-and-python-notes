- **Pros**: Low generalization error, computationally inexpensive, easy to interpret results.

- **Cons**: Sensitive to tuning parameters and kernel choice; natively only handles binary classification.

- This technique has shown promising empirical results in many practical applications, from handwritten digit recognition to text categorization.

# The Maximum Margin Hyperplane

- Separating hyperplane is  <img style="webkit-filter: invert(1);filter:invert(1);width: 15%" src="images/math.svg">

- We want to maximize the distance from separating hyperplane to the closest instance.

- <img style="webkit-filter: invert(1);filter:invert(1);width: 20%" src="images/math1.svg"> draws a perpendicular line to instance `A`.

<!-- https://render.githubusercontent.com/render/math?math=\dfrac{|w^T%20A%2Bb|}{||w||} -->

- Objective function is <img style="webkit-filter: invert(1);filter:invert(1);width: 70%" src="images/math2.svg"> where the labels are `-1` or `1`.
<!-- https://render.githubusercontent.com/render/math?math=\maximize_{wb}\{min_{n}\{label * (w^T%20A%2Bb)\} . \dfrac{1}{||w||} \} -->


- We will hold `label * (wT x + b)` and maximize `||w||^-1`. `label * (wT x + b)` can be 1 or more. This kind of proplems are called constrained optimization problems and we can solve them by using Lagrange multipliers. We rewrite the problem with constraints as below;

-  <img style="webkit-filter: invert(1);filter:invert(1);width: 90%" src="images/math3.svg">
<!-- https://render.githubusercontent.com/render/math?math=\maximize_{\alpha}[\sum_{i=1}^{m}%20\alpha%20\sum_{i%20,%20j%20=1}^{m}%20label^i%20*%20label^j%20*%20\alpha_{i}%20*%20\alpha_{j}%20*%20\lt%20x^i%20,%20x^j\gt] -->

- Subject to the following constraints;
- `alpha >= 0` and <img style="webkit-filter: invert(1);filter:invert(1);width: 30%" src="images/math4.svg">

<!-- https://render.githubusercontent.com/render/math?math=\sum_{i-1}^{m} \alpha_i * label^i = 0  -->

- The constraint below requires that the data is linearly separable. We need to relax the first constraint to solve linearly non-separable data by introducing a `slack variable` `c` as below;
-  `c > alpha >= 0`

- `c` is one of the hyperparameters of the SVM algorithm. Our aim is to find best alpha values. Once we have the alpha values we can easily calculate `w`.


#  Sequential Minimal Optimization (SMO)

- John Platt published SMO algorithm in 1996. SMO takes a large optimization problem and breaks it into smaller problems. On each cycle, SMO finds two suitable alphas for optimization and optimize them by increasing one and decreasing the other.
- The pair of alphas should be outside of their margin boundary, and they should not be clamped or bounded (error should be less than tolerance, and alpha should be less than C for negative labels, and more than 0 for the positive labels).
- The size of alphas equals to the size of the training set.

```
Create an alphas vector filled with 0s While the number of iterations is less than MaxIterations:

For every data vector in the dataset:

    If the data vector can be optimized:

    Select another data vector at random

    Optimize the two vectors together

  If the vectors can’t be optimized → break If no vectors were optimized →increment the iteration count
```

# Full Platt SMO
- Create a sublist of non-bound alphas. (alphas that aren’t bound at the limits 0 or C.) and iterate over the list.
- Select the second alpha which return max for `Ei - Ej`

# Kernels
- When the data is nonlinear, we can map data from one feature space to another feature space to linearly separate data. Usually, this mapping goes from a lower-dimensional feature space to a higher-dimensional space. This may be costly, and suffer from the curse of dimensionality.

- A better way is to user kernels which actually calculates similarity between two instances.

- We can think of the kernel as a wrapper or interface for the data to translate it from a difficult formatting to an easier formatting.

- Radial Basis Function (rbf) ->  <img style="webkit-filter: invert(1);filter:invert(1);width: 40%" src="images/math5.svg">

<!--
https://render.githubusercontent.com/render/math?math=k(x,y)\=exp(\dfrac{-||x-y||^2}{2\sigma^2})
 -->
