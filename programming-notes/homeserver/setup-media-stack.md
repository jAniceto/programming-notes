# Setup a media stack

This guide shows how to set up a media stack using Plex or Jellyfin and the Servarr stack. Everything is installed in Docker containers in Ubuntu Server. For more info on how to set up Ubuntu and Docker check [Ubuntu server setup](../linux/server-setup.md) and [Setup Docker](./setup-docker.md).

This guides assumes you named your host server `homeserver` and it has the following folder structure:

```
~/
|-- data/
|   |-- downloads/
|   |-- movies/
|   |-- shows/
|-- plex/
|   |-- library/
|   |-- docker-compose.yml
|-- transcode/
|   |-- temp/
```

You can start by creating these folders:

```bash
cd ~
mkdir - p data/downloads
mkdir - p data/movies
mkdir - p data/shows
```

Make sure the folders have the needed permissions and ownership by running:

```bash
sudo chown -R $USER:$USER data
sudo chmod -R 775 data
```


## Media server

### Plex

<sub><sup>Reference: [Docker Hub - Plex](https://hub.docker.com/r/linuxserver/plex)</sub></sup>

Plex is a media server software. We install the Plex server in our Ubuntu server and can stream our media to the Plex clients that can be installed in yor Android phone, your SmartTV, etc. 

We can start by adding a few more folder for Plex.

```
~/
|-- data/
|-- plex/
|   |-- library/
|   |-- docker-compose.yml
|-- transcode/
|   |-- temp/
```

```bash
cd plex
nano docker-compose.yml
```

```yaml
services:
  plex:
    image: lscr.io/linuxserver/plex:latest
    container_name: plex
    network_mode: host
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
      - VERSION=docker
    #   - PLEX_CLAIM=  # optional, get from https://account.plex.tv/claim
    volumes:
      - '/home/${USER}/plex/library:/config'
      - '/home/${USER}/data/shows:/tv'
      - '/home/${USER}/data/movies:/movies'
      - '/home/${USER}/transcode/temp>:/transcode'
    restart: unless-stopped
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Plex will be available at `http://homeserver:32400/web`.



### Jellyfin

<sub><sup>Reference: [Jellyfin Container Installation](https://jellyfin.org/docs/general/installation/container)</sub></sup>

An open-source alternative to Plex is Jellyfin.

Create persistent storage for configuration and cache data. Create two directories on the host and use bind mounts:

```bash
cd ~
mkdir -p jellyfin/config
mkdir -p jellyfin/cache
mkdir data
```

Create a `docker-compose.yml` file with the following contents.

```bash
cd jellyfin
nano docker-compose.yml
```

```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    network_mode: 'host'
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/jellyfin/config:/config'
      - '/home/${USER}/jellyfin/cache:/cache'
      - '/home/${USER}/data/:/cache'
      - type: bind
        source: '/home/${USER}/data'
        target: /data
    restart: 'unless-stopped'
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Jellyfin will be available at `http://homeserver:8096`.



## Servarr stack


### Radarr

Radarr is a movie collection manager.

Create a `docker-compose.yml` file with the following contents.

```bash
cd radarr
nano docker-compose.yml
```

```yaml
services:
  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/radarr/data:/config'
      - '/home/${USER}/media/movies:/movies' # optional
      - '/home/${USER}/media/downloads:/downloads' # optional
    ports:
      - 7878:7878
    restart: unless-stopped
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Radarr will be available at `http://homeserver:7878`.


### Prowlarr

```yaml
services:
  prowlarr:
    image: lscr.io/linuxserver/prowlarr:latest
    container_name: prowlarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/prowlarr/data:/config'
    ports:
      - 9696:9696
    restart: unless-stopped
```

### Sonarr



```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/sonarr/data:/config'
      - '/home/${USER}/media/shows:/tv' # optional
      - '/home/${USER}/media/downloads:/downloads' # optional
    ports:
      - 8989:8989
    restart: unless-stopped
```


### Bazarr

Bazarr is a companion application to Sonarr and Radarr to manage and download subtitles.

Create a `docker-compose.yml` file with the following contents.

```bash
cd bazarr
nano docker-compose.yml
```

```yaml
services:
  bazarr:
    image: lscr.io/linuxserver/bazarr:latest
    container_name: bazarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/bazarr/config:/config'
      - '/home/${USER}/media/movies:/movies' # optional
      - '/home/${USER}/media/shows:/tv' # optional
    ports:
      - 6767:6767
    restart: unless-stopped
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Bazarr will be available at `http://homeserver:6767`.



### Overseerr

Overseerr is a request management and media discovery for Plex media server.

Create a `docker-compose.yml` file with the following contents.

```bash
cd overseerr
nano docker-compose.yml
```

```yaml
services:
  overseerr:
    image: sctx/overseerr:latest
    container_name: overseerr
    environment:
      - LOG_LEVEL=debug
      - TZ=Europe/Lisbon
      - PORT=5055 #optional
    ports:
      - 5055:5055
    volumes:
      - '/home/${USER}/overseerr/config:/config'
    restart: unless-stopped
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Overseerr will be available at `http://homeserver:5055`.



## Complete Docker Compose

The following `docker-compose.yml` will install:

- Plex
- Radarr, Sonarr, Prowlarr, Bazarr, and Overseerr


```yaml
services:
  plex:
    image: lscr.io/linuxserver/plex:latest
    container_name: plex
    network_mode: host
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
      - VERSION=docker
    #   - PLEX_CLAIM=  # optional, get from https://account.plex.tv/claim
    volumes:
      - '/home/${USER}/plex/library:/config'
      - '/home/${USER}/data/shows:/tv'
      - '/home/${USER}/data/movies:/movies'
      - '/home/${USER}/transcode/temp>:/transcode'
    restart: unless-stopped

  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/radarr/data:/config'
      - '/home/${USER}/media/movies:/movies' # optional
      - '/home/${USER}/media/downloads:/downloads' # optional
    ports:
      - 7878:7878
    restart: unless-stopped

  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/sonarr/data:/config'
      - '/home/${USER}/media/shows:/tv' # optional
      - '/home/${USER}/media/downloads:/downloads' # optional
    ports:
      - 8989:8989
    restart: unless-stopped

  prowlarr:
    image: lscr.io/linuxserver/prowlarr:latest
    container_name: prowlarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/prowlarr/data:/config'
    ports:
      - 9696:9696
    restart: unless-stopped

  bazarr:
    image: lscr.io/linuxserver/bazarr:latest
    container_name: bazarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
    volumes:
      - '/home/${USER}/bazarr/config:/config'
      - '/home/${USER}/media/movies:/movies' # optional
      - '/home/${USER}/media/shows:/tv' # optional
    ports:
      - 6767:6767
    restart: unless-stopped

  overseerr:
    image: sctx/overseerr:latest
    container_name: overseerr
    environment:
      - LOG_LEVEL=debug
      - TZ=Europe/Lisbon
      - PORT=5055 #optional
    ports:
      - 5055:5055
    volumes:
      - '/home/${USER}/overseerr/config:/config'
    restart: unless-stopped
```