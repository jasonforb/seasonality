#!/usr/bin/env python

import os
import csv
import commands
import cgi, cgitb

from seasonality import BuildSightings

cgitb.enable()
print "Content-Type: text/csv\r\n\r\n"
form = cgi.FieldStorage()
filedata = form['csvfile']

if filedata.file:
    c = csv.reader(filedata.file)
    namefield = form['namefield']
    datefield = form['datefield']
    startingmonth = form['startingmonth']
    endingmonth = form['endingmonth']
    segments = form['segments']
    lines = BuildSightings(c, namefield, datefield, startingmonth, endingmonth, segments)
    print lines