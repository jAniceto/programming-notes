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
