#  Pandas Objects
## Series
- A Pandas Series is a one-dimensional array of indexed data.
- `data = pd.Series([0.25, 0.5, 0.75, 1.0])`
- `data.values` returns Numpy array for the values of the series.
- `data.index` return the index object.
  -  `data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])`: `data['b']` returns 0.5
- We can initiate Pandas Series with Python dictionary. Keys will be indexes. We can also use `index` attribute in Series constructor.

## DataFrame

- DataFrame is as a sequence of aligned Series objects. Here, by “aligned” we mean that they share the same index.
- `a = pd.DataFrame({'column1':[1,2,3], 'column2':[4,5,6]})`
  - `a.iloc[0]` will return the first row.

## Index
- We can think of an index as an immutable array or ordered set.
- `pd.Index([2, 3, 5, 7, 11])`

# Data Selection
-  `.loc` gets rows (or columns) with particular labels from the index. `.iloc` gets rows (or columns) at particular positions in the index (so it only takes integers)
- `loc` is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
-  `iloc` is integer index-based. So here, we have to specify rows and columns by their integer index.
- Use `data['pop']` rather than `data.pop` since `data.pop` may conflict with the name of the build-in functions.


# Data Update

- `df.loc[df['Click_Id']=='A',['Click_Id','Click_Count']] = ['A1',10000]`: Update the row where Click_Id equals to A. Set Click_Id, and Click_Count to A1, and 10000.

# Index Alignment

## Series

- `A / B`: Divides A, B by their index.
- `A.index | B.index`: Union of indexes.
- `A + B`: Sum values by index.

## DataFrame

- `A + B`: Sum values by column.
- Functions also available for operations such as `A.add(B, fill_value=0)`.

# Missing Data

- In Numpy, `None` is an object and if we use None in an array the type of the array should be `dtype=object`.
- In Numpy, `NaN` is a special floating-point number and if we use it in an array the type of the array should be  float e.g. `float64`
- Pandas handles `None`, and `NaN` interchangeably where it is appropriate.
- Related functions are `isnull()`, `notnull()` (opposite of isnull), `dropna()`, `fillna()`

- To fill N/A values of column A with 0 and column B with 1;

```
values = {'A': 0, 'B': 1}
df.fillna(value=values)`

```


# Multiple Index
- Multiple Indexes helps us to represent data of multiple dimensions by using a single Series or DataFrame with a single column.
- In Pandas, a bad way to create multiple index is to use tuples in index columns. Because we can not use some easy syntax such as select and slice.
- `pd.MultiIndex.from_tuples(index)`: Better was is to use `MultiIndex`
- `unstack()` method converts multiple indexed Series into a DataFrame. `stack()` does the opposite.
- MultiIndex slicing operations will fail if the index is not sorted. `data['a':'b']` will fail (a, b are values) if we do not call `data = data.sort_index()` in advance.

# Concat
- `pd.concat([df1, df2])`. Similar to Numpy `axis=1 or axis='col'` will add new columns for df2.
- `pd.concat([df5, df6], join='inner')` will get only common columns (intersection of columns). `join=outer` will get union of columns.
- `pd.concat([df5, df6], join_axes=[df5.columns])`: We can also define the columns we want to join.
- `df1.append(df2)` works same as `pd.concat([df1, df2])`.

# Merge and Join

- `pd.merge(df1, df2)` finds out the common columns in DataFrames automatically and joins them. The joins may be one-to-one, many-to-one, or many-to-many depending on the data.
- `pd.merge(df1, df2, on='employee')`: We can also set the column to join.
- `pd.merge(df1, df3, left_on="employee", right_on="name")`: Column names to join may be different. df1 has employee and df3 has name columns.
- `pd.merge(df6, df7, how='inner')`: We can specify if we want to apply `inner` or `outer` join.
- `pd.merge(df6, df7, how='left')`: `left`, and `right` are other possible values for `how` parameter. `left` keeps all values in `df6`, and `right` keeps all values in `df7`.

# GroupBy

- GroupBy consists of 3 steps.
  - `split`: Break up on the specified value
  - `apply`: aggregate, filter, sum etc.
  - `combine`: merge results
- `df.groupby('key').sum()`: key is the column that we want to groupby. sum is the apply operation.

# Pivot Table
- `titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()`: Group by sex and class, get survived, and then get mean for each group.
- Pivot table equivalent:  `titanic.pivot_table('survived', index='sex', columns='class')`: `index` can be an array.

# eval() and query()
- `numexpr.evaluate('(x > 0.5) & (y < 0.5)')`
- In Numpy numexpr evaluates faster since it does not keep intermediate operations in memory. Pandas eval() and query() are similar and they also use numexpr internally.


# Rename columns
- `df = df.rename(columns = {'Count':'NewCount'})`: Renames column Count to NewCount.
