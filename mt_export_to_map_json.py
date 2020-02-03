##!/usr/bin/env python3'
## -*- coding: utf-8 -*-



import csv
import sys
import json
from mt_download import lastVersionFile

stopsJson = 'map/maps/stops.json'

def addStop():
	print ("Add stop")



def openFile():	
	
	jsonFile = {}
	stopFile = lastVersionFile('stops')
	
	with open(stopFile) as stopsFile:
		stopsCSV = csv.reader(stopsFile, delimiter=';')
		
		header_row = next(stopsCSV)
		stopsStructure = {}
		jsonArray = []
		
		for row in stopsCSV:   
			
			id = int(row[0])
			city = row[1] 
			area = row[2]
			street = row[3]
			
			if row[4]:
				name = row[4]				
			
			info = row[5]
			lng = float(row[6]) / 100000
			lat = float(row[7]) / 100000
			
			if lat < 1 or lng < 1:
				continue
			
			stops = row[8]
			stopNum = row[9]
				
			j={}
			
			j['id'] = id

			j['name'] = name
			j['lat'] = lat
			j['lon'] = lng
						
			stopsArray= []
			if len(stops) > 0:
				stopsArraySting = stops.split(',')
				for s in stopsArraySting:
					stopsArray.append(int(s))	
			
			jsonArray.append(j)
		
		with open(stopsJson, 'w') as outfile:
			outfile.write("stops = ")
			json.dump(jsonArray, outfile, ensure_ascii=False) #.encode('utf8')


if __name__ == "__main__":
    openFile()







