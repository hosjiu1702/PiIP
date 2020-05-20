# PiIP
Find your headless Raspberry Pi IP address (_for lazy people_). You just need provide _username_ and _password_

It uses [paramiko](http://www.paramiko.org/) and [netdiscover](http://manpages.ubuntu.com/manpages/bionic/man8/netdiscover.8.html) command behind the scene.

## Prerequisite
__Python 3.6+__

## Dependencies

- Install [netdiscover](http://manpages.ubuntu.com/manpages/bionic/man8/netdiscover.8.html) if you do not have it on your system.

`sudo apt install netdiscover`
- Install [paramiko](http://www.paramiko.org/) in your favorite virtual enviroment and then install it with **pip** or your favorite package manager.
```
1. pip install -r requirements.txt
2. python ssh_script.py 
```

## Usage
`python ssh_script --username {your unix account to log in} --password {Your password}`

Voila !! (Your IP address will appear in a magic manner :) )

## Acknowledgement
Paramiko's Authors

Netdiscover's Authros

for creating very usefull tools

Thanks to [linhdb-2149](https://github.com/linhdb-2149) for first testing and using my tool :)

Thanks to [com0t](https://github.com/com0t) for his support. This mini project will not be true without his help.
