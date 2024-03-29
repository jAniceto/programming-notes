# Data manipulation with `pandas`

`pandas` is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.


## Instalation

`pandas`, and other required libraries like `numpy` and the remaining scientific stack, comes pre-installed if you use the Anaconda Python distribution. 

To install via PyPI run:

```
$ pip install pandas
```

## DataFrame indexing

See [here](https://lucytalksdata.com/how-to-effectively-index-pandas-dataframes/).

## Useful snippets:

Create a test dataframe:

```python
df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])

# Output:
#    A  B   C   D
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
```

### Droping (removing) a column: [^](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)

```python
df = df.drop(columns=['B', 'C'])

# Output:
#    A   D
# 0  0   3
# 1  4   7
# 2  8  11
```

### Copying a dataframe: [^](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html)

Note that you can't copy a dataframe simply by `df2 = df`. Here df2 and df refer to the same object and any change in one will affect the other. To create a new copy of a dataframe you do:

```python
df2 = df.copy()
```

### Merge dataframes on common column [^](https://stackoverflow.com/questions/43297589/merge-two-data-frames-based-on-common-column-values-in-pandas)

```python
merged_df = pd.merge(df1, df2, on="column_name")
```

Only rows for which common keys are found are kept in both data frames. In case you want to keep all rows from the left data frame and only add values from `df2` where a matching key is available, you can use `how="left"`.

Alternatively:

```python
dfinal = df1.merge(df2, on="column_name", how ='inner')
```

### Applying a function to each row of a dataframe:

Use `dataframe.apply()` to run a function on each row, `axis=1`, (or column, `axis=0`) in a dataframe. In the example below we create a new column in the dataframe where the value for each row is the row index + 10.

```python
def function1(x):
    return x.name + 10
    
df['new_column'] = df.apply(lambda row: function1(row), axis=1)
```


## Advanced funtions

### Collinear variables: [^](https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on/61938339)

The function below finds collinear variables and removes them from dataframe. It also prints a report of the collinear pairs found.

```python
def remove_collinear_features(x, threshold):
    '''
    Objective:
        Remove collinear features in a dataframe with a correlation coefficient greater than the threshold. 
        Removing collinear features can help a model to generalize and improves the interpretability of the model.
        
    Inputs: 
        x: features dataframe
        threshold: any features with correlations greater than this value are removed
    
    Output: 
        dataframe that contains only the non-highly-collinear features
    '''
    
    # Calculate the correlation matrix
    corr_matrix = x.corr()
    iters = range(len(corr_matrix.columns) - 1)
    drop_cols = []

    # Iterate through the correlation matrix and compare correlations
    for i in iters:
        for j in range(i+1):
            item = corr_matrix.iloc[j:(j+1), (i+1):(i+2)]
            col = item.columns
            row = item.index
            val = abs(item.values)
            
            # If correlation exceeds the threshold
            if val >= threshold:
                # Print the correlated features and the correlation value
                print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
                drop_cols.append(col.values[0])

    # Drop one of each pair of correlated columns
    drops = set(drop_cols)
    x = x.drop(columns=drops)
               
    return x
```

## References

- [Pandas docs](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
- [Pandas DataFrame Indexing Explained](https://lucytalksdata.com/how-to-effectively-index-pandas-dataframes/)
