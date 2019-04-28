##!/usr/bin/env python3'
## -*- coding: utf-8 -*-



import csv
import sys
import json


#wget http://www.minsktrans.by/city/minsk/routes.txt
#wget http://www.minsktrans.by/city/minsk/stops.txt
#wget http://www.minsktrans.by/city/minsk/times.txt

'''
CREATE DATABASE public_transport;
ctrl+d
psql public_transport
CREATE TABLE minsktrans 
(
	id SERIAL PRIMARY KEY,
	city varchar(64),
	area varchar(128),
	street varchar(128),
	name varchar(128),
	info varchar(128),
	lng  int,
	lat = int,
	stops = varchar(32),
	stopNum = varchar(32)
);
  
ALTER TABLE minsktrans ADD COLUMN id SERIAL PRIMARY KEY;


CREATE USER pb_user WITH password 'pb_password';


GRANT ALL privileges ON DATABASE minsktrans TO pb_user;

CREATE DATABASE osm;
GRANT ALL privileges ON DATABASE osm TO pb_user;

psql -d osm -c 'CREATE EXTENSION postgis; CREATE EXTENSION hstore;'

'''

#https://pygtfs.readthedocs.io/en/latest/
#http://avtobusing.ru/gtfs/reference.html




def addStop():
	print ("Add stop")



def openFile():

	
	
	jsonFile = {}
	stopIdName = {}
	
	with open('stops.txt') as stopsFile:
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
			
			#~ j['area'] = area
			#~ j['city'] = city
			#~ j['street'] = street
			#~ j['info'] = info

			#~ j['stops'] = stopsArray
			#~ j['stopNum'] = stopNum
			
			stopsArray= []
			if len(stops) > 0:
				stopsArraySting = stops.split(',')
				for s in stopsArraySting:
					stopsArray.append(int(s))	
			
			jsonArray.append(j)
		
					
		with open('stops.json', 'w') as outfile:
			outfile.write("stops = ")
			json.dump(jsonArray, outfile, ensure_ascii=False) #.encode('utf8')






openFile()

    
#  to GTFS






