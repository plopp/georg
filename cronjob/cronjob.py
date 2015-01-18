#!/usr/bin/env python
import json
import urllib2
georgUrl = "http://localhost:3000/collectionapi/events"

def main():
	print("main")
	georgPut()

def georgPut():
	#[{
	#	"_id":"LEshFkwmcyLy86qS2",
	#	"description":"Beskrivning",
	#	"lat":57,
	#	"lon":12,
	#	"visible":false
	#}]
	data = {
		"description": "Beskrivning1",
		"lat": 57,
		"lon": 12,
		"visible": True
	}

	req = urllib2.Request(georgUrl)
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))

	print response

if __name__ == '__main__':
	#Call Main-function
	main()


