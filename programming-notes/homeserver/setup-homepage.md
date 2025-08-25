# Set up Homepage

<sub><sup>Reference: [Docker Installation](https://gethomepage.dev/installation/docker/)</sub></sup>

Set up directory for configuration file, for instance, in your `/home` directory:

```bash
cd ~
mkdir -p homepage/config
```

Create a `docker-compose.yml` file:

```bash
cd homepage
nano docker-compose.yml
```

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    ports:
      - 3000:3000
    volumes:
      - '/home/${USER}/homepage/config:/config' # Make sure your local config directory exists
      - /var/run/docker.sock:/var/run/docker.sock # (optional) For docker integrations
    environment:
      HOMEPAGE_ALLOWED_HOSTS: hostname:3000 # required, may need port. See gethomepage.dev/installation/#homepage_allowed_hosts
    restart: 'unless-stopped'
```

Start Docker container:

```bash
docker compose up -d
```

Going to `http://hostname:3000`, you should see your homepage.


## Configuration

In the `services.yml`:

```yaml
- Media:
    - Immich:
        href: http://homeserver:2283
        description: Photo and video management

    - Plex:
        href: http://homeserver:32400/web
        description: Media server

- Utilities:
    - Portainer:
        href: http://homeserver:9443
        description: Docker container management

    - qBittorrent:
        href: http://homeserver:8080
        description: Bittorrent client

- Servarr:
    - Radarr:
        href: http://homeserver:7878
        description: Movies

    - Sonarr:
        href: http://homeserver:8989
        description: TV shows

    - Prowlarr:
        href: http://homeserver:9696
        description: Indexer manager

    - Bazarr:
        href: http://homeserver:6767
        description: Subtitle manager

    - Overseerr:
        href: http://homeserver:5055
        description: Media requests manager
```
