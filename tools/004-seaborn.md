# Line Charts
- `sns.lineplot(data=data)` where data is pandas DataFrame, x axis is the index column of the data frame, and y axis is the rest of columns.

# Bar Charts and Heatmaps
- `sns.barplot(x=data.index, y=data['y_column'])`
- `sns.heatmap(data=data, annot=True)` y column is the index column, and `annot=True` shows the values for each cell.

# Scatter Plots
- `sns.scatterplot(x=data['x_column'], y=data['y_column'])`
- `sns.regplot(x=data['x_column'], y=data['y_column'])` regplot is similar to scatterplot but regplot also draws a regression line.
- `sns.scatterplot(x=data['x_column'], y=data['y_column'], hue=data['category_column'])`: Color-coded scatter plots gets `hue` attribute where we set a categorical column, and each category will be shown with a different color.
- `sns.lmplot(x="x_column", y="y_column", hue="category_column", data=data)` similar to the plot above, but adds regression lines for each category in category_column
- `sns.swarmplot(x=data['category_column'], y=data['y_column'])` We can use this when x column is a categorical column.

# Distributions (Histograms, and Density Plots)
- `sns.distplot(a=data['x_column'], kde=False)` shows histogram for the given column.
- `sns.kdeplot(data=data['x_column'], shade=True)` KDE plot also shows the distribution. It is like smoothed histogram.
- `sns.jointplot(x=data['x_column'], y=data['y_column'], kind="kde")` Two-dimensional (2D) KDE plot. Shows the relation of two columns by
using  color-coding.

- We can also show distributions of different columns in a single plot as below;

```
sns.distplot(a=data['x1_column'], label="X1", kde=False)
sns.distplot(a=data['x2_column'], label="X2", kde=False)
sns.distplot(a=data['x3_column'], label="X3", kde=False)
plt.title("Histogram of X'es")
plt.legend()
```

# Choosing Plot types

## Trends
- A trend is defined as a pattern of change.
- `sns.lineplot` - Line charts are best to show trends over a period of time, and multiple lines can be used to show trends in more than one group.

##  Relationship
- There are many different chart types that you can use to understand relationships between variables in your data.
- `sns.barplot` - Bar charts are useful for comparing quantities corresponding to different groups.
- `sns.heatmap` - Heatmaps can be used to find color-coded patterns in tables of numbers.
- `sns.scatterplot` - Scatter plots show the relationship between two continuous variables; if color-coded, we can also show the relationship with a third categorical variable.
- `sns.regplot` - Including a regression line in the scatter plot makes it easier to see any linear relationship between two variables.
- `sns.lmplot` - This command is useful for drawing multiple regression lines, if the scatter plot contains multiple, color-coded groups.
- `sns.swarmplot` - Categorical scatter plots show the relationship between a continuous variable and a categorical variable.

## Distribution
- We visualize distributions to show the possible values that we can expect to see in a variable, along with how likely they are.
- `sns.distplot` - Histograms show the distribution of a single numerical variable.
- `sns.kdeplot` - KDE plots (or 2D KDE plots) show an estimated, smooth distribution of a single numerical variable (or two numerical variables).
- `sns.jointplot` - This command is useful for simultaneously displaying a 2D KDE plot with the corresponding KDE plots for each individual variable.
