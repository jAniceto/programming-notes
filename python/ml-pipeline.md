# Pipelines

A pipeline chains together multiple steps, meaning the output of each step is used as input to the next step.

## Creating a pipeline

Load data:
```python
import pandas as pd
import numpy as np

train = pd.DataFrame({'feat1':[10, 20, np.nan, 2], 'feat2':[25., 20, 5, 3], 'label':['A', 'A', 'B', 'B']})
test = pd.DataFrame({'feat1':[30., 5, 15], 'feat2':[12, 10, np.nan]})
```

Defining steps:
```python
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

imputer = SimpleImputer()
clf = LogisticRegression()
```

Create a 2-step pipeline. Impute missing values, then pass the results to the classifier:
```python
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(imputer, clf)
```

Using the pipeline:
```python
features = ['feat1', 'feat2']
X, y = train[features], train['label']
X_new = test[features]

# pipeline applies the imputer to X before fitting the classifier
pipe.fit(X, y)

# pipeline applies the imputer to X_new before making predictions
# note: pipeline uses imputation values learned during the "fit" step
pipe.predict(X_new)
```

## `make_pipeline` vs `Pipeline`

`Pipeline` requires naming of steps while `make_pipeline` does not.

With `make_pipeline`:
```python
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(imputer, clf)
```

With `Pipeline`:
```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([('preprocessor', imputer), ('classifier', clf)])
```

## Examine the intermediate steps in a Pipeline
Use the `named_steps` attribute as `pipe.named_steps.STEP_NAME.ATTRIBUTE`:

```python
pipe.named_steps.imputer.statistics_ 
# or
pipe.named_steps.preprocessor.statistics_ 
```

If using `make_pipeline` the name of the step is the name of the variable (here `imputer`). When using `Pipeline` the name is the assigned name when creating the pipeline (here `preprocessor`).

## Cross-validate and grid search an entire pipeline

Cross-validate the entire pipeline (not just the model):
```python
from sklearn.model_selection import cross_val_score

cross_val_score(pipe, X, y, cv=5, scoring='accuracy').mean()
```

Find optimal tuning parameters for the entire pipeline:
```python
# specify parameter values to search
params = {}
params['columntransformer__countvectorizer__min_df'] = [1, 2]
params['logisticregression__C'] = [0.1, 1, 10]
params['logisticregression__penalty'] = ['l1', 'l2']

# try all possible combinations of those parameter values
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(pipe, params, cv=5, scoring='accuracy')
grid.fit(X, y);
```

Best score found during the search:
```python
grid.best_score_
```

Combination of parameters that produced the best score:
```python
grid.best_params_
```

## Pipeline diagram

Create interactive diagrams of Pipelines (and other estimators):
```python
from sklearn import set_config
set_config(display='diagram')

pipe = make_pipeline(ct, selection, logreg)
pipe
```

Export the diagram to an HTML file:
```python
from sklearn.utils import estimator_html_repr

with open('pipeline.html', 'w') as f:  
    f.write(estimator_html_repr(pipe))
```

## Operate on part of a Pipeline

Slice the Pipeline using Python's slicing notation:

```python
# access step 0 (preprocessor)
pipe[0].fit_transform(X)

# access steps 0 and 1 (preprocessor and feature selector)
pipe[0:2].fit_transform(X, y)

# access step 1 (feature selector)
pipe[1].get_support()
```


## References
- [scikit-learn tips](https://github.com/justmarkham/scikit-learn-tips)

