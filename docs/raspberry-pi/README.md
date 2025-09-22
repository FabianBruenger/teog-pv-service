# Raspberry PI setup instructions

This document show you how to set up a Raspberry Pi to run the TeoG PV service.
This includes installing the operating system, setting up networking (VPN connection. OPTIONAL) and installing the TeoG PV service.

## Hardware requirements

- Raspberry Pi 3 (B/B+)
- microSD card (32GB)
- Power supply for the Raspberry Pi
- Ethernet cable (to connect to the inverter)
- [SIM module](https://de.aliexpress.com/item/1005007941611700.html?spm=a2g0o.order_list.order_list_main.5.42f05c5fkFyF7u&gatewayAdapt=glo2deu) for Raspberry Pi 
- NB-IoT or CAT-M enabled SIM card by [Onomondo](https://onomondo.com/pricing/?location=&search=Ghana)
- 

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

Initialize IO and install software

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install pip
sudo pip install RPi.GPIO # or sudo apt-get install python3-rpi.gpio
sudo apt-get install python-serial # sudo apt-get install python3-serial
wget -P ~/Documents/ https://files.waveshare.com/upload/4/4a/SIM7080G_Cat_M_NB_IoT_HAT_Code.tar.gz
cd ~/Documents
tar -xzf SIM7080G_Cat_M_NB_IoT_HAT_Code.tar.gz
sh ~/Documents/SIM7080G_Cat_M_NB_IoT_HAT_Code/RaspberryPi/pi_gpio_init.sh
```

## Run

To run the AT code and follow the [official doc](https://www.waveshare.com/wiki/SIM7080G_Cat-M/NB-IoT_HAT#HTTP.28S.29_Test)

```bash
gpioset gpiochip0 4=0
python3 SIM7080G_Cat_M_NB_IoT_HAT_Code/RaspberryPi/python/at/getting_infos.py
```






