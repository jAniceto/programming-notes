# Machine Learning with `scikit-learn`

This document compiles some code snippets that cover the process of training a Machine Learning model using the [`scikit-learn`](https://scikit-learn.org) Python library.

Required Python libraries to run this code:
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [matplotlib](https://matplotlib.org/)


Useful resources:
- [scikit-learn documentation](https://scikit-learn.org/stable/index.html)
- A. Geron (2021) Hands-On Machine Learning with Scikit-Learn, Keras & Tensorflow, O'Reilly, 2nd Ed.
- [JPS Aniceto et al. (2021) Machine learning models for the prediction of diffusivities in supercritical CO2 systems, Journal of Molecular Liquids.](https://www.sciencedirect.com/science/article/pii/S0167732221000076)
- [JPS Aniceto et al. (2021) Predictive Models for the Binary Diffusion Coefficient at Infinite Dilution in Polar and Nonpolar Fluids, Materials.](https://www.mdpi.com/1996-1944/14/3/542)


Some nomenclature used here:
- `x_train` - training set variables/descriptors/features values. Size is [*number of data points*] x [*number of features*].
- `y_train` - training set targets. Size is [*number of data points*] x [*number of targets*]. Usually the *number of targets* is 1.
- `x_test` - test set variables/descriptors/features values. Size is [*number of data points*] x [*number of features*].
- `y_test` - test set targets. Size is [*number of data points*] x [*number of targets*]. Usually the *number of targets* is 1.


## Loading and saving data

### Loading data from CSV with pandas:

```python
import pandas as pd

df = pd.read_csv('path/to/csvfile.csv')
```

### Save pandas.Dataframe to CSV:

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
- `random_state` - selects the random seed. Setting a random state guarantees the same result every time the command is run. Otherwise, since a random split is performed each time the command `train_test_split` runs.


## Scale data

Most ML algorithms require that their input data is scaled into the same range/dimensions. There are several scaler available in `sklearn`, below and example is shown using `MinMaxScaler`. The `MinMaxScaler` transform the variables by scaling each variables to a given range, usually between 0 and 1.  

```python
from sklearn.preprocessing import MinMaxScaler

# Create the scaler object with a range of 0-1
scaler = MinMaxScaler(feature_range=(0, 1))

# Fit on the training data
scaler.fit(x_train)

# Transform both the training and testing data
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Convert y to one-dimensional array (vector)
y_train = np.array(y_train).reshape((-1, ))
y_test = np.array(y_test).reshape((-1, ))
```


## Train a model

### 1) Train using default options

An example using the [Gradient Boosting regression](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html).

```python
from sklearn.ensemble import GradientBoostingRegressor

# Create the model instance
model = GradientBoostingRegressor(random_state=42)

# Fit model to training data
model.fit(x_train, y_train)

# Use the fitted model to predict the target on the test data
y_test_pred = model.predict(x_test)

# Evaluate the model using the coefficient of determination of the prediction (R^2)
R2 = model.score(x_test, y_test
```

### 2) Train the model with hyperparameter tuning

Most ML models have a series of intrinsic parameters that are not fitted to the data but must instead be defined beforehand (before training can commence). These are called **hyperparameters**. Hyperparameter tuning is the process of choosing the optimal hyperparamters for the working problem.

We start by defining the values of the hyperparamters that we wish to try. Here we will test the following hyperparamters of the Gradient Boosting regression model.

```python
# Loss function to be optimized
loss = ['ls', 'lad', 'huber']

# Number of trees used in the boosting process
n_estimators = [100, 500, 900, 1100, 1500]

# Maximum depth of each tree
max_depth = [2, 3, 5, 10, 15]

# Minimum number of samples per leaf
min_samples_leaf = [1, 2, 4, 6, 8]

# Minimum number of samples to split a node
min_samples_split = [2, 4, 6, 10]

# Maximum number of features to consider for making splits
max_features = ['auto', 'sqrt', 'log2', None]

# Define the grid of hyperparameters to search
hyperparameter_grid = {'loss': loss,
                       'n_estimators': n_estimators,
                       'max_depth': max_depth,
                       'min_samples_leaf': min_samples_leaf,
                       'min_samples_split': min_samples_split,
                       'max_features': max_features}
```

#### Hyperparameter tuning with Random Search Cross Validation

A [Random Search Cross Validation (RandomizedSearchCV)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) performs a randomized search on hyperparameters. In contrast to GridSearchCV, not all combinations of parameter values are tried out, but rather a fixed number of parameter settings is sampled. The number of parameter settings that are tried is given by `n_iter`.

```python
from sklearn.model_selection import RandomizedSearchCV

# Create the model to use for hyperparameter tuning
model = GradientBoostingRegressor(random_state=42)

# Set up the random search with 4-fold cross validation
random_cv = RandomizedSearchCV(estimator=model,
                               param_distributions=hyperparameter_grid,
                               cv=4, 
                               n_iter=200, 
                               scoring='neg_mean_absolute_error',
                               n_jobs=-1, 
                               verbose = 1, 
                               return_train_score=True,
                               random_state=42)

# Fit on the training data
random_cv.fit(x_train, y_train)

# Print best hyperparameters found with Random Search
print("Best Hyperparameters:\n\n", random_cv.best_params_)

# Select the best model
best_random_cv_model = random_cv.best_estimator_
```

#### Hyperparameter tuning with Grid Search Cross Validation

A [Grid Search Cross Validation (GridSearchCV)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) performs an exhaustive search over specified parameter values for an estimator.

```python
from sklearn.model_selection import GridSearchCV

# Create the model to use for hyperparameter tuning
model = GradientBoostingRegressor(random_state=42)

# Set up the grid search with 4-fold cross validation
grid_cv = GridSearchCV(estimator=model,
                       param_grid=hyperparameter_grid,
                       cv=4, 
                       scoring='neg_mean_absolute_error',
                       n_jobs=-1, 
                       verbose=1, 
                       return_train_score=True,
                       random_state=42)

# Fit on the training data
grid_cv.fit(x_train, y_train)

# Print best hyperparameters found with Grid Search
print("Best Hyperparameters:\n\n", grid_cv.best_params_)

# Select the best model
best_grid_cv_model = grid_cv.best_estimator_
```


## Make predictions

We will select the best model obtained from the Grid Search.

```python
# Select the best model from grid search
best_model = grid_cv.best_estimator_

# Get best model prediction of testing set
best_model_y_test = best_model.predict(x_test)
```

## Plot Experimental vs Calculated

Create a plot of **experimental vs calculated** values (also called **true vs predicted**). Points falling on the diagonal represent cases where the prediction is accurate.

```python
import matplotlib.pyplot as plt

# Determine the upper range of the plot regarding the target
max_val = np.max([np.max(y_test), np.max(best_model_y_test)])
    
# Plot diagonal line
plt.plot([0, max_val], [0, max_val], '-')

# Plot results
plt.plot(y_test, best_model_y_test, 'o');

# Plot formatting
plt.ylim(0, max_val)
plt.ylabel('Calculated value')
plt.xlim(0, max_val)
plt.xlabel('Experimental value')
plt.ticklabel_format(style='sci', scilimits=(0,0))
```
