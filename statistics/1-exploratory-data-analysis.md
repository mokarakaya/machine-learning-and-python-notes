# Data Types
- Numeric
  - Continuous: float numeric.
  - Discrete: only integers such as counts.
- Categorical
  - Binary
  - Ordinal: Explicit ordering such as rating (1 to 5)

- Sklearn has OrdinalEncoder.

# Estimates of Location
- Mean
- Weighted mean
- Median (50th percentile) [1,2,3,4] -> 2.5
- Percentile

```
import numpy as np
x = [3,4,7,12,14,15,20]
perc = 35
modf = np.modf((len(x) - 1) * (perc / 100))
dec, num = modf[0],  int(modf[1])
per_c = x[num] + (dec * (x[num + 1] - x[num]))
assert per_c == np.percentile(x, perc)


```

- Weighted Median
- Trimmed Mean
  - See `scipy.stats.trim_mean`
- Robust: non-sensitive to extreme values.
  - See `sklearn.preprocessing.RobustScaler`
- Outlier

- The basic metric for location is the mean, but it can be sensitive to extreme values (outlier). Other metrics (median, trimmed mean) are less sensitive to outliers and unusual distributions and hence are more robust.

# Estimates of Variability
- Variance: The sum of squared deviations from the mean divided by n – 1 where n is the number of data values.
- Mean absolute deviation: The mean of the absolute values of the deviations from the mean.
  - Synonyms: l1-norm, Manhattan norm
- Median absolute deviation from the median: The median of the absolute values of the deviations from the median. This is robust to outliers.

# Exploring the data distribution

- Boxplot: shows median, Q1, and Q3. By default, they extend no more than 1.5 * IQR (IQR = Q3 - Q1) from the edges of the box, ending at the farthest data point within that interval. Outliers are plotted as separate dots.

- Frequency table: The function pandas.cut creates a series that maps the values into the segments. Using the method value_counts, we get the frequency table:

```
binnedPopulation = pd.cut(state['Population'], 10)
binnedPopulation.value_counts()
```

- Histogram: A histogram is a way to visualize a frequency table, `state['Population'].plot.hist()`
- Density plot: Related to the histogram is a density plot, which shows the distribution of data values as a continuous line.

```
ax = state['Murder.Rate'].plot.hist(density=True, xlim=[0,12], bins=range(1,12))
state['Murder.Rate'].plot.density(ax=ax) 1
```

# Exploring Binary and Categorical Data

## Expected Value (Weighted mean)
- A: 5% 300 , B: 15% 50, C: 80% 100
  - expected value = (0.05)(300)+(0.15)(50)+(0.80)(0)=22.5


# Correlation
- Pearson Correlation Coefficient: Multiply deviations from the mean for variable 1 times those for variable 2, and divide by the product of the standard deviations.

- Showing a correlation matrix:

```

sns.heatmap(etfs.corr(), vmin=-1, vmax=1, cmap=sns.diverging_palette(20, 220, as_cmap=True))

```

- Scatterplots is another way of showing correlation between two variables.


# Exploring two or more variables (multivariate analysis)
##  Hexagonal Binning and Contours (Plotting numeric vs numeric data)
- We can use Hexagonal binning instead of scatterplots when the data is large.
```
ax = kc_tax0.plot.hexbin(x='SqFtTotLiving', y='TaxAssessedValue',
                         gridsize=30, sharex=False, figsize=(5, 4))

```
- Contour plot is similar to scatterplot but it also shows peaks.

```
ax = sns.kdeplot(kc_tax0.SqFtTotLiving, kc_tax0.TaxAssessedValue, ax=ax)

```

## Two Categorical Variables
- We can create contingency tables to analyse categorical variables. We generally use Pivot tables to create contingency tables.

```

crosstab = lc_loans.pivot_table(index='grade', columns='status',
                                aggfunc=lambda x: len(x), margins=True) 1

```

- Another way to create contingency table is using `crosstab` function.

```
data_crosstab = pd.crosstab(data['grade'],
                            data['loan_status'],  
                               margins = False)
```
https://www.geeksforgeeks.org/contingency-table-in-python/

- The website below explains how to calculate correlation between two categorical variables by using contingency table and Chi-Square test:
https://www.geeksforgeeks.org/python-pearsons-chi-square-test/

## Categorical and Numeric Data
- Boxplot is an easy way to compare one categorical variable to a number variable

```
ax = airline_stats.boxplot(by='airline', column='pct_carrier_delay')
```

- Violin plot: Similar to boxplot but violin plot also shows the density. The advantage of a violin plot is that it can show nuances in the distribution that aren’t perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data.

```

ax = sns.violinplot(airline_stats.airline, airline_stats.pct_carrier_delay,
                    inner='quartile', color='white')

```

## Visualising Multiple Variables

- We can use `FacetGrid` to visualize multiple variables by using multiple graphs.

```

def hexbin(x, y, color, **kwargs):
    cmap = sns.light_palette(color, as_cmap=True)
    plt.hexbin(x, y, gridsize=25, cmap=cmap, **kwargs)

g = sns.FacetGrid(kc_tax_zip, col='ZipCode', col_wrap=2) 1
g.map(hexbin, 'SqFtTotLiving', 'TaxAssessedValue',
      extent=[0, 3500, 0, 700000]) 2
g.set_axis_labels('Finished Square Feet', 'Tax-Assessed Value')
g.set_titles('Zip code {col_name:.0f}')
```

- Another example:

```
g = sns.FacetGrid(attend, col="subject", col_wrap=4, height=2, ylim=(0, 10))
g.map(sns.pointplot, "solutions", "score", order=[1, 2, 3], color=".3", ci=None)
```
