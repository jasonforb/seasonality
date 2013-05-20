#!/usr/bin/python
import csv
import sys
from collections import OrderedDict

START_MONTH = 4
END_MONTH = 12

class Sighting:
    def __init__(self, fields):
        self.name, temp1, temp2, temp3, sdate, temp4, temp5, temp6, temp7, temp8, temp9 = fields
        self.month, self.day, self.year = sdate.split("/")
        
    def cell(self):
        return (int(self.month)-START_MONTH)*6+self.monthsegment()
        
    def __str__(self):
        return "%s (%s-%s-%s) %s" % (self.name, self.day, self.month, self.year, self.cell())
        
    def monthsegment(self):
        self.day = int(self.day)
        if self.day > 29:
            return 5
        return self.day / 5
    
def NumberOfCells():
    return (END_MONTH - START_MONTH + 1) * 6
    
def go():
    sightings = OrderedDict()
    c = csv.reader(file(sys.argv[1]))
    for s in map(Sighting, c):
        if s.name not in sightings:
            sightings[s.name] = {}
        if s.cell() not in sightings[s.name]:
            sightings[s.name][s.cell()] = [s.year]
        else:
            sightings[s.name][s.cell()].append(s.year)
    for s in sightings.keys():
        results = s + ","
        for cell in xrange(0, NumberOfCells()):
            if cell in sightings[s]:
                results += str(len(set(sightings[s][cell]))) + ","
            else:
                results += "0,"
        print results
if __name__=="__main__":
    go()