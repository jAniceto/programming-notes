# Mounting external drives

To list all drives run:

```
$ lsblk
```

## Mount and unmount external drives

One common need is to mount an external drive, be it an external hard drive, USB stick, or an external SSD.

Create a new mount point, and mount the drive there:

```
$ sudo mkdir /mnt/externaldrive
$ sudo mount /dev/sda1 /mnt/externaldrive
```

To unmount:

```
$ sudo umount /mnt/externaldrive
```


## Add a new internal drive

### 1) List all drives:

```
$ lsblk
```

This will output something like this:

```
nvme0n1                   259:0    0 953.9G  0 disk
nvme1n1                   259:1    0 931.5G  0 disk
├─nvme1n1p1               259:2    0     1G  0 part /boot/efi
├─nvme1n1p2               259:3    0     2G  0 part /boot
└─nvme1n1p3               259:4    0 928.5G  0 part
  └─ubuntu--vg-ubuntu--lv 252:0    0 928.5G  0 lvm  /
```

In the above we can see `nvme1n1` is partition and mounted at `/`. Another new drive has been added but is still unpartitioned and unmounted.

### 2) If the disk is raw/unpartitioned, we need to partition the new drive:

```
$ sudo fdisk /dev/nvme0n1
```

Inside fdisk:
 - `n` to create new partition
 - `p` to set as primary
 - Accept defaults for full disk
 - `w` to write changes

After this, you should see `/dev/nvme0n1p1`.

### 3) Format the partition for `ext4` (most common case):

```
$ sudo mkfs.ext4 /dev/nvme0n1p1
```

Take note of the UUID. We will need it later.

### 4) Create a mount point for the new drive:

```
$ sudo mkdir -p /mnt/newssd
```

### 5) Mount the drive (temporarily):

```
$ sudo mount /dev/nvme0n1p1 /mnt/newssd
```

You can verify with:

```
$ df -h
```

### 6) Get the UUID (required for permanent mount):

```
$ blkid /dev/nvme0n1p1
```

It will be something like `UUID="e3b1c9a4-8c5d-4b8d-a9b2-123456789abc"`.


### 7) Mount automatically at boot using `fstab`:

```
$ sudo nano /etc/fstab
```

Add this line and replace UUID and path:

```
UUID=e3b1c9a4-8c5d-4b8d-a9b2-123456789abc  /mnt/ssd2  ext4  defaults,nofail  0  2
```

To test `fstab`:

```
$ sudo umount /mnt/newssd
$ sudo mount -a
```

If no errors, it will mount correctly at boot.


### 8) Set permissions so your user can write to it:

```
$ sudo chown -R $USER:$USER /mnt/newssd
```
