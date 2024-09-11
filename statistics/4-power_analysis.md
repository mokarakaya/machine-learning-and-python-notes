
# Key Inputs to Calculate Sample Size
## Effect size or minimum detectable effect (MDE)
- Smallest effect size you want to test to be able to detect.
- Smaller MDE will require larger sample size. 
- Smaller MDE may not be a meaningful enough change for the business.
- Larger MDE: It's often easier to make smaller and more incremental product changes.
## Significance Level (alpha)
- False positive.
- The probability of rejecting the null hypothesis when it's actually true.
- Common values 0.05 or 0.01.
- Meaning a 5% or 1% chance of Type I error.
## Power (1-Beta)
- The probability of correctly rejecting the null hypothesis when it's false.
- Common values 0.8, 0.9
- Higher power also increases the risk of a false positive.
- There is a tradeoff between significance level and power.
- Beta is the false negative (Type II Error)
- Type II Error: when we fail to reject the null hypothesis when it's actually false.
## Variance 
- Variability of the data within each group. 
- The higher the variance, larger the sample size needed. 

# Example:
## Given
- Baseline Conversion Rate: CRo: 0.05
- MDE: 20% (detect an increase from 5% to 6%)
- Significance Level (alpha): 0.05 (95% confidence)
- Power: 80% (Standard)
## Calculations
- Z-value for 95% confidence (two tailed test): 1.96
- We use two tailed test because we don't know if group A or group B is better.
  - Use one tailed test only if you know one of the groups is better.
- Z-value for 80% power: 0.84

- Baseline conversion rate CRo: 0.05
- Desired relative increase: 20%
- New conversion rate to detect: CRb = 0.05 * 1.2 = 0.06
- MDE= 0.06 - 0.05 = 0.01

`n = (2 * (1.96 + 0.84)^2 * 0.055 * (1- 0.055)) / 0.01^2`
Number of users per group: `n = 8150`
Online sample size calculator: https://clincalc.com/stats/samplesize.aspx

## Duration Calculation
- Total required sample size = 8150 * 2 = 16300
- Assume that we have 10K visitors per day.
- Baseline conversion rate is 5%.
- Test duration = 16300 / (10000 * 0.05) = 32.6 days.


