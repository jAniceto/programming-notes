# Saving Scikit-learn model for reuse

Saving the model with Pickle allows you to recover the full Scikit-learn estimator object however some compatibility issues may occur if using different versions of sklearn. Other methods of saving models can deploy the model for prediction, usually by using tools supporting open model interchange formats but do not allow the recovery of the full Scikit-learn estimator object.

## Using Pickle

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

## References:
- [Scikit-learn docs](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Machine Learning — How to Save and Load scikit-learn Models](https://medium.com/datadriveninvestor/machine-learning-how-to-save-and-load-scikit-learn-models-d7b99bc32c27)
- [Save and Load Machine Learning Models in Python with scikit-learn](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)
