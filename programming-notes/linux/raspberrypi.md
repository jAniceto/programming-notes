# Set up server in Raspberry Pi

## Set up Django web app locally

Find you IP:

```
$ ifconfig
```

Run:

```
$ python manage.py runserver 192.XXX.XX.XX:8000
```

You should be able to access your web app from any device in the local network.

This will keep the web app running while the SSH connection is active. 

If you want to serve the app continously you can use `gunicorn`: 

```
$ gunicorn --bind 192.XXX.XX.XX:8000 your_project.wsgi --daemon
```


## References

- [[stackoverflow](https://stackoverflow.com/questions/13654688/what-is-the-correct-way-to-leave-gunicorn-running)](https://stackoverflow.com/questions/13654688/what-is-the-correct-way-to-leave-gunicorn-running)
