# Saving Scikit-learn model for reuse

Saving the model with Pickle or Joblib allows you to recover the full Scikit-learn estimator object however some compatibility issues may occur if using different versions of sklearn. Other methods of saving models can deploy the model for prediction, usually by using tools supporting open model interchange formats but do not allow the recovery of the full Scikit-learn estimator object.

## Index
* [Using Joblib](#using-joblib)
* [Using Pickle](#using-pickle)
* [Saving a complete ML pipeline](#saving-a-complete-ml-pipeline)


## Using Joblib

Joblib is part of the SciPy ecosystem and provides utilities for pipelining Python jobs. It provides utilities for saving and loading Python objects that make use of NumPy data structures, efficiently. This can be useful for some machine learning algorithms that require a lot of parameters or store the entire dataset (like k-Nearest Neighbors).

```python
from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)
SVC()
```

Saving and reusing the model: 
```python
# Save
from joblib import dump
dump(clf, 'filename.joblib') 

# Load
from joblib import load
clf = load('filename.joblib') 
```


## Using Pickle

Pickle is the standard way of serializing objects in Python. You can use the pickle operation to serialize your machine learning algorithms and save the serialized format to a file. Later you can load this file to deserialize your model and use it to make new predictions.

Train the model:

```python
from sklearn import svm
from sklearn import datasets

clf = svm.SVC(gamma='scale')
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  
```

Saving and reusing the model: 

```python
import pickle

# Save to file
pickle.dump(clf, open('model.sav', 'wb'))

# Load from file
clf2 = pickle.load(open('model.sav', 'rb'))

# Reuse
clf2.predict(X[0:1])

y[0]
```

## Saving a complete ML pipeline

Often it is useful, not only saving the ML model, but also other required component lique the scaler used. In the following you can use `joblib` or `pickle`. The point is to create a pipeline so that you don't have to separately call the scaler.

Create the pipeline:
```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib

pipeline = make_pipeline(MinMaxScaler(),YOUR_ML_MODEL() )

model = pipeline.fit(X_train, y_train)
```

Save:
```python
joblib.dump(model, 'filename.mod') 
```

Load:
```python
model = joblib.load('filename.mod')
```


## References:
- [Scikit-learn docs](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Machine Learning — How to Save and Load scikit-learn Models](https://medium.com/datadriveninvestor/machine-learning-how-to-save-and-load-scikit-learn-models-d7b99bc32c27)
- [Save and Load Machine Learning Models in Python with scikit-learn](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)
