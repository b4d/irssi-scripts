#!/usr/bin/env python
# -*- coding: utf-8 -*-

# itunes.py
# irssi now playing script for iTunes
# v 0.1, 19.08.2013
# v 0.2, 22.11.2018 
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


def ratingStars(rating):
    if rating == '20':
        return "[★☆☆☆☆]"
    elif rating == '40':
        return "[★★☆☆☆]"
    elif rating == '60':
        return "[★★★☆☆]"
    elif rating == '80':
        return "[★★★★☆]"
    elif rating == '100':
        return "[★★★★★]"
    else:
        return " "

def mpcnp():
    result = commands.getoutput("osascript -e 'tell application \"iTunes.app\" \n \
                set this_name to the name of current track \n \
                set this_artist to the artist of current track \n \
                set this_album to the album of current track \n \
                set this_rating to the rating of current track \n \
                set this_time to the duration of current track \n \
                set this_current_time to the player position \n \
        end tell \n \
        return this_artist & tab & this_name & tab & this_album & tab & this_time & tab & this_current_time & tab & this_rating \
            '")

    result = result.split("\t")


    if len(result) == 1:
        np = 'Is iTunes running?'
    else:
        artist = result[0].lstrip()
        track = result[1].lstrip()
        album = result[2].lstrip()
        rating = result[5]
        time = result[3].replace(',','.')
        current_time = result[4].replace(',','.')

        percent = (float(current_time)/float(time))*100

        #np = u"\u2669"+' '+artist+' - '+track+' ~ ('+album+') @ '+progressBar(percent)

        np = "♩ "+artist+' - '+track+' ~ ('+album+') @ '+progressBar(percent) +' '+ratingStars(rating)
        # notes in unicode 2669 quarter, 266A eighth, 266B beamed eighth, 266C beamed sixteenth
        # 1D11E G CLEF
        # 1F3B5 emoji note

        # ★
        # ☆
    print(np)




try:
    mpcnp()
except Exception as e:
    print("EXCEPTION: Is iTunes running?")
    print e

