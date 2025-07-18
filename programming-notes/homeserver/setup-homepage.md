# Set up Homepage

<sub><sup>Reference: [Docker Installation](https://gethomepage.dev/installation/docker/)</sub></sup>

Set up directory for configuration file, for instance

```bash
cd ~/server/configs/homepage
```

Create a `docker-compose.yml` file:

```bash
nano docker-compose.yml
```

```bash
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    ports:
      - 3000:3000
    volumes:
      - '/home/${USER}/server/configs/homepage:/config' # Make sure your local config directory exists
      - /var/run/docker.sock:/var/run/docker.sock # (optional) For docker integrations
    environment:
      HOMEPAGE_ALLOWED_HOSTS: hostname:XXXX # required, may need port. See gethomepage.dev/installation/#homepage_allowed_hosts
```

Start Docker container:

```bash
docker compose up -d
```

Going to `hostname:XXXX`, you should see your homepage.
