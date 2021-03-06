# PiIP
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![Python 3.7](https://img.shields.io/badge/python-v3.7-blue)
![license MIT](https://img.shields.io/badge/license-MIT-green)

Find your *headless* Raspberry Pi __IP address__ (_for lazy people_).

* You just need provide _username_ and _password_.

* It uses [paramiko](http://www.paramiko.org/) and [netdiscover](http://manpages.ubuntu.com/manpages/bionic/man8/netdiscover.8.html) command behind the scene.

## Prerequisite
Python 3.6 or later

## Dependencies

- Install [netdiscover](http://manpages.ubuntu.com/manpages/bionic/man8/netdiscover.8.html) if you do not have it on your system.

```
sudo apt install netdiscover
```
- Install [paramiko](http://www.paramiko.org/) in your favorite virtual enviroment and then install it with **pip** or your favorite package manager.
```
pip install -r requirements.txt
```

## Usage
```
python scan --username {your unix account to log in} --password {Your password}
```

Voila !! (Your IP address will appear in a magic manner :) )

## Acknowledgement
Paramiko's Authors | Netdiscover's Authros for creating very usefull tools

Thanks to [linhdb-2149](https://github.com/linhdb-2149) for first testing and using my tool :)

Thanks to [com0t](https://github.com/com0t) for his support. This mini project will not be true without his help.
