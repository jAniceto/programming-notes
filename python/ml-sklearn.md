# ML with `scikit-learn`

## Loading and saving data

## Loading data from CSV with pandas:

```python
import pandas as pd

df = pd.read_csv('path/to/csvfile.csv')

```

## Save pandas.Dataframe to CSV:

```python
df.to_csv('path/to/csvfile.csv', index=False)
```


## Data preparation

### Removing unwanted columns:

```python
df.drop(columns=['x3', 'x4'], inplace=True)
```

### Removing rows with missing data:

```python
df.dropna(inplace=True)
```


### Separate the variables/descriptors/features (x1, x2, x3,...) and targets (y):

```python
variables = df.drop(columns=['y'])  # select the target from the original dataframe
target = pd.DataFrame(df['y'])  # select the target from the original dataframe
```


### Replace the inf and -inf with nan (may be required for later imputation):

```python
import numpy as np

variables = variables.replace({np.inf: np.nan, -np.inf: np.nan})
```

### Split data into training and testing sets:

```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(variables, target, test_size=0.3, random_state=42)
```

- `test_size` - fraction of data to be reserved for testing (between 0 and 1)
- `random_state` - setting a random state guarantees the same result every time the command is run. Otherwise, since a random split is performed each time the command `train_test_split` runs.