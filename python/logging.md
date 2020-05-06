# Logging

Pyhton standard library comes with a powerful logging module.

## Usage

By default, there are 5 standard levels indicating the severity of events: `DEBUG`, `INFO`, `WARNING`, `ERROR` and `CRITICAL`. 
The default logger configurarion will log all events with level `WARNING` or above. Example:

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Outputs:
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message
```

### Configurating the logger

```python
import logging

logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will log every log level to a file.')
```

Adding time info:

```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')
```

## References:

- [Logging in Python](https://realpython.com/python-logging/)
- [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
