# Raspberry PI setup instructions

This document show you how to set up a Raspberry Pi to run the TeoG PV service.
This includes installing the operating system, setting up networking (VPN connection. OPTIONAL) and installing the TeoG PV service.

## Hardware requirements

- Raspberry Pi 4 (4GB or 8GB RAM recommended)
- microSD card (16GB or larger recommended)
- Power supply for the Raspberry Pi
- Ethernet cable (to connect to the inverter)
- SIM module for Raspberry Pi https://de.aliexpress.com/item/1005007941611700.html?spm=a2g0o.order_list.order_list_main.5.42f05c5fkFyF7u&gatewayAdapt=glo2deu
- SIM card with data plan

## Initial setup manually

Enable ssh access:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Add an ssh-key and disable password access:

```bash
# On your local machine create an SSH key
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ssh-copy-id -i ~/.ssh/your_key.pub user@IP_ADDRESS
# Disable password login
sudo nano /etc/ssh/sshd_config
PasswordAuthentication no
sudo systemctl restart ssh
```



