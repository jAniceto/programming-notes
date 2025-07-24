# Docker

## Types of Docker storage

**Volumes**: Managed by Docker, stored in `/var/lib/docker/volumes/` (on Linux), best for most use cases.

**Bind mounts**: Maps a host directory into the container. Useful for development.

**Tmpfs**: Temporary storage in memory. Disappears after container stops.

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