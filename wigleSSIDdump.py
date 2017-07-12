import sys
from pygle import network

lat1 = raw_input("Lat1: ")
lat2 = raw_input("Lat2: ")
long1 = raw_input("Long1: ")
long2 = raw_input("Long2: ")
outfilename = raw_input("Outfile name: ")

reply1 = network.search(lastupdt="20160101",latrange1=lat1,latrange2=lat2,longrange1=long1,longrange2=long2)
reply2 = network.search(lastupdt="20160101",latrange1=lat1,latrange2=lat2,longrange1=long1,longrange2=long2,first=101)
reply3 = network.search(lastupdt="20160101",latrange1=lat1,latrange2=lat2,longrange1=long1,longrange2=long2,first=201)
reply4 = network.search(lastupdt="20160101",latrange1=lat1,latrange2=lat2,longrange1=long1,longrange2=long2,first=301)
reply5 = network.search(lastupdt="20160101",latrange1=lat1,latrange2=lat2,longrange1=long1,longrange2=long2,first=401)

ssidlist = []

for line in reply1["results"]:
    ssidlist.append(line["ssid"])

for line in reply2["results"]:
    ssidlist.append(line["ssid"])

for line in reply3["results"]:
    ssidlist.append(line["ssid"])

for line in reply4["results"]:
    ssidlist.append(line["ssid"])

for line in reply5["results"]:
    ssidlist.append(line["ssid"])

ssidlist = set(ssidlist)

with open(outfilename,"w") as outfile:
    for x in ssidlist:
        outfile.write(str(x) + "\n")
