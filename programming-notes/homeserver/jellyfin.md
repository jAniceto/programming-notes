# Set up Jellyfin

## Installing in Docker container

<sub><sup>Reference: [Jellyfin Container Installation](https://jellyfin.org/docs/general/installation/container)</sub></sup>

Create persistent storage for configuration and cache data.

Either create two directories on the host and use bind mounts:

```bash
mkdir /path/to/config
mkdir /path/to/cache
```

or create two persistent volumes:

```bash
docker volume create jellyfin-config
docker volume create jellyfin-cache
```

Create a `docker-compose.yml` file with the following contents.

```
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    network_mode: 'host'
    volumes:
      - /path/to/config:/config
      - /path/to/cache:/cache
      - type: bind
        source: /path/to/media
        target: /media
      - type: bind
        source: /path/to/media2
        target: /media2
        read_only: true
    restart: 'unless-stopped'
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Jellyfin will be available at `http://hostname:8096`.~
