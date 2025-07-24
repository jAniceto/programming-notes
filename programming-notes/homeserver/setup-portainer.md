# Set up Portainer

<sub><sup>Reference: [Install Portainer CE](https://docs.portainer.io/start/install-ce)</sub></sup>

<sub><sup>Install Portainer CE > Set up a new Portainer CE Server installation > Docker Standalone > Install Portainer CE with Docker on Linux</sub></sup>

## Installing

Create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Download and install the Portainer Server container:

```bash
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
```

!!! Note

    By default, Portainer generates and uses a self-signed SSL certificate to secure port 9443. Alternatively you can provide your own SSL certificate during installation or via the Portainer UI after installation is complete.

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`.

Log in with at `https://hostname:9443`.


