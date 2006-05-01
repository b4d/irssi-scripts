#!/usr/bin/env python

author = 'b4d, baccic@gmail.com'
version = '0.1c, Noveber 18, 2008'
#version = '0.1b, May 1, 2006'

#
#TODO:
#       -more linux distro versions, maybe with * for independance

import commands
import string
import os
import platform

# machineinfo
def compinfo():
    uname = platform.uname()

    # user@host
    u = commands.getoutput('whoami')
    h = uname[1]
    uh = u+'@'+h

    # Proc
    cpuinfo = uname[5]

    # uptime
    up = commands.getoutput("uptime")
    splitit = string.split(up)
    if splitit[3] == 'days,' or splitit[3] == 'day,':
        uptime = splitit[2]+' '+splitit[3]+' '+splitit[4][0:-1]+' hours'
    elif splitit[3] == 'min,':
        uptime = splitit[2]+'  minutes'
    else:
        uptime = splitit[2][0:-1]+' hours'

    # Distro
    distro = platform.dist()[0]
    if distro =='':
        distro = file('/etc/issue', 'r').readlines()[1][:10] #only in arch :(

    # kernel ---shorter
    ver = uname[2]

    #memory info
    memtotal = string.split(commands.getoutput('cat /proc/meminfo | grep "MemTotal"'), ':')
    memtotal1 = memtotal[1]
    memtotal1 = string.lstrip(memtotal1)
    memtotal1 = eval(memtotal1[:-3]) / 1024

    #client info
    client = commands.getoutput("irssi -v")
    
    #print output
    print h+" || OS: "+ver+"; "+distro+" || CPU: "+cpuinfo+" || Memory:", memtotal1, "Mb || Up: "+uptime+" || Client: "+client

compinfo()
