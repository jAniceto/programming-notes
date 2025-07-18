# Set up Docker and Docker Compose

## Installing Docker

<sub><sup>Reference: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)</sub></sup>

Set up Docker's `apt` repository.

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install the Docker packages.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify that the installation is successful by running the hello-world image:

```bash
sudo docker run hello-world
```

### Now some optional post-installation steps

<sub><sup>Reference: [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/)</sub></sup>

Create the `docker` group and add your user:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Log out and log back in so that your group membership is re-evaluated. 

```bash
exit
ssh username@hostname
```

## Installing Docker Compose

<sub><sup>Reference: [Overview of installing Docker Compose](https://docs.docker.com/compose/install/)</sub></sup>

Since we already have Docker Engine and Docker CLI installed, we can install the Docker Compose plugin from the command line, by using Docker's repository:

Update the package index, and install the latest version of Docker Compose:

```bash
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

To verify that Docker Compose is installed correctly we can run:

```bash
docker compose version
```

