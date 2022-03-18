# Simple Machine Learning workflow

This can be adapted to solve many ML problems. It has plenty of shortcomings, but can work surprisingly well as-is. Main shortcomings include:
- Assumes all columns have proper data types
- May include irrelevant or improper features
- Does not handle text or date columns well
- Does not include feature engineering
- Ordinal encoding may be better
- Other imputation strategies may be better
- Numeric features may not need scaling
- A different model may be better

## Load data

```python
import pandas as pd

cols = ['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

# Train data
df = pd.read_csv('http://bit.ly/kaggletrain')
X = df[cols]
y = df['Survived']

# Test data
df_new = pd.read_csv('http://bit.ly/kaggletest', nrows=10)
X_new = df_new[cols]
```

## ML imports

```python
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
```

## Preprocessing

```python
# set up preprocessing for numeric columns
imp_median = SimpleImputer(strategy='median', add_indicator=True)
scaler = StandardScaler()

# set up preprocessing for categorical columns
imp_constant = SimpleImputer(strategy='constant')
ohe = OneHotEncoder(handle_unknown='ignore')

# select columns by data type
num_cols = make_column_selector(dtype_include='number')
cat_cols = make_column_selector(dtype_exclude='number')

# do all preprocessing
preprocessor = make_column_transformer(
    (make_pipeline(imp_median, scaler), num_cols),
    (make_pipeline(imp_constant, ohe), cat_cols))
```

## Create pipeline
```python
# create a pipeline
pipe = make_pipeline(preprocessor, LogisticRegression())

# cross-validate the pipeline
cross_val_score(pipe, X, y).mean()
```

## Fitting and making predictions
```python
# fit the pipeline and make predictions
pipe.fit(X, y)
pipe.predict(X_new)
```
