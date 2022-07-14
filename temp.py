"""
    temp file for testing out things
"""


import glob

txtfiles = []
for file in glob.glob("pictures/*.png"):
    txtfiles.append(file)


#print(txtfiles)

place_png = []
for i in txtfiles:
    t = i.split( "\\")
    place_png.append(t[1])

place = []
for k in place_png:
    p = k.split(".")
    place.append(p[0])

#print(place)
test = place[0]
vergleich = place[1]
#print(test.split("_"))
#print(vergleich.split("_")[0])

d = [{"place": "dukatia_unten", "section": "dukatia"},
    {"place": "dukatia_oben", "section": "dukatia"},
    {"place": "roselia_unten", "section": "roselia-mall"}]

for i in d:

    if("roselia" in i.values()):
        print(i)
