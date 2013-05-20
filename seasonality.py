#!/usr/bin/env python

import sys
import csv
from collections import OrderedDict

class Sighting:
    def __init__(self, fields, namefield, datefield, startmonth, endmonth, segments):
        self.name = fields[namefield - 1]
        sdate = fields[datefield - 1]
        self.month, self.day, self.year = sdate.split("/")
        self.startmonth = startmonth
        self.endmonth = endmonth
        self.segments = segments
        
    def cell(self):
        return (int(self.month)-self.startmonth)*self.segments + self.monthsegment()
        
    def __str__(self):
        return "%s (%s-%s-%s) %s" % (self.name, self.day, self.month, self.year, self.cell())
        
    def monthsegment(self):
        self.day = int(self.day)
        segment = (self.day-1) / (self.segments - 1)
        if segment >= self.segments: # count partial end of months as part of last bit of previous segment
            segment -= 1
        return segment
        
def NumberOfCells(start, end, numberofsegments):
    return (end - start + 1) * numberofsegments
    
    
def BuildSightings(csvfile, namefield, datefield, startmonth, endmonth, numberofsegments):
    def MakeSighting(fields):
        return Sighting(fields, namefield, datefield, startmonth, endmonth, numberofsegments)
    sightings = OrderedDict()
    for s in map(MakeSighting, csvfile):
        if s.name not in sightings:
            sightings[s.name] = {}
        if s.cell() not in sightings[s.name]:
            sightings[s.name][s.cell()] = [s.year]
        else:
            sightings[s.name][s.cell()].append(s.year)
    results = ""
    for s in sightings.keys():
        line = s + ","
        for cell in xrange(0, NumberOfCells(startmonth, endmonth, numberofsegments)):
            if cell in sightings[s]:
                line += str(len(set(sightings[s][cell]))) + ","
            else:
                line += "0,"
        results += "%s\n" % (line.rstrip(","))
    return results