- **Pros**: Easy to interpret results, computationally inexpensive
- **Cons**: Poorly models nonlinear data


# Standard Regression

- Squared error: <img style="webkit-filter: invert(1);filter:invert(1);width: 30%" src="images/math6_1.svg">

<!-- https://render.githubusercontent.com/render/math?math=\sum_{i=0}^{m}(y_i-X^Tw)^2 -->

- We can rewrite the equation as: <img style="webkit-filter: invert(1);filter:invert(1);width: 30%" src="images/math6_2.svg">

<!-- https://render.githubusercontent.com/render/math?math=(y-Xw)^T(y-Xw)
-->
- If we take the derivative with respect to `w`: <img style="webkit-filter: invert(1);filter:invert(1);width: 30%"
src="images/math6_3.svg">


- The equation for `w` becomes: <img style="webkit-filter: invert(1);filter:invert(1);width: 30%"
src="images/math6_4.svg">

<!-- https://render.githubusercontent.com/render/math?math=w=(X^TX)^{-1}X^Ty
-->

- Then we can calculate `w` by using the data. Since we get the inverse of `X^T X` the determinant of `X^T X` should not be zero.

# Ridge Regression
- Ridge Regression adds `\lambda I` where I (identity matrix) is `m x m`. So, the inverse matrix always exists.
- `\lambda` is a user defined value.
- <img style="webkit-filter: invert(1);filter:invert(1);width: 30%"
src="images/math6_5.svg">
<!-- https://render.githubusercontent.com/render/math?math=w=(X^TX%2B\lambda%20I)^{-1}X^Ty -->


# Lasso Regression
- Lasso regression uses the same equation for `w` as Ridge.
- The only difference is the additional constraints.
- Additional constraint for Ridge is <img style="webkit-filter: invert(1);filter:invert(1);width: 20%"
src="images/math6_6.svg">
- Additional constraint for Lasso is <img style="webkit-filter: invert(1);filter:invert(1);width: 20%"
src="images/math6_7.svg">
<!--
https://render.githubusercontent.com/render/math?math=\sum_{k=0}^{n}w_k^2\leq%20\lambda -->

# Bias Variance Tradeoff

- High Bias - Low Variance: Underfitting
- High Bias - High Variance: Bad results
- Low Bias - Low Variance: Good results
- Low Bias - High Variance: Overfitting
- The errors of the instances are similar when variance is low.
