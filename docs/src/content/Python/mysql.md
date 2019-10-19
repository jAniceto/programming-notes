Title: Using MySQL in Python
Date: 2017-08-04 11:13
Authors: José Aniceto
Modified: 2017-09-06 23:09

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


## Copying a database to another server

1. One the server where the DB is located make a backup file by running the following command (on Windows it may be necessary to `cd Program Files/MySQL/MySQL Server 5.1/bin` first: 

   `mysqldump -u root -p database_name > C:\Users\USER\Desktop\database_name.sql`

   Alternatively: `mysqldump -u[root] -p[password] database_123 > C:\Users\USER\Desktop\database_123.sql`

   If getting an "Access Denied" it message probably means you are outputing to a directory where you have no permission to create files.

2. On the second server create a new database using the same database name:

   `mysql -u root -p` to start the MySQL shell

   `CREATE DATABASE database_123;` to create the new DB

3. Copy the created backup to the second server and import it:

   `mysql -u[root] -p[password] database_name < database_name.sql`



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
