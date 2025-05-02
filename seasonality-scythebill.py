#!/usr/bin/env python

import sys
import csv
from collections import OrderedDict


def getsegment(day, segments):
    # does not work for 8, 9, 11, 12, 13 (and anything greater than 15)
    divisor = 32 - (31 % segments) 
    s = day*segments / divisor
    if s>=segments: s=segments - 1
    return s
    
def StripSubspecies(name):
    if "(" in name:
        return name[:name.find("(")-1]
    return name
    
def BuildSightings(sightings, namefield, datefield, startmonth, endmonth, segments):
    seasonality = OrderedDict()
    lines = ""
    for s in sightings:
        name = StripSubspecies(s[namefield])
        year, month, day = map(int, s[datefield].split("-"))
        #month, day, year = map(int, s[datefield].split("/"))
        if startmonth <= month and endmonth >= month: # skip any sighting outside the given range of months
            segment = getsegment(day, segments)
            if name not in seasonality: # set up empty sets for each section first (could be wasteful but 36 per name can't add up to that much)
                seasonality[name] = {}
                for m in range(startmonth, endmonth+1):
                    seasonality[name][m] = {}
                    for n in range(segments):
                        seasonality[name][m][n] = set()
        
            seasonality[name][month][segment].add(year)
    for s in seasonality:
        line = "" + s
        for m in range(startmonth, endmonth+1):
            for n in range(segments):
                line += "," + str(len(seasonality[s][m][n]))
        lines += line + "\n"
    return lines
        
    
if __name__=="__main__":
    csv = csv.reader(file(sys.argv[1]))
    header = next(csv)
    sc = sorted(csv, key=lambda x: float(x[3]))
    print BuildSightings(sc, int(sys.argv[2])-1, int(sys.argv[3])-1, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
