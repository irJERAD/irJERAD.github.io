- - -
layout: post
Author: Jerad Acosta
title: "VPN Setup on Kali Pi"
date: "2017-04-05"
tags: [Linux, Kali, Raspberry Pi, IoT, Security, VPN]
category: Tutorial
- - -

## How To:

#Kali-Pi VPN Tutorial

### Enable Private Internet Access VPN service on a Raspberry Pi Running Kali v2.1.2

This is a quick method to render a fresh Kali image running on a Raspberry Pi able to work with the Private Internet Access VPN service.  
The [Offensive Security](https://www.offensive-security.com) [Kali ARM Images](https://www.offensive-security.com/kali-linux-arm-images/) do not support the [Private Internet Access](https://www.privateinternetaccess.com/) VPN service out of the box at the time of this piece (Kali ARM Version 2.1.2 + [Raspberry Pi 3](http://amzn.to/2o8mvpO))


Here I attempt the mend that problem (*spoiler* it works) and share any hopeful results with other fans of the service as well as the tech; _stubbornly existing, unwilling to **choose between forfeiting security or freedom**_
> ‘for they shall have none’
> ¿or is it 'deserve none’?
> either way Abraham Lincoln will be pissed at you...
>
>	...for messing up a Bengimin Franklin quote of course!


1. Install `openvpn` packages
```bash
$ apt-get install network-manager-openvpn
```

2. install private internet access’ openvpn client
```bash
$ wget https://www.privateinternetaccess.com/openvpn/openvpn.zip
```
3. move downloaded zip file to its own directory
```bash
$ mv openvpn.zip /etc/openvpn
```
4. change into newly created openvpn directory where the zip file was placed
```bash
cd /etc/openvpn
```

5. unzip the openvpn package in it’s directory
```bash
$ unzip openvpn.zip
```
6. You can now use the GUI to select a VPN connection Type: follow the prompt.


Open Network Manager -->
--> Select VPN connections, configure/add VPN...

click   **[ADD +]**   click the drop down menu, and set the type as OpenVPN.

click   **[Create]**

Make sure you are on "**VPN**" tab, not "**IPv4 settings**".

Connection name: (you can put whatever you want here)

For Gateway enter `us-east.privateinternetaccess.com` (no quotes or spaces)

Type: set the type as Password

put in your Private Internet Access username and password.

CA Certificate:  **CA.crt** is in the folder that you unzipped openvpn.zip in.
click **(none)** and direct it there, if you're following word for word it will be in:  
`/etc/openvpn`

click **[Advanced]** and check the box next to `use LZO data compression`

click **[OK]** **[Save]** **[Close]**

You're good to go!

now click network manager > vpn connections > your connection

it will notify you when you are connected.

(note: there are lots of great things to do after this, some are here: http://www.blackmoreops.com/2014/03/03/20-things-installing-kali-linux/ I have no affiliation with them, but it's a good read.)

if you choose saved for password, you may have to enter your password for keyring.