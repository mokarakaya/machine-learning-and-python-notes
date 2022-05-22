# A/B Testing

- We can apply A/B testing for design changes (change place or style of a button, layout changes of a page.), UI flow (e.g. purchase pipeline), algorithmic changes (recommender system), pricing changes.
- We can measure the changes in revenue, profit, clicks, ad views in product A, and product B.
- Just looking at the differences in means isn't enough. When you're trying to evaluate the results of an experiment, you need to take the variance into account as well.

## T-test
- t-value
  - = signal / noise
  - = difference between group means / variability of groups.
  - <img style="webkit-filter: invert(1);filter:invert(1);width: 30%" src="images/math3.svg">
  - s is standard variation and n is the number of samples.

<!--https://render.githubusercontent.com/render/math?math=\dfrac{|x1_{mean}-x2_{mean}|}{\sqrt{\dfrac{s1^2}{n1}%2B\dfrac{s2^2}{n2}}} -->

- After we calculate t-value we run t-test.
- T-test is running Ho (null hypothesis) which measures if there is difference between two samples statistically.
- We define a critical value, and if t-value is lower than the critical-value we do not reject the null hypothesis.
- In order to find the critical value, we need to define degrees of freedom and probability. Then we will look up from t-table.
  - Degrees of freedom = `n1 + n2 + -2`
  - Probability = e.g. p=0.05, p=0.01. if p=0.05 95% of times we reject the null hypothesis.

### P-value
- The p-value is basically the probability that this experiment satisfies the null hypothesis, that is, the probability that there is no real difference between the control and the treatment's behavior.
- A low p-value means that there's a high probability that your change had a real effect. We can choose a value between 1% and 5%. 5% is safer.

- We can use `scipy.stats.ttest_ind(A,B)` to calculate t-value and p-value.
  - T-value has direction, and negative values for t-value indicates that B results are worse.
  - In order to declare significance, we need high t-value, and low p-value.
  - If A and B sets are identical we will get; `t-value: 0.0`, `p-value:1.0`

- A neat explanation is [here](https://www.youtube.com/watch?v=-FtlH4svqx4).

## Duration of the Experiment
- We can plot t-values and p-values daily and check if there is a trend.

# A/B Test Effects

- `Novelty Effects`: Customers sometimes get attracted just because the buttons are different. So, after a while we may get opposite results in A, B tests.

- `Seasonal Effects`: We may get different results in summer times, Christmas times etc.

- `Selection Bias`: We need to make sure that the customers in Group A, Group B are selected randomly. `Undercoverage bias` is another problem, which indicates that one of the groups is not represented enough in data set.

- `Auditing Selection Bias Issues`: We can run A/A tests on A/B framework to make sure that the framework itself does not have issues.

- `Data Pollution`: We need to make sure that the customers in the groups do not pollute data. E.g. the customer is not a testing robot.

- `Attribution Errors`: We need to make sure that multiple A/B tests do not effect each other.
