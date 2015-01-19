#!/usr/bin/env python
# -*- coding: utf-8 -*-
import georgapi

def main():
	print("main - Demo of API-functions")

	print "Demo get all"
	georgEvents = georgapi.GetAllEvents()
	print georgEvents
	print ""


	print "API return None if empty"
	if georgEvents == None:
		print "georgEvents is none"
	else:
		print "georgEvents have data"
	print ""


	print "Add data"
	data1 = {
		"description": "beskrivninggg 1",
		"lat": 57.5,
		"lon": 12,
		"visible": True
	}
	data2 = {
		"description": "Beskrivning 2",
		"lat": 55,
		"lon": 11,
		"visible": True
	}
	print data1
	print data2
	georgapi.EventCreate(data1)
	georgapi.EventCreate(data2)
	print ""


	print "Find data literary"
	dictFind = {
		"lat": 57.5,
		"lon": 12
	}
	findResult1 = georgapi.FindEvents(dictFind, False)
	print dictFind
	print findResult1
	print ""


	print "Find data using regex"
	dictFind = {
		"description": ".*riv.*"
	}
	findResult2 = georgapi.FindEvents(dictFind, True)
	print dictFind
	print findResult2
	print ""

	#georgapi.DeleteEvent("oyGi9PxoqEZ6XSn3K")

	print "Modify existing event"
	if findResult1 is not None:
		data1 = findResult1
		print data1
		data1[0]["lon"] = 10
		print georgapi.UpdateEvent(findResult1[0]["_id"], data1[0])
		print findResult1
		print data1
	else:
		print "findResult1 is none"
	print ""


	print "Get event by id"
	print georgapi.GetEvent(findResult1[0]["_id"])
	print ""


	print "Delete by id"
	print georgapi.DeleteEvent(findResult1[0]["_id"])
	print georgapi.DeleteEvent(findResult2[0]["_id"])
	print ""


	#Find all events of a description and delete them
	dictFind = {
		"description": "beskrivninggg 1"
	}
	findResult1 = georgapi.FindEvents(dictFind, False)
	if findResult1 is not None:
		for item in findResult1:
			georgapi.DeleteEvent(item["_id"])

	dictFind = {
		"description": "Beskrivning 2"
	}
	findResult1 = georgapi.FindEvents(dictFind, False)
	if findResult1 is not None:
		for item in findResult1:
			georgapi.DeleteEvent(item["_id"])

if __name__ == '__main__':
	#Call Main-function
	main()

