#!/usr/bin/env python

author = 'b4d, baccic@gmail.com'
version = '0.1, August 19, 2013'
#version = '0.1b, May 1, 2006'


import commands
import string
import os

# machineinfo
def compinfo():

    # user@host
    #iu = commands.getoutput('whoami')
    h = commands.getoutput('hostname').split('.')[0]
    #uh = u+'@'+h

    # Proc
    #model = commands.getoutput('system_profiler SPHardwareDataType | grep "Processor Name"').split(':')[1].lstrip()
    #clock = commands.getoutput('system_profiler SPHardwareDataType | grep "Processor Speed"').split(':')[1].lstrip().replace(" ", "")

    #cpuinfo = model+' '+clock
    cpuinfo = commands.getoutput('sysctl -n machdep.cpu.brand_string')

    # uptime
    #up = commands.getoutput("uptime")
    #splitit = string.split(up)
    #if splitit[3] == 'days,' or splitit[3] == 'day,':
    #    uptime = splitit[2]+' '+splitit[3]+' '+splitit[4][0:-1]+' hours'
    #elif splitit[3] == 'min,':
    #    uptime = splitit[2]+'  minutes'
    #else:
    #    uptime = splitit[2][0:-1]+' hours'
    uptime = commands.getoutput("echo `uptime` | awk '{ print $3 " " $4 }'")

    # Distro
    distro = "MacOSX"
    ver = commands.getoutput('sw_vers -productVersion')


    #memory info
    memory = commands.getoutput('system_profiler SPHardwareDataType | grep "Memory"').split(':')[1].lstrip().replace(" ", "")

    #storage info
    storage = commands.getoutput('system_profiler SPStorageDataType | grep "Capacity"').split(':')[1].lstrip().split('(')[0].rstrip().replace(" ", "")
    medium = commands.getoutput('system_profiler SPStorageDataType | grep "Medium"').split(':')[1].lstrip()


    #client info
    #client = commands.getoutput("irssi -v")
    
    #print output
    print h+" | "+distro+" "+ver+" | "+cpuinfo+" | "+memory+" | "+storage+" "+medium+" | Up: "+uptime

compinfo()
