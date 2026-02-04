import sys
import csv



mcccpoints = {
    "Acton": "820, 840, 776, 823",
    "Arlington": "1270, 690",
    "Ashby": "200, 1200, 152, 1266",
    "Ashland": "760, 350, 727, 330",
    "Ayer": "630, 1005, 571, 998",
    "Bedford": "1065, 885, 1033, 839, 1037, 831, 1052, 845",
    "Belmont": "1250, 625",
    "Billerica": "1105, 1015, 1044, 988, 1044, 979",
    "Boxborough": "695, 860, 629, 800",
    "Burlington": "1230, 830",
    "Cambridge": "1315, 615",
    "Carlisle": "960, 940",
    "Chelmsford": "1000, 1065, 917, 1111 ",
    "Concord": "940, 830",
    "Dracut": "960, 1240, 990, 1255",
    "Dunstable": "735, 1235, 646, 1272",
    "Everett": "1430, 660",
    "Framingham": "890, 460",
    "Groton": "665, 1110",
    "Holliston": "830, 235",
    "Hopkinton": "690, 260",
    "Hudson": "700, 615",
    "Lexington": "1190, 710",
    "Lincoln": "1065, 730",
    "Littleton": "690, 970",
    "Lowell": "990, 1190, 956, 1178",
    "Malden": "1405, 715",
    "Marlborough": "700, 555, 666, 526, 630, 520, 610, 521, 610, 515, 524, 516",
    "Maynard": "790, 700",
    "Medford": "1370, 710",
    "Melrose": "1425, 775",
    "Natick": "975, 400",
    "Newton": "1185, 520, 1205, 444",
    "North Reading":"1395, 1005",
    "Pepperell": "515, 1275, 484, 1248",
    "Reading": "1355, 955, 1342, 893",
    "Sherborn": "910, 290, 910, 240, 893, 266",
    "Shirley": "490, 1050",
    "Somerville": "1390, 620",
    "Stoneham": "1390, 820",
    "Stow": "705, 730",
    "Sudbury": "865, 650",
    "Tewksbury": "1120, 1150",
    "Townsend": "410, 1145",
    "Tyngsboro": "835, 1270, 830, 1207",
    "Wakefield": "1400, 870",
    "Waltham": "1135, 600",
    "Watertown": "1210, 580",
    "Wayland": "965, 610",
    "Westford": "790, 1095",
    "Weston": "1060, 560",
    "Wilmington": "1280, 960",
    "Winchester": "1310, 730",
    "Woburn": "1275, 860"
}

masspoints = {
    "Berkshire": "95, 370",
    "Franklin": "200, 400",
    "Hampshire": "210, 330",
    "Hampden": "200, 250",
    "Worcester": "350, 350",
    "Middlesex": "475, 375",
    "Norfolk": "490, 285, 513, 324, 580, 300",
    "Suffolk": "530, 315, 513, 333, 542, 348",
    "Essex": "550, 450",
    "Plymouth": "575, 220",
    "Bristol": "500, 200",
    "Barnstable": "650, 145, 639, 174",
    "Dukes": "625, 65",
    "Nantucket": "740, 33",
}

uspoints = {
    "Alaska": "145, 180",
        "Washington": "190, 790",
        "Oregon": "100, 700",
        "California": "80, 580",
        "Nevada": "185, 525",
        "Idaho": "220, 640",
        "Utah": "280, 535",
        "Arizona": "250, 350",
        "Montana": "400, 700",
        "Wyoming": "400, 600",
        "Colorado": "400, 500",
        "New Mexico": "400, 400",
        "North Dakota": "550, 750",
        "South Dakota": "550, 650",
        "Nebraksa": "550, 550",
        "Kansas": "550, 450",
        "Oklahoma": "600, 350",
        "Texas": "550, 250",
        "Minnesota": "700, 650",
        "Iowa": "700, 550",
        "Missouri": "700, 450",
        "Arkansas": "750, 350",
        "Louisiana": "750, 250",
        "Wisconsin": "800, 650",
        "Illinois": "800, 550",
        "Michigan": "830, 700, 900, 650",
        "Indiana": "880, 525",
        "Kentucky": "900, 450",
        "Tennessee": "850, 400",
        "Mississippi": "800, 300",
        "Alabama": "900, 300",
        "Ohio": "950, 550",
        "West Virginia": "1000, 500, 1067, 526",
        "Florida": "1050, 150",
        "Georgia": "950, 300",
        "South Carolina": "1025, 350",
        "North Carolina": "1050, 400",
        "Virginia": "1050, 500",
        "Maryland": "1100, 530, 1037, 526",
        "Delaware": "1128, 517",
        "Pennsylvania": "1050, 550",
        "New Jersey": "1140, 560",
        "New York": "1100, 700",
        "Connecticut": "1175, 615",
        "Rhode Island": "1192, 623",
        "Massachusetts": "1170, 645",
        "Vermont": "1150, 700",
        "New Hampshire": "1175, 685",
        "Maine": "1200, 750",
        "Hawaii": "300, 188, 352, 163, 416, 138, 447, 910 "     
}


def setup_types(t):
    global locfield
    global outputfolder
    global points
    global labelcoords
    
    if t=="mccc":
        points = mcccpoints
        outputfolder = "mccc"
        locfield = 24
        labelcoords = "400, 1400, 500, 36"
    elif t=="mass":
        points = masspoints
        outputfolder = "mass"
        locfield = 23
        labelcoords = "100, 100, 100, 36"
    elif t=="us":
        points = uspoints
        outputfolder = "states"
        labelcoords = "400, 1400, 500, 36"
        locfield = 22
    else:
        raise Exception("bad map type")
        
def StripSubspecies(name):
    if "(" in name:
        return name[:name.find("(")-1]
    return name

class Sighting:
    def __init__(self, fields):
        self.name = StripSubspecies(fields[0])
        self.loc = fields[locfield]
            
    def __str__(self):
        return "%s %s" % (self.name, self.loc)

    def __repr__(self):
        return str(self)
        
if __name__=="__main__":
    if len(sys.argv)!=3:
        print """%s inputfile type""" % sys.argv[0]
        sys.exit(1)
    f = file(sys.argv[1])
    csv = csv.reader(f)

    t = sys.argv[2]
    setup_types(t)
    locs = points.keys()
    
    print "var birds = ["
    sightings = []
    header = next(csv)
    scsv = sorted(csv, key=lambda x: float(x[3]))

    for sighting in scsv:
        sightings.append(Sighting(sighting))

    f.close()
    
    birdlist = [""]
    birds = {}
    
    for s in sightings:
        if birdlist[-1] != s.name:
            birdlist.append(s.name)
            birds[s.name] = set()
        birds[s.name].add(s.loc)

    
    del birdlist[0]
    
    if sys.argv[2]=="1": print "Bird,%s" % ",".join(locs)
    for b in birdlist:
        llist = ""
        for l in locs:
            if l in birds[b]:
                llist = llist + "," + points[l]
                
        print "[\"%s\",[%s]]," % (b, llist[1:])
    print "[\"fake\",[1,2]]"
    print "];"
   
print "function main(image, doc, layer) {"
print "    for(var b in birds) {"
print "            var n = birds[b][0];"
print "            var ps = birds[b][1];"
print "            if(n!=\"fake\") {"
print "                var d = [doc duplicate];"
print "                var shapeLayer = [[d baseGroup] addShapeLayer];"
print "                var textBox = [shapeLayer addTextWithBounds:NSMakeRect(" + labelcoords + ")];"
print "                textBox.setString_(n);"
print "                for(var i = 0;i<ps.length; i+=2) {"
print "                    [[d currentLayer] floodFillAtPoint:NSMakePoint(ps[i], ps[i+1])];        "
print "                }"
print "             d.webExportWithOptions({'uti': 'public.png', 'file': \"/Volumes/Macintosh HD/Users/jason/Documents/nature/maps/" + outputfolder + "/\" + n + \".png\"});"
print "             d.close();"
print "         }"
print "     }"
print "}"
print
