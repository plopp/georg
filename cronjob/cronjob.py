#!/usr/bin/env python
import json
import urllib2
georgUrl = "http://localhost:3000/collectionapi/events"
georgEvents = []

def main():
	print("main")
	georgGetAll()
	#georgPut()
	georgCheckAndPut("Beskrivningyo", 57, 12)

def georgCheckAndPut(description, lat, lon):
	for value in georgEvents:
		if description == value["description"]:
			return
	georgPut(description, lat, lon)

def georgPut(description, lat, lon):
	#[{
	#	"_id":"LEshFkwmcyLy86qS2",
	#	"description":"Beskrivning",
	#	"lat":57,
	#	"lon":12,
	#	"visible":false
	#}]
	data = {
		"description": description,
		"lat": lat,
		"lon": lon,
		"visible": True
	}

	req = urllib2.Request(georgUrl)
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))

def georgGetAll():
	global georgEvents

	req = urllib2.Request(georgUrl)
	response = urllib2.urlopen(req)

	georgEvents = json.load(response)

	#print georgEvents

if __name__ == '__main__':
	#Call Main-function
	main()


