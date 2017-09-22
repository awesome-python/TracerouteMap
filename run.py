#Python
import os
import simplekml
import re
from pathlib import Path

def traceroute(ipToRoute):
	print("Running Traceroute to: ", ipToRoute)
	command = "tracert " + ipToRoute
	completedRoute = os.popen(command).read()
	#print(completedRoute)
	parseResult(completedRoute)

def parseResult(info):
	lines=info.splitlines()
	addresses = []
	for line in lines:
		#if line starts with a number, then split by [ and remove ].
		#then hopefully I have the IP for curl
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
	lons = []
	lats = []
	names = []
	for a in addresses:
		print(a)
	for address in addresses:
		command = "curl ipinfo.io/" + address
		info = os.popen(command).read()
		lines = info.splitlines()
		for line in lines:
			if "loc" in line:
				char0 = '"'
				tmp1 = line.split(":")
				tmp2 = re.findall('"([^"]*)"', tmp1[1])
				#tmp2 = (tmp1[1][tmp1[1].find(char0)+1 : tmp1[1].find(char0)])
				tmp3 = tmp2[0].split(",")
				lats.append(tmp3[0])
				lons.append(tmp3[1])
				names.append(address)
	createKML(names,lons,lats)

def createKML(names,lons,lats):
	kml = simplekml.Kml()
	print(str(len(names))+" "+str(len(lons))+" " + str(len(lats)))
	for i in range(0,len(names)):
		kml.newpoint(name=names[i], coords=[(lons[i],lats[i])])  # lon, lat, optional height
	for x in range(0,999999):
		pathName = "C:/trace_maps/trace_map_"+str(x)+".kml"
		myFile = Path(pathName)
		if not myFile.is_file():
			kml.save(pathName)
			openGE(pathName)
			break

def openGE(filename):
	os.system("\"C:/Program Files (x86)/Google/Google Earth Pro/client/googleearth.exe\" "+filename)


newpath = "C:/trace_maps/"
if not os.path.exists(newpath):
    os.makedirs(newpath)

traceroute("www.hyundai.com.au")