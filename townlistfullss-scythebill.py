import sys
import csv

cities = ["Acton",
"Arlington",
"Ashby",
"Ashland",
"Ayer",
"Bedford",
"Belmont",
"Billerica",
"Boxborough",
"Burlington",
"Cambridge",
"Carlisle",
"Chelmsford",
"Concord",
"Dracut",
"Dunstable",
"Everett",
"Framingham",
"Groton",
"Holliston",
"Hopkinton",
"Hudson",
"Lexington",
"Lincoln",
"Littleton",
"Lowell",
"Malden",
"Marlborough",
"Maynard",
"Medford",
"Melrose",
"Natick",
"Newton",
"North Reading",
"Pepperell",
"Reading",
"Sherborn",
"Shirley",
"Somerville",
"Stoneham",
"Stow",
"Sudbury",
"Tewksbury",
"Townsend",
"Tyngsboro",
"Wakefield",
"Waltham",
"Watertown",
"Wayland",
"Westford",
"Weston",
"Wilmington",
"Winchester",
"Woburn" ]

def StripSubspecies(name):
    if "(" in name:
        return name[:name.find("(")-1]
    return name

class Sighting:
    def __init__(self, fields):
        self.name = StripSubspecies(fields[0])
        self.city = fields[24]
            
    def __str__(self):
        return "%s %s" % (self.name, self.city)

    def __repr__(self):
        return str(self)
        
if __name__=="__main__":
    if len(sys.argv)!=3:
        print """%s inputfile outputheader""" % sys.argv[0]
        sys.exit(1)
    f = file(sys.argv[1])
    csv = csv.reader(f)
    header = next(csv)
    scsv = sorted(csv, key=lambda x: float(x[3]))
    sightings = []
    for sighting in scsv:
        if csv.line_num==1:
            continue
        sightings.append(Sighting(sighting))

    f.close()
    
    birdlist = [""]
    birds = {}
    
    for s in sightings:
        if birdlist[-1] != s.name:
            birdlist.append(s.name)
            birds[s.name] = set()
        birds[s.name].add(s.city)
    
    del birdlist[0]
    
    if sys.argv[2]=="1": print "Bird,%s" % ",".join(cities)
    for b in birdlist:
        line = b
        for c in cities:
            if c in birds[b]:
                line = "%s,1" % line
            else:
                line = "%s,0" % line
        print line

