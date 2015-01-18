#!/usr/bin/env python
# -*- coding: utf-8 -*-
import georgapi

georgEvents = []
georgPositions = []

def main():
	print("main")
	global georgEvents
	global georgPositions
	
	georgEvents = georgapi.GetAllEvents()
	#print georgEvents

	if georgEvents == None:
		print "georgEvents none"
	else:
		print "georgEvents data"

	data = {
		"description": "description beskrivninggg",
		"lat": 57.5,
		"lon": 12,
		"visible": True
	}
	print georgapi.EventCreate(data)

	georgPositions = georgapi.GetAllPositions()

	georgapi.UpdateEvent("qnu5J5kBpaPaa6NAk", data)

	print georgapi.GetEvent("9KXMXNsCE7XyyEaBL")


if __name__ == '__main__':
	#Call Main-function
	main()

