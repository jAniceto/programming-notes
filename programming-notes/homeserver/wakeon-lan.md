# Wake-on-LAN in Ubuntu

<sub><sup>Reference: [How to Enable Wake-on-LAN in Ubuntu 22.04](https://www.golinuxcloud.com/wake-on-lan-ubuntu/)</sub></sup>

## Enable Wake-On-Lan feature

```bash
ip a
```

Register the mac address.

To view and change the Wake-On-Lan settings, the "ethtool" package must be installed:

```bash
sudo apt install ethtool -y
```

Find out if the network card supports wake-on-LAN:

```bash
sudo ethtool enp2s0
```

The expression `Wake-on:d` indicates that the wake-on-lan feature of the network card is supported but deactivated.

Run the following commands to enable wake-on-lan on your network card:

```bash
sudo ethtool -s enp2s0 wol g
```

Some motherboard manufacturers require you to change the settings in the BIOS to enable this feature. If there is no change when you check after entering the command, it is recommended to look at the BIOS settings.

## Auto Wake-On-Lan activation at startup

If the Wake-on-Lan settings are deactivated when the server is restarted; you should solve this problem with systemd. Create systemd service:

```bash
sudo --preserve-env systemctl edit --force --full wol-enable.service
```

```
[Unit]
Description=Enable Wake-up on LAN

[Service]
Type=oneshot
ExecStart=/sbin/ethtool -s enp2s0   wol g

[Install]
WantedBy=basic.target
```

Replace the `enp2s0` value with your own network interface value. Then reload and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable wol-enable.service
```

## Remote Ubuntu server wake up

 Now, the steps to be done on the server that will do the wake-up task.

```bash
sudo apt  install wakeonlan -y
```

Wake up remote server using:

```bash
sudo wakeonlan 30:5a:3a:0d:ac:0d
```

where `30:5a:3a:0d:ac:0d` is the remote server MAC address
