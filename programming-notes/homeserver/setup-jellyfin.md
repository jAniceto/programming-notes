# Set up Jellyfin

## Installing in Docker container

<sub><sup>Reference: [Jellyfin Container Installation](https://jellyfin.org/docs/general/installation/container)</sub></sup>

Create persistent storage for configuration and cache data. Create two directories on the host and use bind mounts:

```bash
mkdir /path/to/config
mkdir /path/to/cache
mkdir /path/to/media
```

so, more precisely:

```bash
cd ~
mkdir -p jellyfin/config
mkdir -p jellyfin/cache
mkdir media
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
      - type: bind
        source: '/home/${USER}/media'
        target: /media
    restart: 'unless-stopped'
```

Then while in the same folder as the `docker-compose.yml` run:

```bash
docker compose up -d
```

Jellyfin will be available at `http://hostname:8096`.


## Configuration

<sub><sup>Reference: [Jellyfin Libraries](https://jellyfin.org/docs/general/server/libraries/)</sub></sup>

After accessing `http://hostname:8096`, follow the setup wizard.

Add media libraries. If you don't see your media folders listed, you might have permission issues. In the directory containing the `media` folder, try:

```bash
sudo chown -R $USER:$USER media
sudo chmod -R 775 media
```