# Docker

## Basic commands

To check status of all containers:

```bash
docker ps
docker ps -a
```

Add the `-a` flag to include stopped containers.

Stop a container:

```bash
docker stop container_name
```

If stopping doesn’t work, killing the container may also sometimes be necessary:

```bash
docker kill container_name
```

Remove a container:

```bash
docker rm container_name
```

or to stop and remove in a single step:

```bash
docker rm -f container_name
```

To remove all stopped Docker containers:

```bash
docker container prune
```

To start a container:

```bash
docker start container_name
```

To restart a container:

```bash
docker restart container_name
```


## Types of Docker storage

**Volumes**: Managed by Docker, stored in `/var/lib/docker/volumes/` (on Linux), best for most use cases.

**Bind mounts**: Maps a host directory into the container. Useful for development.

**Tmpfs**: Temporary storage in memory. Disappears after container stops.

### Volumes

Here is an example of a `docker-compose.yaml` `volumes` section with a mix of short syntax and long syntax for defining bind mounts:

```yaml
volumes:
  - /path/to/config:/config  # bind mount that maps path on your host machine (left of :) with path inside the container (right of :)
  - /path/to/cache:/cache
  - type: bind  # these 3 lines map a path on your host machine (source) with path inside the container (target)
    source: /path/to/media
    target: /media
```

Both syntax are equivalent.



## Docker Compose

See [Set up Docker and Docker Compose](homeserver/setup-docker.md).


Docker Compose allows you to define and run multi-container applications with Docker.

To builds, (re)create, start, and attach containers for a service.

```bash
docker compose up
docker compose up --build
docker compose up -d
```

The `--build` builds images before starting containers. The `-d` flag starts the containers in the background and leaves them running. The `--force-recreate` flag forces Compose to stop and recreate all containers


To remove the volumes along with the containers:

```bash
docker compose down -v
```

To access the logs:

```bash
docker compose logs
```


## Updating containers

The basic method for updating a container is to pull a newer version of the container image, remove the container, and then start a new container using the new image version. This is one reason storing data inside volumes is important. It's the only way data can survive this process.

[Watchtower](https://containrrr.dev/watchtower) is a service for keeping containers up to date (runs inside a container). It detects whenever a new version is available and automatically replaces containers with the new version using the same settings they were created with. 



## Start containers automatically

### Using restart policies

Docker provides [restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/) to control whether your containers start automatically when they exit, or when Docker restarts.

The following command starts container named `containername` and configures it to always restart, unless the container is explicitly stopped, or the daemon restarts.

```bash
docker run -d --restart unless-stopped containername
```

The following command changes the restart policy for an already running container:

```bash
docker update --restart unless-stopped containername
```

### Using a process manager

You can also use a [process manager like `systemd`](https://stackoverflow.com/a/39493500/5240904). Create the `systemd` file:

```bash
nano /etc/systemd/system/docker-myproject.service
```

```
[Unit]
Description=Docker project
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a myproject
ExecStop=/usr/bin/docker stop -t 2 myproject

[Install]
WantedBy=default.target
```

Then, enable the service at startup:

```bash
sudo systemctl enable docker-myproject.service
```

!!! warning

    Don't combine Docker restart policies with process managers, as this creates conflicts.