import pandas as pd
import csv
import os
import sys

#If not done on the device running this code already, run import nltk then nltk.download() in python shell to download necesary libraries


def findTime(phrase):
    legnthfinder = open("trumpspeeches.csv")
    length = len(legnthfinder.readlines())
    csv.field_size_limit(sys.maxsize)
    rows = list()
    with open("trumpspeeches.csv", 'r') as csvfile:
        content = csvfile.read()
        x = findAll(content, phrase)
        print(x)
        #working with first instance for now, change x[0] to x[whatever] to go with other instances
        z = timeAround(content, x[0])
        wpm = z[0]
        mpw = 1/wpm
        timeBefore = z[1]
        timeAfter = z[2]
        string = content[z[3]:x[0]]
        words = string.split()
        wordCount = len(words)
        timeElapsed = mpw*wordCount
        finalTime = timeElapsed + timeBefore
        print(finalTime)
        return finalTime




    '''
    with open("trumpspeeches.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if phrase in row:
                print (row.index('test'))

    index = 0
'''

    #returns a list of locations of a substring
def findAll(string, substring):
    #actually bad because has a limit which doesn't work on large datafiles, transition to regular expressions
    substring_length = len(substring)
    def recurse(locations_found, start):
        location = string.find(substring, start)
        if location != -1:
            return recurse(locations_found + [location], location+substring_length)
        else:
            return locations_found
    return recurse([], 0)

def timeAround(content, index):
    # indexTimeAfter = content.find("(", x[0])
    y = list()
    z = list()
    i = 0
    while (i < index):
        i = content.find("(", i + 1)
        y.append(i)

    indexTimeAfter = y[-1]
    indexTimeBefore = y[-2]

    timeBefore = (int(content[indexTimeBefore + 4]) * 10 + int(content[indexTimeBefore + 5])) / 60 + (
            int(content[indexTimeBefore + 1]) * 10 + int(content[indexTimeBefore + 2]))

    timeAfter = (int(content[indexTimeAfter + 4]) * 10 + int(content[indexTimeAfter + 5])) / 60 + (
                int(content[indexTimeAfter + 1]) * 10 + int(content[indexTimeAfter + 2]))


    string = content[indexTimeBefore:indexTimeAfter]
    words = string.split()
    wordCount = len(words)
    wpm = wordCount/(timeAfter-timeBefore)
    z.append(wpm)
    z.append(timeBefore)
    z.append(timeAfter)
    z.append(indexTimeBefore)
    z.append(indexTimeAfter)
    return z



findTime("nursing")


