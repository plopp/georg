#!/usr/bin/env python
# -*- coding: utf-8 -*-
import georgapi
import urllib2
import re
from lxml import etree
from lxml.html import fromstring, tostring
import time

georgEvents = []
georgPositions = []

def main():
	print("Fetch water and sewage updates in gbg")
	global georgEvents
	global georgPositions

	gbgurl = "http://goteborg.se/wps/portal/invanare/bygga-o-bo/vatten-och-avlopp/vattenlackor-avbrott/pagaende-vatten--och-avloppsarbeten/!ut/p/b1/04_Sj9Q1MTc2Mzc2NzPVj9CPykssy0xPLMnMz0vMAfGjzOIDDL0CLZwMHQ383S3dDDxDvAPc_Lx9_L1DjYEKIoEKDHAARwNC-v088nNT9XOjciwAr5DUwA!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/"

	#Get page
	request = urllib2.Request(gbgurl)
	rawPage = urllib2.urlopen(request)
	read = rawPage.read()
	#print read
	tree = etree.HTML(read)    

	#<div id="readThis" class="article">
	#print tree.xpath("//div[@id = 'readThis']/h2")

	#Loop through HTML-h2-elements in a specific div-element
	for h2 in tree.xpath("//div[@id = 'readThis']/h2"):
		print h2.text
		matchobjI = re.match(r'.* i (.+)$', h2.text)
		matchobjPa = re.match(r'.* p. (.+)$', h2.text)
		city = ""
		if matchobjI:
			city = matchobjI.group(1).encode('utf-8')
		if matchobjPa:
			city = matchobjPa.group(1).encode('utf-8')

		#Do we have a city parsed?
		if len(city) > 0:
			city += ", Göteborg"
			print city
			cityJson = {}
			cityJson = georgapi.addressToLatLong(city)
			#Did we get a result from OpenStreetmaps?
			if len(cityJson) > 0:
				print city+" was found on OpenStreetmaps"
				#Check if event exists from before in DB
				dictFind = {
					"description": h2.text,
					"lat": float(cityJson[0]["lat"]),
					"lon": float(cityJson[0]["lon"]) 
				}
				print dictFind
				findResult1 = georgapi.FindEvents(dictFind, False)

				if findResult1 is not None:
					print "Found in DB"
					print findResult1
				else:
					print "Not found in DB"
					georgapi.EventCreate(dictFind)
			else:
				print city+" was not found at OpenStreetmaps"
			time.sleep(1)
		print ""

if __name__ == '__main__':
	#Call Main-function
	main()

