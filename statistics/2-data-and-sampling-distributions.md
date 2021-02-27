# Sampling Distribution of a Statistic
# Standard Error
- `SE = s / (n)^(1/2)`
  - s = standard deviation of the sample.
  - n = sample size.

# The Bootstrap
-  The algorithm for a bootstrap resampling of the mean, for a sample of size n, is as follows:

```
Draw a sample value, record it, and then replace it.

Repeat n times.

Record the mean of the n resampled values.

Repeat steps 1–3 R times.

Use the R results to:

  Calculate their standard deviation (this estimates sample mean standard error).

  Produce a histogram or boxplot.

  Find a confidence interval.

```

# Binomial distribution

- Probability of observing exactly x = 2 successes in size = 5 trials, where the probability of success for each trial is p = 0.5

```
from scipy import stats
stats.binom.pmf(2, n=5, p=0.5)
stats.binom.cdf(2, n=5, p=0.5)

```
