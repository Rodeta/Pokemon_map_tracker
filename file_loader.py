import glob

txtfiles = []
for file in glob.glob("pictures/*.png"):
    txtfiles.append(file)


print(txtfiles)

place_png = []
for i in txtfiles:
    t = i.split( "\\")
    place_png.append(t[1])

place = []
for k in place_png:
    p = k.split(".")
    place.append(p[0])

print(place)