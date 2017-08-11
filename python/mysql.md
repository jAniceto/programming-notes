# Using MySQL in Python

### Some basic MySQL commands

In MySQL a `DATABASE` is composed by one or more `TABLE`s. Typically you create a database for each project.

##### To create a new MySQL database named `database_name` (the starting point of a new project using MySQL):

```
CREATE DATABASE database_name;
```

Show all databases:  `SHOW DATABASES;`

##### To start using a database you must:

`USE database_name;`

##### To create a new table named users (an example):

```
CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

Show all tables:  `SHOW TABLES;`

Get info on a TABLE (in this example users): `DESCRIBE users;`

##### Add data to table via command:

```
INSERT INTO users(name, email, username, password) VALUES(x, x, x, x)
```

##### Typical queries:

`SELECT * FROM users;`  Select all rows from users table


## Usage in Python

#### Configuring in MySQL in Flask:
```python
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_DB'] = 'flaskappdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # useful to return queries as dictionaries

# Initialize MySQL
mysql = MySQL(app)
```

Create cursor:  `cursor = mysql.connection.cursor()`

Execute a MySQL command:  `cursor.execute( command )`

Add data:  `cursor.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (x, x, x, x))`

Commit to database:  `mysql.connection.commit()`

Close:  `cursor.close()`

#### Check DB for a login: 
```python
result = cursor.execute("SELECT * FROM users WHERE username = %s", [username])`
data = cursor.fetchone()
```
