# Set up a Django production server with gunicorn

We are going to set up a production ready Django server using Gunicorn and manage it using systemd. 


## 1) Install Gunicorn

Inside the virtual environment with Django and all other required packages for your project run:

```
$ pip install gunicorn
```

## 2) Configure Gunicorn

In your project directory, create a file named `gunicorn_config.py` with the Gunicorn configuration for your Django project:

```python
import multiprocessing

bind = "127.0.0.1:8000"  # Replace with your desired IP and port
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2
timeout = 60
```

To test that Gunicorn can serve your Django app run:

```
$ gunicorn -c gunicorn_config.py myproject.wsgi
```

If Gunicorn starts without errors, it's working correctly. You can stop it by pressing `Ctrl + C`.

## 3) Create a `systemd` service

Create a `systemd` service file to manage the Gunicorn process. Use a text editor to create a file named `myproject_gunicorn.service` in the `/etc/systemd/system/` directory:

```
$ sudo nano /etc/systemd/system/myproject_gunicorn.service
```

Add the following content to the file, adjusting the paths and configuration as neede. Replace `your_username`, `your_group`, `/path/to/your/project`, and `/path/to/your/virtualenv` with your actual information.

```
[Unit]
Description=Gunicorn daemon for myproject
After=network.target

[Service]
User=your_username
Group=your_group
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/virtualenv/bin/gunicorn -c gunicorn_config.py myproject.wsgi
Restart=always

[Install]
WantedBy=multi-user.target
```

## 4) Enable and start the `systemd` service

Enable the systemd service and start Gunicorn:

```
$ sudo systemctl enable myproject_gunicorn
$ sudo systemctl start myproject_gunicorn
```

Check the status of the Gunicorn service to make sure it's running without errors:

```
$ sudo systemctl status myproject_gunicorn
```

If everything is configured correctly, your Django application should now be running in production using Gunicorn and managed by systemd. You can access it through the specified IP and port. Make sure to configure your web server (e.g., Nginx or Apache) as a reverse proxy to forward requests to Gunicorn for better security and performance in a production environment.

## References

- [https://dev.to/karthiknarayan/setting-up-django-for-production-using-gunicorn-on-linux-37ce](https://dev.to/karthiknarayan/setting-up-django-for-production-using-gunicorn-on-linux-37ce)
