# Docker

## Basic commands

To check status of all containers:

```bash
docker ps
```

Add the `-a` flag to include stopped containers.

Stop a container:

```bash
docker stop container_name
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


## Set up Docker and Docker Compose

See [Set up Docker and Docker Compose](homeserver/setup-docker.md).



## Start containers automatically

### Using restart policies

Docker provides [restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/) to control whether your containers start automatically when they exit, or when Docker restarts.

The following command starts container named `containername` and configures it to always restart, unless the container is explicitly stopped, or the daemon restarts.

```bash
docker run -d --restart always containername
```

The following command changes the restart policy for an already running container:

```bash
docker update --restart always containername
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