# Set up Immich

<sub><sup>Reference: [Immich Docs - Quick start](https://immich.app/docs/overview/quick-start)</sub></sup>

## Set up immich server

Create an directory for Immich:

```bash
mkdir ./immich-app
cd ./immich-app
```

Download `docker-compose.yml` and `example.env`:

```bash
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```

Rename `example.env` to `.env`. Populate the `.env` file with custom values:

```
# You can find documentation for all the supported env variables at https://immich.app/docs/install/environment-variables

# The location where your uploaded files are stored
UPLOAD_LOCATION=./library

# The location where your database files are stored. Network shares are not supported for the database
DB_DATA_LOCATION=./postgres

# To set a timezone, uncomment the next line and change Etc/UTC to a TZ identifier from this list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
TZ=Europe/Lisbon

# The Immich version to use. You can pin this to a specific version like "v1.71.0"
IMMICH_VERSION=release

# Connection secret for postgres. You should change it to a random password
# Please use only the characters `A-Za-z0-9`, without special characters or spaces
DB_PASSWORD=postgres

# The values below this line do not need to be changed
###################################################################################
DB_USERNAME=postgres
DB_DATABASE_NAME=immich
```

`UPLOAD_LOCATION` is your preferred location for storing backup assets. It should be a new directory on the server with enough free space.

From the directory which contains the docker-compose.yml and .env files, start Immich as a background service:

```bash
docker compose up -d
```


## Start the app

The first user to register will be the admin user. The admin user will be able to add other users to the application.

To register for the admin user, access the web application at `http://<machine-ip-address>:2283` and click on the **Getting Started** button.


## Add photos from Google Photos via Google Takeout

<sub><sup>Reference: [immich-go](https://github.com/simulot/immich-go)</sub></sup>

To add photos from Google Photos via Google Takeout you can use [immich-go](https://github.com/simulot/immich-go).

1. Visit the [releases page](https://github.com/simulot/immich-go/releases/latest).

2. Download the archive for your operating system and architecture:
   - Linux: `immich-go_Linux_x86_64.tar.gz`

3. Extract the archive:
   ```bash
   # For Linux
   tar -xzf immich-go_*_x86_64.tar.gz
   ```

4. (Optional) Move the binary to a directory in your PATH:
   ```bash
   # Linux
   sudo mv immich-go /usr/local/bin/
   ```
   
5. After installation, verify that `immich-go` is working correctly:
  ```bash
  immich-go --version
  ```

Examples usage:

```bash
## Upload photos from a local folder to your Immich server
immich-go upload from-folder --server=http://your-ip:2283 --api-key=your-api-key /path/to/your/photos

## Archive photos from your Immich server to a local folder
immich-go archive from-immich --from-server=http://your-ip:2283 --from-api-key=your-api-key --write-to-folder=/path/to/archive

## Upload a Google Photos takeout to your Immich server
immich-go upload from-google-photos --server=http://your-ip:2283 --api-key=your-api-key /path/to/your/takeout-*.zip
```
