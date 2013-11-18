#!/usr/bin/env python

import os
import csv
import commands
import cgi, cgitb

from seasonality import BuildSightings

cgitb.enable()
print "Content-Type: application/octet-stream\r\nContent-Disposition: attachment; filename=seasonality.csv\r\n"
form = cgi.FieldStorage()
filedata = form['csvfile']

if filedata.file:
    c = csv.reader(filedata.file)
    namefield = int(form['namefield'].value)-1
    datefield = int(form['datefield'].value)-1
    startingmonth = int(form['startingmonth'].value)
    endingmonth = int(form['endingmonth'].value)
    segments = int(form['segments'].value)
    try:
        lines = BuildSightings(c, namefield, datefield, startingmonth, endingmonth, segments)
        print lines
    except:
        print "Sorry, either the file was not read or the wrong fields were given."