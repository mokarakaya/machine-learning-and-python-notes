
# Step 1: Define the problem
- Why is this experiment important for the company?
- What decisions will the experiment drive?
- What does the company hope to learn from it?
- Do we want to increase the purchases, CTR, attract new users etc.
# Step 2: Identify key metrics
- North Star: Company's core value or ultimate goal.
E.g. Monthly Active Users (MAU) can be a north metric.
If MAU is a north metric, and the change increases revenue but decreases MAU,
we may decide not to release the change.
- Primary Success: Closely related to North Star, but focuses on a specific aspect.
- Guardrail: Ensure that other important metrics are not negatively affected.
- Secondary: Not critical as others but used for deeper analysis, optimization.
# Step 3: Select the unit or randomization
- Unit of randomization: Ensure that the entities are assigned to groups randomly.
One assignment should not impact another.
- Select the triggering criteria: We should assign the user to a group when
they use the feature. Otherwise, it may lead to noise.
# Step 4: Formulate hypotheses
State the null and alternative hypotheses.
# Step 5: Select a statistical test
- Z-test: Comparing means to a known population mean when sample size is large (n>=30)
and population standard deviation is known. (Mostly used)
- T-test: Comparing means of two groups.
- Chi-square test: Testing independence or association between categorical variables.
- Analysis of variance (ANOVA): Comparing means of three or more groups.
# Step 6: Conduct power analysis
- To determine the sample size required.
- Main inputs:
  - Effect size: How much change do we want to detect.
  - Power: the probability of detecting a true effect, which is typically 0.8
  - Significance level (alpha): the probability of detecting false positive which
  is typically 0.05.
  - Variance: typically estimated using historical data.
Also discuss other factors such as seasonality or variability in the metric (weekends)
- Ramp-up strategy: If we want more control, we can increase the a/b test scope
gradually.
# Step 7: Analyse test results
- Making decisions before the test duration ends (sample size reached) may lead to
Type I error (false positive)
# Step 8: Evaluate and make recommendations:
- Check if all metrics such as north star, guardrail etc positive.