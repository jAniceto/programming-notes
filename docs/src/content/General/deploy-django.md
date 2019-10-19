Title: Deploy a Django app in an Ubuntu VPS (DigitalOcean)
Date: 2018-06-06 23:29
Authors: José Aniceto
Modified: 2018-06-13 14:31

This guide will demonstrate how to install and configure some components on Ubuntu 16.04 to support and serve Django applications. We will be setting up a PostgreSQL database and configure the Gunicorn application server to interface with our applications. We will then set up Nginx to reverse proxy to Gunicorn, giving us access to its security and performance features to serve our apps.

## 1) Initial Server Setup

Perform the initial server setup as detailed [here](server-setup.md).

## 2) Install the Packages from the Ubuntu Repositories

We need to update the local apt package index and then download and install the packages. The packages we install depend on which version of Python your project will use.

If you are using Django with Python 3, type:
```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev nginx
```

This will install pip, the Python development files needed to build Gunicorn later and the Nginx web server.

## 3) Install the Database

Install the database system and the libraries needed to interact with it.

#### For Postgres: 
```
$ sudo apt-get install postgresql postgresql-contrib`
```

#### For MySQL
```
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install mysql-server mysql-client
```

Now let's create the Database and User but first verify that the MySQL service is running:
```
$ systemctl status mysql.service
```

If the output is negative you can run `sudo systemctl start mysql` to get `mysql.service` started again. Now you can log in with your MySQL credentials using the following command. Where `-u` is the flag for declaring your username and `-p` is the flag that tells MySQL that this user requires a password:
```
$ sudo mysql -u db_user -p
```

```mysql
mysql> SHOW DATABASES;
mysql> CREATE DATABASE project_db;
mysql> SHOW DATABASES;
```

Whenever you'd like to exit MySQL server, press CTRL + D.

## 4) Create a Python Virtual Environment

```
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv
```

```
$ mkdir ~/myproject
$ cd ~/myproject
$ virtualenv venv
$ source venv/bin/activate
```

Note: Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).

Install the `mysqlclient` library:
```
$ pip install mysqlclient
```

With your virtual environment active, install Django and Gunicorn:
```
$ pip install django gunicorn
```

## 5) Create Django project

Since we already have a project directory, we will tell Django to install the files here. It will create a second level directory with the actual code, which is normal, and place a management script in this directory. The key to this is that we are defining the directory explicitly instead of allowing Django to make decisions relative to our current directory:
```
$ django-admin startproject myproject ~/myproject
```

At this point, your project directory (~/myproject in our case) should have the following content:
```
~/myproject/manage.py: A Django project management script.
~/myproject/myproject/: The Django project package. This should contain the __init__.py, settings.py, urls.py, and wsgi.py files.
~/myproject/myprojectenv/: The virtual environment directory we created earlier.
```

Go to the end of the `settings.py` file and add `STATIC_ROOT` as shown below:
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Add your server’s IP address between the square brackets and single quotes to the `ALLOWED_HOSTS`:
```python
# The simplest case: just add the domain name(s) and IP addresses of your Django server
# ALLOWED_HOSTS = [ 'example.com', '203.0.113.5']
# To respond to 'example.com' and any subdomains, start the domain with a dot
# ALLOWED_HOSTS = ['.example.com', '203.0.113.5']
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . .]
```

Migrate the initial database schema to our database using the management script:

```
(venv) $ python ~/myproject/manage.py makemigrations
(venv) $ python ~/myproject/manage.py migrate
```
Create an administrative user for the project by typing:
```
(venv) $ ~/myproject/manage.py createsuperuser
```

We can collect all of the static content into the directory location we configured by typing:
```
(venv) $ ~/myproject/manage.py collectstatic
```

The static files will then be placed in a directory called static within your project directory.

#### Connect your Django app to MySQL

Navigate to the settings.py file and replace the current DATABASES lines with the following. We will configure your database dictionary so that it knows to use MySQL as your database backend and from what file to read your database connection credentials:

```python
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
```

Next, let’s edit the config file so that it has your MySQL credentials. Use nano as sudo to edit the file and add the following information:
```
$ sudo nano /etc/mysql/my.cnf
```
```
[client]
database = db_name
user = db_user
password = db_password
default-character-set = utf8
```

Where database name in our case is mysite, your username for the MySQL server is the one you’ve created, and the password is the MySQL server password you’ve created. Also, you’ll notice that utf8 is set as the default encoding, this is a common way to encode unicode data in MySQL. Once the file has been edited, we need to restart MySQL for the changes to take effect.
```
$ systemctl daemon-reload
$ systemctl restart mysql
```

Please note that restarting MySQL takes a few seconds, so please be patient. Now, let's test the MySQL connection to the application. We need to verify that the configurations in Django detect your MySQL server properly. We can do this by simply running the server. If it fails, it means that the connection isn’t working properly. Otherwise, the connection is valid.
```
$ cd ~/mysite/mysite/
$ python manage.py runserver your-server-ip:8000
```

## 6) Setting up Gunicorn's ability to serve the project
The last thing we want to do before leaving our virtual environment is test Gunicorn to make sure that it can serve the application. We can do this by entering our project directory and using gunicorn to load the project's WSGI module:

```
$ cd ~/myproject
$ gunicorn --bind 0.0.0.0:8000 myproject.wsgi
```

This will start Gunicorn on the same interface that the Django development server was running on. You can go back and test the app again. 

We passed Gunicorn a module by specifying the relative directory path to Django's wsgi.py file, which is the entry point to our application, using Python's module syntax. Inside of this file, a function called application is defined, which is used to communicate with the application. When you are finished testing, hit CTRL-C in the terminal window to stop Gunicorn. We're now finished configuring our Django application. We can back out of our virtual environment by typing:

```
$ deactivate
```

Create and open a systemd service file for Gunicorn with sudo privileges in your text editor:

```
$ sudo nano /etc/systemd/system/gunicorn.service
```

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=synergix
Group=www-data
WorkingDirectory=/home/synergix/myproject
ExecStart=/home/synergix/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/synergix/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

We can now start the Gunicorn service we created and enable it so that it starts at boot:
```
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
```
We can confirm that the operation was successful by checking for the socket file.
```
$ sudo systemctl status gunicorn
```
Next, check for the existence of the myproject.sock file within your project directory:
```
$ ls /home/synergix/myproject
```

If the systemctl status command indicated that an error occurred or if you do not find the myproject.sock file in the directory, it's an indication that Gunicorn was not able to start correctly. Check the Gunicorn process logs by typing:
```
$ sudo journalctl -u gunicorn
```

## 7) Configure Nginx to Proxy Pass to Gunicorn
Now that Gunicorn is set up, we need to configure Nginx to pass traffic to the process. Start by creating and opening a new server block in Nginx's sites-available directory:
```
$ sudo nano /etc/nginx/sites-available/myproject
```

Inside, open up a new server block. We will start by specifying that this block should listen on the normal port 80 and that it should respond to our server's domain name or IP address. Next, we will tell Nginx to ignore any problems with finding a favicon. We will also tell it where to find the static assets that we collected in our ~/myproject/static directory. All of these files have a standard URI prefix of "/static", so we can create a location block to match those requests. Finally, we'll create a location / {} block to match all other requests. Inside of this location, we'll include the standard proxy_params file included with the Nginx installation and then we will pass the traffic to the socket that our Gunicorn process created:
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
```

Save and close the file when you are finished. Now, we can enable the file by linking it to the sites-enabled directory:
```
$ sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```

Test your Nginx configuration for syntax errors by typing:
```
$ sudo nginx -t
```
If no errors are reported, go ahead and restart Nginx by typing:
```
$ sudo systemctl restart nginx
```

Finally, we need to open up our firewall to normal traffic on port 80. Since we no longer need access to the development server, we can remove the rule to open port 8000 as well:
```
$ sudo ufw delete allow 8000
$ sudo ufw allow 'Nginx Full'
```
You should now be able to go to your server's domain or IP address to view your application.



## 8) Troubleshooting

Logs can help narrow down root causes. Check each of them in turn and look for messages indicating problem areas. The following logs may be helpful:

* Check the Nginx process logs by typing: `sudo journalctl -u nginx`
* Check the Nginx access logs by typing: `sudo less /var/log/nginx/access.log`
* Check the Nginx error logs by typing: `sudo less /var/log/nginx/error.log`
* Check the Gunicorn application logs by typing: `sudo journalctl -u gunicorn`

As you update your configuration or application, you will likely need to restart the processes to adjust to your changes. If you update your Django application, you can restart the Gunicorn process to pick up the changes by typing:
```
$ sudo systemctl restart gunicorn
```

If you change gunicorn systemd service file, reload the daemon and restart the process by typing:

```
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
```

If you change the Nginx server block configuration, test the configuration and then Nginx by typing:
```
$ sudo nginx -t && sudo systemctl restart nginx
```


## References
* [DigitalOcean - Setup Django, Postgres, nginx and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
* [DigitalOcean - Serve Django with uwsgi and ngix on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)
* [DigitalOcean - Create Django app and connect to database](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
