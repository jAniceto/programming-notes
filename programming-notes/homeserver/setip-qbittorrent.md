# Set up qbittorrent

<sub><sup>Reference: [Docker Hub qbittorrent](https://hub.docker.com/r/linuxserver/qbittorrent)</sub></sup>

Set up directories.

```bash
cd ~
mkdir -p qbittorrent/appdata
mkdir downloads
```

Create a `docker-compose.yml` file with the following contents.

```bash
cd qbittorrent
nano docker-compose.yaml
```

```yaml
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:latest
    container_name: qbittorrent
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Lisbon
      - WEBUI_PORT=8080
      - TORRENTING_PORT=6881
    volumes:
      - '/home/${USER}/qbittorrent/appdata:/config'
      - '/home/${USER}/downloads:/downloads' #optional
    ports:
      - 8080:8080
      - 6881:6881
      - 6881:6881/udp
    restart: unless-stopped
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

The web UI is available at `http://homeserver:8080`.