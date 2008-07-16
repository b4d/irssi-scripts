#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mpc.py
# irssi now playing script for mpd/mpc
# v 0.1, 16.07.2008
#

import commands
import string

def progressBar(percent):
    progBar = "[]"
    min = 0
    max = 10
    width = 20
    amount = 0
    percent = int(percent)

    allFull = width - 2
    numHashes = (percent / 100.0) * allFull
    numHashes = int(round(numHashes))
    progBar = "[" + '='*numHashes + ' '*(allFull-numHashes) + "]"
    percentPlace = (len(progBar) / 2) - len(str(percent)) 
    percentString = str(percent) + "%"
    progBar = progBar[0:percentPlace] + percentString + progBar[percentPlace+len(percentString):]
    return str(progBar)

def mpcnp():
    results = commands.getoutput("mpc").split("\n")
    line1 = results[1].split()
    line2 = results[2].split()
    
    track = results[0]
    time = line1[2].split('/')[1]
    current_time = line1[2].split('/')[0]
    percent = line1[3].rstrip(')').lstrip('(').rstrip('%')
    album = commands.getoutput("mpc --format %album%").split("\n")[0]
    if track == '':
        np = 'Are mpd and mpc running?'
    else:
        if album == '':
            np = 'mpd: '+track+' ~ (N/A) @ '+progressBar(percent)
        else:
            np = 'mpd: '+track+' ~ ('+album+') @ '+progressBar(percent)
    print(np)

try:
    mpcnp()
except:
    print("Are mpd and mpc running?")

