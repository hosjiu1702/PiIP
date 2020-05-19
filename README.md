# PiIP
Find your headless Raspberry Pi IP address (for lazy people)

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


Voila !! (Your IP address will appear in a magic manner :) )
