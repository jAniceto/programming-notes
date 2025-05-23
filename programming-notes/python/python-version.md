# Working with the Python version

To check the Python version installed, open a terminal window and entering the following:
```
python ––version
```

### Check for a minimum required Python version
You can check for the Python version in your code, to make sure your users are not running your script with an incompatible version. Use this simple check:
```python
if not sys.version_info > (2, 7):
   # berate your user for running a 10 year
   # python version
elif not sys.version_info >= (3, 5):
   # Kindly tell your user (s)he needs to upgrade
   # because you're using 3.5 features
```


### Check if 32 or 64 bit version

```python
if sys.maxsize > 2**32:
    print('64 bit Python version')
else:
    print('32 bit Python version')
```
