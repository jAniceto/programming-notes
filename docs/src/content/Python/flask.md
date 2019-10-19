Title: Building a Flask site
Date: 2017-08-07 12:00
Authors: José Aniceto


### Installing Flask and other usefull Python modules
```
pip install Flask
pip install flask-mysqldb
pip install Flask-WTF
pip install passlib
```

### Project file structure
```
/flask-site
    /venv
    /flask-site
        __init__.py
        /static
            style.css
        /templates
            layout.html
            index.html
            about.html
            ...
```

### The `__init__.py` file

```python
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')
    
# About page route
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

```
