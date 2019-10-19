Title: Deploy a Flask Application on an Ubuntu VPS (DigitalOcean)
Date: 2018-01-25 14:14
Authors: José Aniceto


This page details the process of seting up a Ubuntu VPS (in this case a DigitalOcean dropplet using Ubuntu 16.04 was used) to serve a Flask based websiite. MySQL databases are used.


## 1) Install Apache
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install apache2
```

You can do a spot check right away to verify that everything went as planned by visiting your server's public IP address in your web browser. You will see the default Ubuntu 16.04 Apache web page.
```
http://your_server_IP_address
```

### How To Find your Server's Public IP Address
Usually, this is the address you use to connect to your server through SSH. However you can find the IP address from the command line by typing this:
```
$ ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
```

Alternatively you can use `curl` to contact an outside party to tell you how it sees your server. You can do this by asking a specific server what your IP address is:
```
$ sudo apt-get install curl
$ curl http://icanhazip.com
```

## 2) Install MySQL
```
$ sudo apt-get install mysql-server mysql-client
```
During the installation, your server will ask you to select and confirm a password for the MySQL "root" user. This is an administrative account in MySQL that has increased privileges. Think of it as being similar to the root account for the server itself (the one you are configuring now is a MySQL-specific account, however). Make sure this is a strong, unique password, and do not leave it blank.

**Optional:** Run a simple security script that will remove some dangerous defaults and lock down access to our database system a little bit. See more info on this on reference [2].
```
$ mysql_secure_installation
```

## 3) Install and enable mod_wsgi
WSGI (Web Server Gateway Interface) is an interface between web servers and web apps for python. Mod_wsgi is an Apache HTTP server mod that enables Apache to serve Flask applications.
```
$ cd /var/www
```
Copy in your Flask app directory struture. It should look like this:
```
|----FlaskApp
|---------FlaskApp
|--------------static
|--------------templates
|--------------__init__.py
```

## 4) Install Flask and virtualenv 
Install `pip`
```
$ sudo apt-get install python-pip 
```

Install `virtualenv` and create a new virtual environment names `venv` for the Flask app
```
$ sudo pip install virtualenv 
$ cd /var/www/FlaskApp/FlaskApp
$ sudo virtualenv venv
$ source venv/bin/activate 
```

Install `Flask` and other necessary Flask plug-ins and extensions
```
$ sudo pip install Flask 
$ sudo pip install flask-mysqldb
$ sudo pip install Flask-WTF
$ sudo pip install passlib
```

Test if the installation is successful and the app is running:
```
$ sudo python __init__.py 
```
It should display “Running on http://localhost:5000/” or "Running on http://127.0.0.1:5000/". If you see this message, you have successfully configured the app.

To deactivate the environment, give the following command:
```
$ deactivate
```

## 5) Configure and Enable a New Virtual Host
```
$ sudo nano /etc/apache2/sites-available/FlaskApp.conf
```

Add the following lines of code to the file to configure the virtual host. Be sure to change the ServerName to your domain or cloud server's IP address:

```
<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAlias www.mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Enable the virtual host with the following command:
```
$ sudo a2ensite FlaskApp
```

## 6) Create the .wsgi File
```
$ cd /var/www/FlaskApp
$ sudo nano flaskapp.wsgi 
```

Add the following lines of code to the flaskapp.wsgi file:
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```

## 7) Restart Apache
```
$ sudo service apache2 restart 
```

To view your application, open your browser and navigate to the domain name or IP address that you entered in your virtual host configuration.

## Final directory structure
```
|--------FlaskApp
|----------------FlaskApp
|-----------------------static
|-----------------------templates
|-----------------------venv
|-----------------------__init__.py
|----------------flaskapp.wsgi
```

## Useful references:
1) [How To Deploy a Flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
2) [How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04)
3) [Initial Server Setup with Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
4) [Building a Flask site](blob/master/python/flask.md)
