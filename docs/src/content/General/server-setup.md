Title: Initial Server Setup with Ubuntu 18.04
Date: 2018-06-06 23:19
Authors: José Aniceto
Modified: 2018-06-13 22:30

When first creating a new Ubuntu 18.04 server, there are a few configuration steps that you should take early on as part of the basic setup.

## 1) Creating a New User

Once you are logged in as root, we're prepared to add the new user (synergix) account that we will use to log in from now on.

`adduser synergix`

Enter a strong password and, optionally, fill in any of the additional information if you would like. This is not required and you can just hit ENTER in any field you wish to skip.

## 2) Granting Administrative Privileges

Set up what is known as "superuser" or root privileges for our normal account. This will allow our normal user to run commands with administrative privileges by putting the word `sudo` before each command. As **root**, run this command to add your new user to the sudo group:

`usermod -aG sudo synergix`

## 3) Setting Up a Basic Firewall

Ubuntu 18.04 servers can use the UFW firewall to make sure only connections to certain services are allowed. We can set up a basic firewall very easily using this application.

Different applications can register their profiles with UFW upon installation. These profiles allow UFW to manage these applications by name. OpenSSH, the service allowing us to connect to our server now, has a profile registered with UFW. You can see this by typing:

`ufw app list`

Afterwards, we can enable the firewall by typing:

`ufw enable`

Type "y" and press ENTER to proceed. You can see that SSH connections are still allowed by typing:

`ufw status`

As the firewall is currently blocking all connections except for SSH, if you install and configure additional services, you will need to adjust the firewall settings to allow acceptable traffic in. More info here: https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands

## 4) Enabling External Access for Your Regular User

Now that we have a regular user for daily use, we need to make sure we can SSH into the account directly. The process for configuring SSH access for your new user depends on whether your server's root account uses a password or SSH keys for authentication.

#### If the Root Account Uses Password Authentication

If you logged in to your root account using a password, then password authentication is enabled for SSH. You can SSH to your new user account by opening up a new terminal session and using SSH with your new username:

`ssh synergix@your_server_ip`

After entering your regular user's password, you will be logged in. You will be prompted for your regular user password when using sudo for the first time each session (and periodically afterwards).

To enhance your server's security, it is recommended to set up SSH keys instead of using password authentication: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804

#### If the Root Account Uses SSH Key Authentication

If you logged in to your root account using SSH keys, then password authentication is disabled for SSH. You will need to add a copy of your local public key to the new user's `~/.ssh/authorized_keys` file to log in successfully.

Since your public key is already in the root account's `~/.ssh/authorized_keys` file on the server, we can copy that file and directory structure to our new user account in our existing session.

The simplest way to copy the files with the correct ownership and permissions is with the `rsync` command. This will copy the root user's .ssh directory, preserve the permissions, and modify the file owners, all in a single command:

`rsync --archive --chown=synergix:synergix ~/.ssh /home/synergix`

Now, open up a new terminal session and using SSH with your new username:

`ssh synergix@your_server_ip`

You should be logged in to the new user account without using a password. 

## 5) Other

Chose the timezone by running: `sudo dpkg-reconfigure tzdata`

## References:
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04
