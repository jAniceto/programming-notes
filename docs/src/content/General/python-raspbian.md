Title: Installing Python 3.7 on Raspbian
Date: 2018-08-27 21:14
Authors: José Aniceto


As of January 2018, Raspbian does not yet include the latest Python release, Python 3.6. This means we will have to build it ourselves, and here is how to do it. There is also an ansible role attached that automates it all for you.

1) Install the required build-tools (some might already be installed on your system).

```
$ sudo apt-get update
$ sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
```

If one of the packages cannot be found, try a newer version number (e.g. `libdb5.4-dev` instead of `libdb5.3-dev`).

2) Download and install Python 3.6. When downloading the source code, select the most recent release of Python 3.6, available on the [official site](https://www.python.org/downloads/source/). Adjust the file names accordingly.

```
$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
$ tar xf Python-3.7.0.tar.xz
$ cd Python-3.7.0
$ ./configure
$ make
$ sudo make altinstall
```

3) Optionally: Delete the source code and uninstall the previously installed packages. When uninstalling the packages, make sure you only remove those that were not previously installed on your system. Also, remember to adjust version numbers if necesarry.

```
$ sudo rm -r Python-3.7.0
$ rm Python-3.7.0.tar.xz
$ sudo apt-get --purge remove build-essential tk-dev
$ sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev
$ sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
$ sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
$ sudo apt-get autoremove
$ sudo apt-get clean
```

### References
* https://liudr.wordpress.com/2016/02/04/install-python-on-raspberry-pi-or-debian/
* https://gist.github.com/BMeu/af107b1f3d7cf1a2507c9c6429367a3b
