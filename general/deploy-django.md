# Deploy a Django app in an Ubuntu VPS (DigitalOcean)

This guide will demonstrate how to install and configure some components on Ubuntu 16.04 to support and serve Django applications. We will be setting up a PostgreSQL database and configure the Gunicorn application server to interface with our applications. We will then set up Nginx to reverse proxy to Gunicorn, giving us access to its security and performance features to serve our apps.

## 1) Initial Server Setup

Perform the initial server setup as detailed [here](general/server-setup.md).

## 2) Install the Packages from the Ubuntu Repositories

We need to update the local apt package index and then download and install the packages. The packages we install depend on which version of Python your project will use.

If you are using Python 2, type:
```
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx
```

If you are using Django with Python 3, type:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
```

This will install pip, the Python development files needed to build Gunicorn later, the Postgres database system and the libraries needed to interact with it, and the Nginx web server.

...
