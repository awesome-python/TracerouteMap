#########################################
#										#
#			  TracerouteMap			    #
#										#
#		 Created by Joshua Moore		#
#										#
#										#
#########################################

import os, sys
import simplekml
import re
from pathlib import Path

def traceroute(ipToRoute):
	print("Running Traceroute to: ", ipToRoute)
	command = "tracert " + ipToRoute
	completedRoute = os.popen(command).read()
	parseResult(completedRoute)

def parseResult(info):
	print("Parsing information from Traceroute...")
	lines=info.splitlines()
	addresses = []
	for line in lines:
		try:
			if(line[2].isdigit()):
				char1 = '['
				char2 = ']'
				address = (line[line.find(char1)+1 : line.find(char2)])
				if(not address):
					print()
				else:
					addresses.append(address)
		except IndexError:
			print()
	getCurl(addresses)

def getCurl(addresses):
	print("Getting location information from  ipinfo.io ...")
	lons = []
	lats = []
	names = []
	for address in addresses:
		command = "curl ipinfo.io/" + address
		info = os.popen(command).read()
		lines = info.splitlines()
		for line in lines:
			if "loc" in line:
				char0 = '"'
				tmp1 = line.split(":")
				tmp2 = re.findall('"([^"]*)"', tmp1[1])
				tmp3 = tmp2[0].split(",")
				lats.append(tmp3[0])
				lons.append(tmp3[1])
				names.append(address)
	createKML(names,lons,lats)

def createKML(names,lons,lats):
	print("Creating KML file...")

	kml = simplekml.Kml(name="TracerouteMap Map", open=1)
	tour = kml.newgxtour(name="Packet Route")
	playlist = tour.newgxplaylist()
	
	for i in range(0,len(names)):
		pnt = kml.newpoint(name=names[i], coords=[(lons[i],lats[i])])
		pnt.style.iconstyle.scale = 3
		pnt.style.iconstyle.icon.href = 'https://cdn2.iconfinder.com/data/icons/social-media-8/512/pointer.png'
		flyto = playlist.newgxflyto(gxduration=6)
		flyto.camera.longitude = lons[i]
		flyto.camera.latitude = lats[i]
		wait = playlist.newgxwait(gxduration=3)
	for i2 in range(0,len(lons)):
		try:
			name = names[i2] + " to " + names[i2+1]
			ls = kml.newlinestring(name=name)
			ls.coords = [(lons[i2],lats[i2]), (lons[i2+1],lats[i2+1])]
			ls.tessellate = 1
			ls.altitudemode = simplekml.AltitudeMode.clamptoground
			ls.style.linestyle.width = 8
			ls.style.linestyle.color = simplekml.Color.blue
		except IndexError:
			print()
	for x in range(0,999999):
		pathName = "C:/trace_maps/trace_map_"+str(x)+".kml"
		myFile = Path(pathName)
		if not myFile.is_file():
			kml.save(pathName)
			openGE(pathName)
			break

def openGE(filename):
	print("Opening Google Earth Pro...")
	os.system("\"C:/Program Files (x86)/Google/Google Earth Pro/client/googleearth.exe\" "+filename)
	done()

def done():
	print("")
	print(" Thanks for using TracerouteMap!")
	print(" Created by Joshua Moore")
	print(" github.com/supamonkey2000/TracerouteMap/")


newpath = "C:/trace_maps/"
if not os.path.exists(newpath):
    os.makedirs(newpath)

if(len(sys.argv)==1):
	print("Error: Incorrect command: must have IP address argument!")
	print("Example:")
	print("> python run.py 8.8.8.8")
	print("> python run.py google.com")
else:
	traceroute(sys.argv[1])