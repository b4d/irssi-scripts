#!/usr/bin/python
# Filename: irclogcount.py
# Author: b4d
# Version: 0.1a, 01.04.2006
#
#Ubistvu dela sam je treba se nardit da ugotovi na kjerem kanalu si pa kjer datu m je da pravi file odpre

import os, commands, string, sys
# Until date nick 'nick' wrote: counter lines


nick = 'b4d'
channel = 'rilinux'
path = '/mnt/podatki/irclogs/'
date = commands.getoutput('date +%F')
path = path+channel+"-"+date+".txt"
f = file(path, 'r')
counter = 0
logfile = file(path, 'r').readlines()
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        splitted = string.split(line)
        if splitted[2] == nick+">":
            counter = counter + 1
        elif splitted[1] =="<+"+nick+">":
            counter = counter + 1
time = string.split(commands.getoutput('date'))

print "Until "+time[3]+", nick '"+nick+"', wrote:",counter,"lines."


